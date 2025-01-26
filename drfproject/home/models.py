from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.CharField( max_length=100)

    def __str__(self):
        return self.team_name
    
class Person(models.Model):
    team =models.ForeignKey(Team,blank=True,null=True, on_delete=models.CASCADE,related_name ="members",default=None)
    name = models.CharField(max_length=100)
    age  = models.IntegerField()
    designation = models.CharField(max_length=100)

    

