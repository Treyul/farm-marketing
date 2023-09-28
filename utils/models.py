from django.db import models
from datetime import date
from hashlib import sha512
"""
TODO replicate pesticide table to create fertilizer tables ***DONE
     table to hold plant general info ***DONE
     enable user to search for pesticide they may use by plant and pest
     customer,sales and order table
     sales to be grouped by plant? adv?? or remain as is
     ****check on process of selling farm assets and consumables(fertilizers and pesticides)
    things to have their own uuid?
"""

# table for the farm owners authentication
class Farm_Owners(models.Model):
    
    password = models.CharField(max_length=255,null=False)
    
    last_login = models.DateField(null=False)
    
    username = models.CharField(null=False,max_length=30)
    
    full_names = models.CharField(null=False, max_length=140)
    
    Creation_Date = models.DateField(null=False, default=date.today)
        
    def Create_Password(self,password):
        
        self.password  = sha512(password.encode()).hexdigest()
        
    def Confirm_Password(self,password):
        
        Provided_Password = sha512(password.encode()).hexdigest()
        
        if self.password == Provided_Password:
            return True
        elif self.password != Provided_Password:
            return False

class Things_UUID(models.Model):
    
    uuid = models.CharField(null=False,unique=True,max_length=255)
    
    owner_id = models.ForeignKey(Farm_Owners,on_delete=models.CASCADE,null=False,related_name="id_card")    
# table to hold unique farm ids
class Farms(models.Model):
        
    owner_id = models.ForeignKey(Farm_Owners,on_delete=models.CASCADE, null=False,related_name="farm")
    
    farm_size = models.IntegerField(null=True)
    
    location = models.CharField(null = False,max_length=100)
    
    Current_Temperature = models.IntegerField()

class Plot_subdivision(models.Model):
    
    Farm_id = models.ForeignKey(Farms,on_delete=models.CASCADE, null=False,related_name="section")
    
    Section_Number = models.IntegerField(null=False)
    
    Previous_Moisture = models.IntegerField()
    
    Current_Moisture = models.IntegerField()
    
    Irrigation_On = models.BooleanField()
    
    Last_Irrigation =  models.DateField(null=False,default=date.today)
    
    Active = models.BooleanField()
    # parameters are length, width and area UOM is meters
    dimensions = models.JSONField()
     
class Plant_Allocation(models.Model):
    
    plot_id = models.ForeignKey(Plot_subdivision,on_delete=models.CASCADE, null=False,related_name="plants")
    
    name = models.CharField(null=False,max_length=50)
    
    species = models.CharField(null=False,max_length=50)
    
    category = models.CharField(max_length=25,null=False)   #perenial or annual crop column to be changed to a boolean value? 
    # only applicable to annual crops *TODO* to be removed*
    Harvested = models.BooleanField(default=False)
    
    Nursery_Date = models.DateField(null=True)
    
    Germination_Date = models.DateField(null=True)
    
    Transplanting_Date = models.DateField(null=True)
    
    Flowering_Date = models.DateField(null=True)
    
    Fruiting_Date = models.DateField(null=True)
    
    First_Harvest_Date = models.DateField(null=True)
    
    Harvest_End = models.DateField(null=True)
    
class Harvest(models.Model):
    
    plant_id = models.ForeignKey(Plant_Allocation,on_delete=models.CASCADE, null=False,related_name="harvest")
    
    Harvest_Date = models.DateField(null=False)
    
    Harvest_Amount = models.IntegerField(null=False)
    
class Products_Available(models.Model):
    
    plant_id = models.ForeignKey(Plant_Allocation,unique=True,on_delete=models.CASCADE, null=False,related_name="available_products")
    
    Available_Amount = models.IntegerField(null=False)
    
    Sold_Amount = models.IntegerField(null=False,default=0)
     
    Price = models.IntegerField(null=False)
    
    Last_Update = models.DateField(null=False,default=date.today)
    
    Measurement_Unit = models.CharField(max_length=10,null=False)
       
class Farm_Ependiture(models.Model):
    
    farm_id = models.ForeignKey(Farms,on_delete=models.CASCADE, null=False,related_name="expenditure")
    
    name = models.CharField(null=False,max_length=50)
    # categories include wages, Equipment, pesticide, fertlizers
    category = models.CharField(max_length=25,null=False)
    
    date = models.DateField(null=False,default=date.today)
    
    Bought_From = models.CharField(null=True, max_length=50)
    
    Price = models.IntegerField(null=False)

class Farm_Assets(models.Model):
    
    Expenditure_id = models.ForeignKey(Farm_Ependiture,on_delete=models.CASCADE, null=False,related_name="assets")
    #machinery,piping
    category = models.CharField(max_length=25, null=False)

    Measurement_Unit = models.CharField(null=False,max_length=10)
    
    Quantity = models.IntegerField(null=False)
     
class Sales(models.Model):
    
    product_id = models.ForeignKey(Products_Available,on_delete=models.CASCADE, null=False,related_name="sales")
    
    price = models.IntegerField(null=False)
    
    Quantity = models.IntegerField(null=False)
    
    Date = models.DateField(null=False,default=date.today)
     
class Farm_Revenue(models.Model):
    
    Farm_id = models.ForeignKey(Farms,on_delete=models.CASCADE, null=False,related_name="revenues")

    Quantity = models.IntegerField(null=False, default=1)

    amount = models.IntegerField(null=False)

    date = models.DateField(null=False, default=date.today)
    
"""
    Contains plant optimum conditions where the plant data 
    will be crossed checked to ensure plant is receiving maximum care or
    provide farmer quick trouble shooting to problems
"""
class Plant(models.Model):
    
    Plant_Name = models.CharField(null=False,max_length=25)
    
    Irrigation_Sequence = models.JSONField()
    
    Nutrition = models.JSONField()
    
    Vulnerabilities_Mitigations = models.JSONField()
    
    Estimatated_Harvest = models.JSONField()

class Fertilizer_Posession(models.Model):
    
    Expenditure_id = models.ForeignKey(Farm_Ependiture,on_delete=models.CASCADE, null=False,related_name="fertilizers")
    
    purpose = models.CharField(null=False, max_length=100)
    
    Quantity = models.IntegerField(null=False)
    
    Measurement_Unit = models.CharField(null=False,max_length=10)
    
    ratio = models.CharField(max_length=10,null=False)
    # how often should it be applied
    redundancy = models.CharField(null=False,max_length=10)
    
    application = models.JSONField()
    
    Expiry_Date = models.DateField(null=False)
    
    # if the pestcide has been evidence to give severe side effects
    flagged = models.BooleanField(default=False,null=False)
    
    Issues = models.JSONField()

class Fertilizer_Application_History(models.Model):
    # takes pesticide possesession id and plant_Allocation id
    fertilizer_Id  = models.ForeignKey(Fertilizer_Posession,on_delete=models.CASCADE, null=False,related_name="F_application_hist")
    
    Plant_id = models.ForeignKey(Plant_Allocation,on_delete=models.CASCADE, null=False,related_name="nutrition")
    
    Application_Date = models.DateField(null=False,default=date.today)  
    
    Amount = models.IntegerField(null=False)
    
    Ratio = models.IntegerField(null=False)
 
class Pesticide_Posession(models.Model):
    
    Expenditure_id = models.ForeignKey(Farm_Ependiture,on_delete=models.CASCADE, null=False,related_name="pesticides")
    
    purpose = models.CharField(max_length=50)
    
    Quantity = models.IntegerField(null=False)
    # kgs,ml,litres
    Measurement_Unit = models.CharField(null=False,max_length=10)
    # water to pesticide
    ratio = models.CharField(max_length=20,null=False)
    # how often should it be applied
    redundancy = models.IntegerField(null=False,)
    # 
    application = models.JSONField(null=True)
    
    Expiry_Date = models.DateField(null=False)
    
    # if the pestcide has been evidence to give severe side effects
    flagged = models.BooleanField(null=False,default=False)
    
    Issues = models.JSONField(null=True)

class Pesticide_Application_History(models.Model):
    # takes pesticide possesession id and plant_Allocation id
    pesticide_id  = models.ForeignKey(Pesticide_Posession,on_delete=models.CASCADE, null=False,related_name="P_application_hist")
    
    Plant_id = models.ForeignKey(Plant_Allocation,on_delete=models.CASCADE, null=False,related_name="medication")
    
    Application_Date = models.DateField(null=False,default=date.today)
    # main cause for aplication
    purpose = models.CharField(null=False,max_length=255)   
    # pesticide
    Amount = models.IntegerField(null=False)
    # water to pestcide
    Ratio = models.IntegerField(null=False)
