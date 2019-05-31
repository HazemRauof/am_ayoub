from django.db import models
from django.forms import ModelForm


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class User(models.Model):
    User_id = models.AutoField(primary_key=True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100,unique=True)
    Password = models.CharField(max_length=20)
    u_type = models.ForeignKey(Role , on_delete=models.CASCADE)
    names_of_books = models.DateField(null=True)
    categories = models.DateField(null=True)
    phone = models.CharField(max_length=14)
    Gender = models.CharField(max_length=10)

class Reader(models.Model):

    u_id = models.ForeignKey(User , on_delete=models.CASCADE)
    preferred_categories = models.CharField(max_length=100)
    preferred_writers = models.CharField(max_length=100)
    Adress = models.CharField(max_length=100)

class SystemAdmin(models.Model):
    system_id=models.AutoField(primary_key=True)
    email=models.EmailField()
    password=models.CharField(max_length=500)



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['First_name','Last_name','Email','Password','phone','Gender']