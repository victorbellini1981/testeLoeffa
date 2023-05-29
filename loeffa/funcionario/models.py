from django.db import models

# Create your models here.
class Funcionario(models.Model):  
    eid = models.CharField(max_length=20)  
    enome = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtato = models.CharField(max_length=15)  
    class Meta:  
        db_table = "funcionario"  
