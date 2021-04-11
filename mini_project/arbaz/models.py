from django.db import models

# Create your models here.
class Image(models.Model):
	#name=models.CharField(max_length=200)
	input_loc=models.CharField(max_length=500,default="none")
	output_loc=models.CharField(max_length=500,default="none")

