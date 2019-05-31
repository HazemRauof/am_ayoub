from django.db import models
from reader.models import User

class Writer(models.Model):
    bio=models.TextField(max_length=1000)
    Writer=models.ForeignKey(User,on_delete=models.CASCADE)

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    Writer_id=models.ForeignKey(Writer,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=1000)






