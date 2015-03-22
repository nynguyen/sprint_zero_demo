from django.db import models

class InputFile(models.Model):
	input = models.FileField(upload_to='input/%Y/%m/%d')
