from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.conf import settings
from django.contrib import messages


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
def profile(request):

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
        'title': 'Profil'
    }

    return render(request, 'authentication/profile.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')
