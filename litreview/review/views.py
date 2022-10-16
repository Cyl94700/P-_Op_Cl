from itertools import chain
from django.core.paginator import Paginator
from django.shortcuts import render
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
