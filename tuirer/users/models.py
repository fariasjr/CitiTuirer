from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    picture = models.ImageField('Fotode perfil', default='/img/blank-pic.png')
    following = models.ManyToManyField('self', blank=True)