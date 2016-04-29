from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from visual.models import Visual
from visual.helper import formHelper

# Create your views here.

def home(request):
    visuals = Visual.objects.all()
    return render(request, 'home.html', {'visuals' : visuals})

def detail(request, id):
    visual = Visual.objects.get(id=int(id))
    
    return render(request, 'detail.html', {'visual' : visual})

def add(request):
    if request.method == 'POST':
        visual = Visual.objects.create()
        visual = formHelper(visual, request)
        visual.save()
        return redirect('/')
    return render(request, 'add.html')

def edit(request, id):
    visual = Visual.objects.get(id=int(id))
    if request.method == 'POST':
        visual = formHelper(visual, request)
        visual.save()
        return redirect('/')
    return render(request, 'edit.html', {'visual' : visual})
