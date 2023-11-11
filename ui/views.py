from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, template_name='dashboard.jinja',)

def up_rank(request):
    return render(request, template_name='up_rank.jinja',)
