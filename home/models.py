from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    contact = models.CharField(max_length=10)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    

   

    

    