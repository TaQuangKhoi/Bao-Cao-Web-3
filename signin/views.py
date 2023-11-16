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

    return render(
        request,
        template_name='signin.jinja',
        context={'form': form}
    )
