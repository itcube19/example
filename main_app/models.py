from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser,PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, verbose_name='Login')
    lastname = models.CharField(max_length=255, unique=True, verbose_name='Фамилия')
    firstname = models.CharField(max_length=255, unique=True, verbose_name='Имя')
    email = models.EmailField(unique=True, verbose_name='Email')
    password = models.CharField(max_length=128)
    rating = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, default=timezone.now)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['lastname', 'firstname', 'password', 'rating']
    # add additional fields in here

    def __str__(self):
        return self.username

# Create your models here.
class Problem(models.Model):
    problem = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    type_problem = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.problem


class Training(models.Model):
    problem = models.ForeignKey("Problem", on_delete=models.PROTECT)
    username = models.ForeignKey("CustomUser", on_delete=models.PROTECT)
    date = models.DateField(auto_now=True)
    user_answer = models.CharField(max_length=100)
