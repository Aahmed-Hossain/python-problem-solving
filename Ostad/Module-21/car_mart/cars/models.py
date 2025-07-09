from django.db import models

class CarCompany(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class Ceo(models.Model):
    ceo_name = models.CharField(max_length=100)
    car_company = models.OneToOneField(CarCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.ceo_name

class CarModel(models.Model):
    car_model_name = models.CharField(max_length=100)
    car_company = models.ForeignKey(CarCompany, on_delete=models.CASCADE) #ForeignKey refers many to one

    def __str__(self):
        return self.car_model_name

class FuelType(models.Model):
    fuel_name = models.CharField(max_length=100)
    car_models = models.ManyToManyField(CarModel)
    def __str__(self):
        return self.fuel_name
