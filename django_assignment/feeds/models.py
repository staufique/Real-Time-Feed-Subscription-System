from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)
    
class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email', null=False)
    password = models.CharField(max_length=100, null=False)
    channel_subscription = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    
    objects = CustomUserManager()

    def __str__(self):
        return self.username
