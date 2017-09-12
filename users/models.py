from django.db import models

# Create your models here.
class MyUsers(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    myEmail = models.CharField(max_length=30)

    def __str__(self):
        return self.fname + " " + self.lname + " " + self.myEmail
