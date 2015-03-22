from django.db import models

class InputFile(models.Model):
	input = models.FileField(upload_to='input/%Y/%m/%d')
	next_one = models.FileField(upload_to='documents/%Y/%m/%d')
	name=models.CharField(max_length=100)
	privacy=models.BooleanField(default=False)
