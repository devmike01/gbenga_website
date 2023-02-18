from django.db import models


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    linked_in_profile = models.CharField(max_length=100)
    github_profile = models.CharField(max_length=50)
    about_me = models.CharField(max_length=1000)
    twitter_profile = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
