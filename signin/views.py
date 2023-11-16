from django.shortcuts import render

from signin.forms import SignInForm


def signin(request):
    form = SignInForm()

    return render(
        request,
        template_name='signin.jinja',
        context={'form': form}
    )
