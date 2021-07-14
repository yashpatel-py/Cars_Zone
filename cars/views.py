from django.shortcuts import get_object_or_404, render
from .models import Car

# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_at')
    data = {
        'cars': cars,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)

    data = {
        'single_car':single_car
    }
    return render(request, 'cars/car_detail.html', data)