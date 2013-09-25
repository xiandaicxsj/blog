from django.db import models
class blog_post(models.Model):
		title=models.CharField(max_length=30)
		text=models.TextField()

		
# Create your models here.
