from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from visual.models import Visual, Type, Review
from visual.helper import formHelper, importHelper
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import requests
import os

# Create your views here.

def home(request):
    user = request.user
    current_path = request.get_full_path()
    sort = request.GET.get('sort')
    if sort:
        visuals = Visual.objects.order_by('-' + sort)
    else:
        visuals = Visual.objects.all()
    return render(request, 'visual/home.html', {'visuals' : visuals, 'user' : user, 'current_path' : current_path})

def type_visuals(request, id):
    visuals = Visual.objects.filter(visual_type__id=int(id))
    return render(request, 'visual/type.html', {'visuals' : visuals})

def detail(request, id):
    visual = get_object_or_404(Visual, pk=id)
    view_count = visual.view_count
    view_count += 1
    visual.view_count = view_count
    visual.save()
    reviews = visual.review_set.all()
    types = visual.visual_type.all()
    return render(request, 'visual/detail.html', {'visual' : visual, 'types' : types, 'reviews' : reviews})

def add(request):
    visual_types = Type.objects.all()
    if request.method == 'POST':
        visual = Visual.objects.create()
        visual = formHelper(visual, request)
        visual.save()
        return redirect('/dashboard')
    if request.user.is_superuser:
        return render(request, 'visual/add.html', {'types' : visual_types})
    else:
        return HttpResponseRedirect('/')

def edit(request, id):
    visual = Visual.objects.get(id=int(id))
    visual_types = Type.objects.all()
    if request.method == 'POST':
        print(request.POST.get('visual_types'))
        visual = formHelper(visual, request)
        visual.save()
        #return redirect('/dashboard')
    if request.user.is_superuser:
        return render(request, 'visual/edit.html', {'visual' : visual, 'types' : visual_types})
    else:
        return HttpResponseRedirect('/')

@csrf_exempt
def ajax_submit_review(request):
    if request.method == 'POST':
        user = request.user
        content = request.POST.get('content')
        visual_id = request.POST.get('visual_id')
        visual = Visual.objects.get(id=int(visual_id))
        review = Review.objects.create(content=content, visual=visual, user=user)
        review.save()
        response = {'status' : 'success', 'user' : user.username}
        return JsonResponse(response)

def export(request):
    visuals = Visual.objects.all()
    
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'douban.txt')
    douban = "";
    douban_file = open(file_path, "w")
    for visual in visuals:
        douban += visual.douban_id + "\n"
    douban_file.write(douban)
    return HttpResponse(douban, content_type='text/plain')

def importVisual(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'douban.txt')
    doubans = open(file_path, "r+")
    for douban in doubans:
        douban = douban.strip()
        douban_api = "https://api.douban.com/v2/movie/subject/" + douban
        response = requests.get(douban_api)
        data = response.json()
        visual = Visual.objects.create()
        visual = importHelper(visual, data)
        visual.save()
    return HttpResponse("import success")