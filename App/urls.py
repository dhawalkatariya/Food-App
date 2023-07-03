from django.urls import path
from .views import RestaurantView, HomeView, RestaurantDetailView,SearchingView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('restaurants/', RestaurantView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetailView,name='restaurant-detail'),
    path('search_venues/',SearchingView,name="search-venues"),
]