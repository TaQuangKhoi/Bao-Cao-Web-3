from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render


def dashboard(request):
    if request.user.is_authenticated:
        print(request.user.username)
        return render(request, template_name='dashboard.jinja', )
    else:
        return HttpResponseRedirect('/signin/')

