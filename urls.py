from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('create_listing/', views.create_listing, name='create_listing'),
    path('<int:listing_id>/', views.listing_detail, name='listing_detail'),
    path('<int:listing_id>/edit/', views.edit_listing, name='edit_listing'),
    path('<int:listing_id>/delete/', views.delete_listing, name='delete_listing'),
    path('search/', views.search, name='search'),
    path('category/<str:category>/', views.category, name='category'),
]
