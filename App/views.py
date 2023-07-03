from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Restaurant, Item
# from django.db.models import Q


# Create your views here.

class HomeView(TemplateView):
    template_name = 'base.html'


class RestaurantView(ListView):
    model = Restaurant
    queryset = Restaurant.objects.all()
    context_object_name = 'restaurant_list'
    template_name = 'App/restaurant_list.html'


def RestaurantDetailView(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    data = Item.objects.filter(restaurant__id=pk)
    return render(request,'App/restaurant_detail.html',{"data":data,"restaurant":restaurant})


def SearchingView(request):
    if request.method == "POST":
        searched = request.POST['search']
        # items = Item.objects.filter(item_name__icontains=searched)
        restaurants = Restaurant.objects.filter(item__item_name__icontains=searched).distinct()
        return render(request,'App/search_venues.html',{"searched":searched,"restaurants":restaurants},)