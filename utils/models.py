from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
from hashlib import sha512

# table for the farm owners authentication
class Farm_Owners(models.Model):
    
    def Create_Password(self,password):
        
        self.password  = sha512(password.encode()).hexdigest()
        
    def Confirm_Password(self,password):
        
        Provided_Password = sha512(password.encode()).hexdigest()
        
        if self.password == Provided_Password:
            return True
        elif self.password != Provided_Password:
            return False
# table to hold unique farm ids
class Farms(models.Model):
    
    farm_size = models.IntegerField()
    
    location = models.CharField()

class Plot_subdivision(models.Model):
    
    Section_Number = models.IntegerField()
    
    Previous_Moisture = models.IntegerField()
    
    Current_Moisture = models.IntegerField()
    
    Irrigation_On = models.BooleanField()
    
    Last_Irrigation =  models.DateField()
    
    Active = models.BooleanField()
    # parameters are length, width and area UOM is meters
    dimensions = models.JSONField()
    
class Pesticide_Posession(models.Model):
    
    name = models.CharField()
    
    purpose = models.CharField()
    
    ratio = models.CharField()
    
    redundancy = models.CharField()
    
    application = models.JSONField()
    
    Expiry_Date = models.DateField()

class Pesticide_Application_History(models.Model):
    # takes pesticide possesession id
    
    Application_Date = models.DateField()
    
    purpose = models.CharField()   
    
class Plant_Allocation(models.Model):
    # takes plot id
    
    name = models.CharField()
    
    species = models.CharField()
    
    Harvested = models.BooleanField()
    
    Nursery_Date = models.DateField()
    
    Germination_Date = models.DateField()
    
    Transplanting_Date = models.DateField()
    
    Flowering_Date = models.DateField()
    
    Fruiting_Date = models.DateField()
    
    category = models.CharField()   #perenial or annual crop column to be changed to a boolean value? 
    
class Harvest(models.Model):
    
    Harvest_Date = models.DateField()
    
    Harvest_Amount = models.IntegerField()
    
    Amount_Available = models.IntegerField()
    
class Products_Available(models.Model):
    
    name = models.CharField()
    
    Available_Amount = models.IntegerField()
    
    Price = models.IntegerField()
    
    Last_Update = models.DateField()
    
    Measurement_Unit = models.CharField()
    
class Farm_Assets(models.Model):
    
    name = models.CharField()
    
    category = models.CharField()
    
    date = models.DateField()
    
    Quantity = models.IntegerField()
    
    Price = models.IntegerField()
    
class Farm_Ependiture(models.Model):
    
    name = models.CharField()
    
    category = models.CharField()
    
    date = models.DateField()
    
    Quantity = models.IntegerField()
    
    Price = models.IntegerField()
    
# TODO customer,sales and order table
class Sale(models.Model):
    
    name = models.CharField()
    
    price = models.IntegerField()
    
    Quantity = models.IntegerField()
    
    Date = models.DateField()
    
    
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