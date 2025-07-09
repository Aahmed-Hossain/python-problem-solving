from django.shortcuts import render
from . import models
from django.db.models import Prefetch

# Unoptimized code
# def home(request):
#     car_models = models.CarModel.objects.all()
#     car_details = []
#     for car in car_models:
#         car_details.append({
#             'car_name': car.car_model_name,
#             'car_company': car.car_company.company_name,
#             'ceo_name' : models.Ceo.objects.filter(car_company = car.car_company).first().ceo_name,
#             'fuel_names': [fuel.fuel_name for fuel in models.FuelType.objects.filter(car_models=car)],
#         })
#     return render(request, 'cars/home.html', {'car_details': car_details})

def home(request):
    car_models = models.CarModel.objects.select_related('car_company').prefetch_related(
        Prefetch('car_company__ceo'),
        Prefetch('fueltype_set')
    )
    car_details = []
    for car in car_models:
        car_details.append({
            'car_name': car.car_model_name,
            'car_company': car.car_company.company_name,
            'ceo_name' : models.Ceo.objects.filter(car_company = car.car_company).first().ceo_name,
            'fuel_names': [fuel.fuel_name for fuel in models.FuelType.objects.filter(car_models=car)],
        })
    return render(request, 'cars/home.html', {'car_details': car_details})
