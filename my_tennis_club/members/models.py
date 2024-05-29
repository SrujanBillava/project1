from django.db import models # type: ignore

# Create your models here.
class Member(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=100)
    phone=models.IntegerField(null=True)
    joined_date=models.DateField(null=True)
    def __str__(self):
        return self.name

    
    