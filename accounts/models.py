from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, first_name, username, email,password=None):
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

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name
        )

        user.is_admin = True
        user.is_superadmin = True
        user.is_staff=True
        user.is_active=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    username = models.CharField(max_length=25, unique=True)
    first_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50, unique=True)

    sign_up_date = models.DateTimeField(auto_now_add=True)
    last_signin = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['first_name', 'email']
    USERNAME_FIELD = 'username'

    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm (self, perm):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
