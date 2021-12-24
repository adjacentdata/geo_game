from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class Account(AbstractBaseUser):
    user_name = models.CharField(max_length=25, unique=True)
    first_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50, unique=True)

    sign_up_date = models.DateTimeField(auto_now_add=True)
    last_signin = models.DateTimeField(auto_now_add=True)
    user_admin = models.BooleanField(default=False)
    user_active = models.BooleanField(default=False)
    user_superadmin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['user_name', 'first_name', 'email']

    def __str__(self):
        return self.email

    def has_perm (self, perm):
        return self.user_admin

class AccountManager(BaseUserManager):
    def create_player(self, first_name, username, email,password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have a username")
        player = self.model(
            email = self.normalize_email(email),
            username=username,
            first_name = first_name
        )

        player.set_password(password)
        player.save(using=self._db)
        return player
