from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name='Student Name')
    roll = models.IntegerField(unique=True, null=False)
    father_name = models.CharField(max_length=50, verbose_name='Father Name')
    mother_name = models.CharField(max_length=80, blank=True, null=False)

    def __str__(self):
        return f'Name:{self.name},  Roll:{self.roll}'

class Blog(models.Model):
    name = models.TextField( verbose_name='Blog Name')
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'ID:{self.id}, Name:{self.name}'
