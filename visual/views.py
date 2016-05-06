from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from visual.models import Visual
from visual.helper import formHelper, importHelper
import requests

# Create your views here.

def home(request):
    sort = request.GET.get('sort')
    if sort:
        visuals = Visual.objects.order_by('-' + sort)
    else:
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

def export(request):
    visuals = Visual.objects.all()
    douban = "";
    douban_file = open("douban.txt", "w")
    for visual in visuals:
        douban += visual.douban_id + "\n"
    douban_file.write(douban)
    return HttpResponse(douban, content_type='text/plain')

def importVisual(request):
    doubans = open("douban.txt", "r+")
    for douban in doubans:
        douban = douban.strip()
        douban_api = "https://api.douban.com/v2/movie/subject/" + douban
        response = requests.get(douban_api)
        data = response.json()
        visual = Visual.objects.create()
        visual = importHelper(visual, data)
        visual.save()
    return HttpResponse("import success")

def test(request):
    return HttpResponse("test");