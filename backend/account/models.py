from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class AccountManager(BaseUserManager):

    def create_user(self, email, first_name, last_name="", password=None):
        if not email:
            raise ValueError('Users must have an email address.')

        if not first_name:
            raise ValueError('First name must be provided.')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, first_name, password):
        user = self.create_user(
            email=email,
            first_name=first_name,
            password=password
        )

        user.is_admin = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class Account(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=40)
    last_name = models.CharField(verbose_name='last name', max_length=40, blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self) -> str:
        return self.email

    @property
    def is_superuser(self):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_staff
    

class UserInfo(models.Model):

    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=40)
    last_name = models.CharField(verbose_name='last name', max_length=40, blank=True, null=True)

    def __str__(self):
        return self.email
