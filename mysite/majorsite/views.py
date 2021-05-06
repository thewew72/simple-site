from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.decorators.http import require_http_methods
from django.utils import timezone

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

#from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block
from friendship.models import FriendshipRequest

from .forms import AvatarForm, AudiosForm, PostForm

from majorsite.models import UserFiles, Post

User = get_user_model()

def index(request):

    context = {}

    return render(request, 'majorsite/index.html', context)

def all_users(request):

    user = get_user_model()
    users = user.objects.all()

    context = {'users': users}

    return render(request, 'majorsite/all_users.html', context)

def showfriends(request):

    friends = Friend.objects.friends(request.user)
    
    context = {'friends': friends}

    return render(request, 'majorsite/friends.html', context)

def personalpage(request, id):

    page_owner = User.objects.get(pk=id)
    fname = page_owner.first_name
    lname = page_owner.last_name
    avatar = page_owner.avatar

    posts = Post.objects.filter(author=id)

    context = {'fname': fname,
                'lname': lname,
                'page_owner': page_owner,
                'avatar': avatar,
                'posts': posts}

    return render(request, 'majorsite/personalpage.html', context)

def show_requests(request):

    items = Friend.objects.requests(request.user)

    context = {'items': items}

    return render(request, 'majorsite/show_requests.html', context)

@require_http_methods("POST")
@login_required
def add_friend(request, slug):
    page_owner = User.objects.get(username=slug)
    Friend.objects.add_friend(request.user, page_owner)

    return redirect('/')

@require_http_methods("POST")
@login_required
def accept_friend(request, id):
    friend_request = FriendshipRequest.objects.get(from_user=id)
    friend_request.accept()

    return redirect('/')

@require_http_methods("POST")
@login_required
def reject_friend(request, id):
    friend_request = FriendshipRequest.objects.get(from_user=id)
    friend_request.reject()
    friend_request.cancel()

    return redirect('/')

@login_required
def define_avatar(request):
    if request.method == 'POST':
        #profile = User.objects.get(id=request.user)
        profile = User.objects.get(username=request.user)

        form = AvatarForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()

    else:
        form = AvatarForm()

    return render(request, 'majorsite/define_avatar.html', {'form': form})

def audios(request, id):

    user = User.objects.get(pk=id)
    audios = UserFiles.objects.filter(user=user)

    context = {'audios': audios}

    return render(request, 'majorsite/audios.html', context)

@login_required
def audios_upload(request):
    if request.method == 'POST':

        form = AudiosForm(request.POST, request.FILES)
        user = request.user

        if form.is_valid():
            audio = form.save(commit=False)
            audio.user_id = user.id
            audio.save()


    else:
        form = AudiosForm()

    return render(request, 'majorsite/audios_upload.html', {'form': form})

@login_required
def post_create(request):
    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)
        user = request.user

        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = user.id
            post.save()


    else:
        form = PostForm()

    return render(request, 'majorsite/post_create.html', {'form': form})


