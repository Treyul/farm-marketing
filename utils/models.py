from django.db import models
from datetime import date

class Farm_Expenses(models.Model):
    
    Type = models.CharField()

    Quantity = models.IntegerField(null=False, default=1)

    amount = models.IntegerField(null=False)

    date = models.DateField(null=False,default=date.today)
    
    Category = models.CharField()
    
    Price = models.IntegerField()

class Farm_Revenue(models.Model):

    Quantity = models.IntegerField(null=False, default=1)

    amount = models.IntegerField(null=False)

    date = models.DateField(null=False, default=date.today)
    
    
class Plant(models.Model):
    
    Plant_Name = models.CharField()
    
    Irrigation_Sequence = models.JSONField()
    
    Nutrition = models.JSONField()
    
    Vulnerabilities_Mitigations = models.JSONField()
    
    Estimatated_Harvest = models.JSONField()
    
    
class Plot_Data(models.Model):
    
    Plant_Name =  models.CharField()
    
    Nursery_PrepDate = models.DateField()
    
    Germination_Date = models.DateField()
    
    Transplanting_Date = models.DateField()
    
    First_Harvest = models.DateField()
    
    Last_Harvest = models.DateField()
    
    Fertilization_Dates = models.JSONField()
    
    Plot_Number = models.IntegerField()
    
    Unit_Price = models.IntegerField()
    
    
