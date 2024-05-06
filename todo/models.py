from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tododata(models.Model):
    LIVE=0
    COMPLETE=1
    COMPLETE_CHOICE=((LIVE,'Live'),(COMPLETE,'Complete'))
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    tododata=models.CharField(max_length=500)
    status=models.IntegerField(choices=COMPLETE_CHOICE,default=LIVE)
    def __str__(self) -> str:
        return self.tododata
