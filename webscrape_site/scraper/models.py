from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Headlines(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=500,unique=True)
    url = models.URLField(max_length=2000)
    # image = models.ImageField("")
    scraped_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title