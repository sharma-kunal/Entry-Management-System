from django.db import models

# Create your models here.


class Data(models.Model):
    visitor_name = models.TextField()
    visitor_number = models.TextField()
    visitor_email = models.EmailField()
    curr_time = models.TextField()
    host_name = models.TextField()
    host_number = models.TextField()
    host_email = models.EmailField()