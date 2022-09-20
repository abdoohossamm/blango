from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy
from django.contrib.auth.hashers import make_password
# Create your models here.

class BlangoUserManager(UserManager):
  def _create_user(self, email, password, **extra_fields):
    if not email:
        raise ValueError('The given email must be set')
    email = self.normalize_email(email)

    user = self.model(email=email, **extra_fields)
    user.password = make_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email=None, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, password, **extra_fields)

  def create_superuser(self,email=None, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
        raise ValueError('Superuser must have is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
        raise ValueError('Superuser must have is_superuser=True.')

class User(AbstractUser):
  username = None
  email = models.EmailField(
      gettext_lazy("email address"),
      unique=True,
  )

  objects = BlangoUserManager()

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = []

  def __str__(self):
      return self.email