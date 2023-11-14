from django.shortcuts import render


def signin(request):
    return render(request, template_name='signin.jinja', )
