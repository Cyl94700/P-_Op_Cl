from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.conf import settings
from django.contrib import messages
from review.models import Ticket, Review
from authentication.models import User


from . import forms


class LoginPage(View):
    form_class = forms.LoginForm
    template_name = 'authentication/login.html'

    def get(self, request):
        form = self.form_class
        message = ''
        context = {
            'form': form,
            'message': message
        }
        return render(
            request,
            self.template_name,
            context
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('feed')

        message = 'Identifiants invalides.'
        context = {
            'form': form,
            'message': message
        }
        return render(
            request,
            self.template_name,
            context
        )


class SignupPage(View):
    form_class = forms.SignupForm
    template_name = 'authentication/signup.html'

    def get(self, request):
        form = self.form_class
        context = {
            'form': form
        }
        return render(
            request,
            self.template_name,
            context
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        context = {
            'form': form
        }
        return render(
            request,
            self.template_name,
            context
        )


@login_required
def profile(request, user):
    user = User.objects.get(username=user)
    if request.method == 'POST':
        user_form = forms.UserUpdateForm(request.POST, instance=request.user)
        photo_form = forms.PhotoUpdateForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid() and photo_form.is_valid():
            user_form.save()
            photo_form.save()
            messages.success(request, f'Votre profil a été modifié!')
            return redirect('profile')

    else:
        user_form = forms.UserUpdateForm(instance=request.user)
        photo_form = forms.PhotoUpdateForm(instance=request.user)

    context = {
        'user_form': user_form,
        'photo_form': photo_form,
        'requested_user': user,
        'title': 'Profil'
    }

    return render(request, 'authentication/profile.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def followers_page(request, user):
    search_form = forms.SearchUser()
    searched_user_resp = ""
    requested_user = User.objects.get(username=user)
    # search
    searched_user_resp_btn = ''

    # get follows and followers
    user_follows = requested_user.follows.all()
    user_followers = requested_user.followed_by.all()

    group_follows_users = {}
    for user in user_follows:
        follow_form = forms.FollowUserButton(initial={'user_to_follow': user.id})
        group_follows_users[user] = follow_form

    if request.method == 'POST':

        # search form
        if request.POST.get('search_user_id'):
            search_form = forms.SearchUser(request.POST)
            if search_form.is_valid():
                query = search_form.cleaned_data['search']
                searched_user = User.objects.filter(username__icontains=query).first()
                if searched_user:
                    searched_user_resp = searched_user
                    searched_user_resp_btn = forms.FollowUserButton(initial={'user_to_follow': searched_user.id})

        # follow / unfollow button
        else:
            follow_form = forms.FollowUserButton(request.POST)
            if follow_form.is_valid():
                user_to_follow = get_object_or_404(User, id=follow_form.cleaned_data['user_to_follow'])
                if request.user.follows.filter(id=user_to_follow.id).exists():
                    request.user.follows.remove(user_to_follow)
                    user_to_follow.followed_by.remove(request.user)
                else:
                    request.user.follows.add(user_to_follow)
                    user_to_follow.followed_by.add(request.user)

    context = {
        'search_form': search_form,
        'searched_user_resp': searched_user_resp,
        'searched_user_btn': searched_user_resp_btn,
        'requested_user': requested_user,
        'user_follows': user_follows,
        'group_user_follows': group_follows_users,
        'user_followers': user_followers
    }
    return render(
        request,
        'authentication/followers.html',
        context
    )
