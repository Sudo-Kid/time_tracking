from django.shortcuts import render
from django.views import View

from . import forms


class Index(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return render(request, self.template_name, {})
        else:
            auth_form = forms.LoginForm()
            return render(request, self.template_name, {'auth_form': auth_form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return render(request, self.template_name, {})
        else:
            auth_form = forms.LoginForm()
            return render(request, self.template_name, {'auth_form': auth_form})
