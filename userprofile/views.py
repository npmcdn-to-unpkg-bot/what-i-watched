from django.shortcuts import render, redirect, get_object_or_404
from userprofile.models import UserProfile
from django.contrib.auth.models import User

# Create your views here.
def detail(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'userprofile/detail.html', {'user' : user,})

def edit(request, id):
    pass