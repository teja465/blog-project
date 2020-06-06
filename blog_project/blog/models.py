from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class blog_model(models.Model):
    status_choices=(('draft','draft'),('published','published'))
    title=models.CharField(max_length=200)
    #author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='bp')
    author=models.CharField(max_length=15)
    post=models.TextField()
    publish_date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=15,choices=status_choices)

    def __str__(self):
        return self.title
#  hero  someone  raviteja reddy  ravi@2020
