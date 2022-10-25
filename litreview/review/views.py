from itertools import chain
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from . import forms, models


@login_required
def feed(request):
    tickets = models.Ticket.objects.filter(
        user__in=request.user.follows.all()
    )
    reviews = models.Review.objects.filter(
        user__in=request.user.follows.all()
    )
    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )

    paginator = Paginator(tickets_and_reviews, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'page_obj': page_obj
    }

    return render(
        request,
        'review/feed.html',
        context
     )


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            if form.cleaned_data['image']:
                ticket.image = form.cleaned_data['image']
            ticket.save()
            return redirect('feed')
    context = {
        'form': form
    }
    return render(
        request,
        'feed/create_ticket.html',
        context
    )


@login_required
def create_review(request, ticket_id):
    form = forms.ReviewForm()
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = get_object_or_404(models.Ticket, id=ticket_id)
            review.ticket.has_review = True
            review.ticket.save()
            review.save()
            return redirect('feed')
    context = {
        'both': False,
        'form': form
    }
    return render(
        request,
        'feed/create_review.html',
        context
    )


@login_required
def create_ticket_and_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            if ticket_form.cleaned_data['image']:
                ticket.image = ticket_form.cleaned_data['image']
            ticket.has_review = True
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = get_object_or_404(models.Ticket, id=ticket.id)
            review.save()
            return redirect('feed')
    context = {
        'both': True,
        'ticket_form': ticket_form,
        'review_form': review_form
    }
    return render(
        request,
        'feed/create_review.html',
        context
    )