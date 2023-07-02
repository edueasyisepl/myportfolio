from django.db import models

# Create your models here.
class message(models.Model):
    First_Name = models.CharField(max_length=40)
    Last_Name = models.CharField(max_length=40)
    Email_Address = models.EmailField(max_length=255)
    Message = models.TextField()

    def __str__(self):
        return self.First_Name
    