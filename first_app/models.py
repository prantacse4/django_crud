from django.db import models


# Create your models here.


class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    dept = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)

    def __str__(self):
        return str(self.pk)+" - "+self.name+" "+self.dept
    