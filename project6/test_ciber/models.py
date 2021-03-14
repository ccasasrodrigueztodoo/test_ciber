from django.db import models
from django.utils import timezone
import os, pandas as pd

# Create your models here.

class FilesAdmin(models.Model):
    name = models.CharField(max_length=50)
    upload_date = models.DateField(default=timezone.now)
    adminupload =  models.FileField(upload_to='media', null=False)

    def __str__(self):
        return self.name

    
    def read_file(self):
        if self.adminupload: 
            a = self.adminupload
            df = pd.read_excel(a, engine='pyxlsb')
            print(df)
            print(type(df))
            dd = pd.DataFrame()
            print('hello')
            print(dd)


        
    def save(self, *args, **kwargs):
        self.read_file()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        #do_something_else()

class Stock(models.Model):
    serie_number = models.CharField(max_length=50)
    amount_elements =  models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()
