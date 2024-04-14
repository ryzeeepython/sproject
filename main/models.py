from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserAccount(models.Model): 
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    is_done_test = models.BooleanField(null = True)
    test_mark = models.IntegerField(null = True) 
    unique_code = models.CharField(max_length = 21, null = True, unique = True)
