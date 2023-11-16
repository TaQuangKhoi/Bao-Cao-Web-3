from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

from signin.forms import SignInForm


def signin(request):
    form = SignInForm()

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data['username']
            password = cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
            else:
                print('The username and password were incorrect.')
                form.add_error(None, 'Invalid username or password')

    return render(
        request,
        template_name='signin.jinja',
        context={'form': form}
    )


def logout_view(request):
    logout(request)
