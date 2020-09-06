from django.db import models


class Register(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_no = models.IntegerField()
    password = models.CharField(max_length= 15)
