# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm
from django.views.generic import FormView, TemplateView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
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
# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponseRedirect('/index/')
#                 else:
#                     return HttpResponse('Algo salio mal')
#             else:
#                 return HttpResponse("Invalid Login")
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form':form})
