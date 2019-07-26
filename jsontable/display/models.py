from django.db import models

class data(models.Model):
    order_no=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    booking_datetime=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    amount=models.IntegerField()
    no_of_people=models.IntegerField()

