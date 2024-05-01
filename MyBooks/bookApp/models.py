from django.db import models
from django.core.validators import RegexValidator
from datetime import date

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return str(self.name)

class Authors(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    auth = models.ForeignKey("self", on_delete=models.CASCADE)
    follower = models.ForeignKey(Users,on_delete=models.CASCADE)

class Publishers(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    join_date = models.DateField(default=date.today)
    popularity_score = models.DecimalField(decimal_places=3 ,max_digits=10)
    publisher = models.ForeignKey("self", on_delete=models.CASCADE)

class Books(models.Model):
    author = models.OneToOneField(Authors,
        on_delete=models.PROTECT,
        blank=False)
    
    publisher = models.ForeignKey(Publishers,on_delete=models.PROTECT,
        blank=False)

    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=3,max_digits=12)
    publshed_date = models.DateField(default=date.today)




    