from django.contrib.auth import logout
from django.http import HttpResponseRedirect


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')