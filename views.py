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
            
            from django.views.generic import ListView
from .models import Category, Subcategory

class CategoryListView(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'
    queryset = Category.objects.all()

class SubcategoryListView(ListView):
    model = Subcategory
    template_name = 'subcategories.html'
    context_object_name = 'subcategories'
    queryset = Subcategory.objects.all()

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # автоматично авторизуємо користувача
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

from django.shortcuts import render
from .models import Ad
from .forms import SearchForm

def search_ads(request):
    ads = Ad.objects.all()
    form = SearchForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        keywords = form.cleaned_data['keywords']
        category = form.cleaned_data['category']
        subcategory = form.cleaned_data['subcategory']
        if keywords:
            ads = ads.filter(title__icontains=keywords) | ads.filter(description__icontains=keywords)
        if category:
            ads = ads.filter(category=category)
        if subcategory:
            ads = ads.filter(subcategory=subcategory)
    context = {'ads': ads, 'form': form}
    return render(request, 'search.html', context)

def sort_by_date(ads):
    return sorted(ads, key=lambda ad: ad.date_created, reverse=True)

def sort_by_price_asc(ads):
    return sorted(ads, key=lambda ad: ad.price)

def sort_by_price_desc(ads):
    return sorted(ads, key=lambda ad: ad.price, reverse=True)

def sort_by_category(ads):
    return sorted(ads, key=lambda ad: ad.category.name)

def sort_by_subcategory(ads):
    return sorted(ads, key=lambda ad: ad.subcategory.name)

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Ad
from .forms import AdForm

@login_required
def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id, user=request.user)
    if request.method == 'POST':
        ad.delete()
        return redirect('ads_list')
    return render(request, 'delete_ad.html', {'ad': ad})

