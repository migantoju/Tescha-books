# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm, ProfileForm, UserForm
from django.views.generic import FormView, TemplateView, RedirectView
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Profile
from django.db import transaction
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.http import JsonResponse
from django.views.decorators.debug import sensitive_variables
# Create your views here.
class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)
@sensitive_variables('username')
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Ya existe un usuario con este correo electronico'
    return JsonResponse(data)
@sensitive_variables('new_user')
def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
                #Creamos un nuevo objeto usuario
                new_user = user_form.save(commit=False)
                #insertamos la contraseña
                new_user.set_password(user_form.cleaned_data['password'])
                #Guardamos el objeto usuario
                new_user.save()
                return render(request, 'registration/register_done.html', {'user_form': user_form})
        else:
            user_form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'user_form': user_form})

@login_required
def profile_page(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user/profile.html', {'usuario':user})

@login_required
@transaction.atomic
def update_profile(request, username):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('Profile', username=username)
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'user/profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
from .filters import UserFilter
#Django filter
def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'user/user_list.html', {'filter': user_filter})
