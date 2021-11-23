from django.db import models

class Usernames(models.Model):
    username = models.CharField(max_length=100)


class UserDatas(models.Model):
    Pregnancies = models.CharField(max_length=100)
    Glucose = models.CharField(max_length=100)
    Blood_Pressure = models.CharField(max_length=100)
    Skin_Thickness = models.CharField(max_length=100)
    Insulin = models.CharField(max_length=100)
    BMI = models.CharField(max_length=100)
    Diabetes_Pedigree_Function = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Usernames, null=True, on_delete=models.SET_NULL)







