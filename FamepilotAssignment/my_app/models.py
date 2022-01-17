from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    mobile_number = models.IntegerField(default=None, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

