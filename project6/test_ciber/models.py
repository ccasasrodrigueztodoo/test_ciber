from django.db import models
from django.utils import timezone
import os, pandas as pd
from jsonfield import JSONField
import json

# Create your models here.

class FilesAdmin(models.Model):
    name = models.CharField(max_length=50)
    upload_date = models.DateField(default=timezone.now)
    adminupload =  models.FileField(upload_to='media', null=False)
    res = JSONField(default='{}')

    def __str__(self):
        return self.name

    
    def read_file(self):
        if self.adminupload: 
            a = self.adminupload
            df = pd.read_excel(a, engine='pyxlsb')     
            arr = df.to_numpy()
            total = df['cantidad de elementos'].sum()
            total_price  = df['precio'].sum()
            average = (df['precio'].sum() / df['cantidad de elementos'].count())
            values = dict(elementos = total,  promedio= average )
            self.res = json.dumps(values, sort_keys=True)
            for line in arr:
                serie_number = line[0]
                amount_elements = line[1]
                price = line[2]
                Stock.objects.create(serie_number=serie_number, amount_elements=amount_elements, price=price)

                    


        
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
