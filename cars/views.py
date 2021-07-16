from django.shortcuts import get_object_or_404, render
from .models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_at')
    pagimator = Paginator(cars, 2)
    page = request.GET.get('page')
    paged_cars = pagimator.get_page(page)
    data = {
        'cars': paged_cars,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)

    data = {
        'single_car':single_car
    }
    return render(request, 'cars/car_detail.html', data)

def search(request):
    cars = Car.objects.order_by('-created_at')
    data = {
        'cars': cars,
    }
    return render(request, 'cars/search.html', data)