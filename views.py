from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db.models import Q
from .models import Listing, Category
from .forms import ListingForm
from .decorators import unauthenticated_user, allowed_users


def index(request):
    listings = Listing.objects.all()
    context = {'listings': listings}
    return render(request, 'board/index.html', context)


@unauthenticated_user
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken.')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'This email is already taken.')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Account created successfully.')
                login(request, user)
                return redirect('index')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')
    return render(request, 'board/signup.html')


@unauthenticated_user
def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'board/login.html')


def logout_request(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def create_listing(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing
