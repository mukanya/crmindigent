from django.db import models
from django.db.models.signals import post_save , pre_save
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
  
class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    id_number = models.CharField(max_length=13, default=0)
    physical_address = models.CharField(max_length=50, default=0)
    postal_address = models.CharField(max_length=50, default=0)
    sex = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=30, choices=sex)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Category(models.Model):
    name = models.CharField(max_length=30)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance , created)
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender= User)


class Book(models.Model):
    name = models.CharField(max_length=30)
    surname= models.CharField(max_length=30)
    bank_statement = models.FileField(upload_to='supporting_docs/bank_statement/')
    id_copy = models.FileField(upload_to='supporting_docs/id_copy/')
    proof_residence = models.FileField(upload_to='supporting_docs/proof_residence/')
    water_proof = models.FileField(upload_to='supporting_docs/water_proof/')
    electricity_proof = models.FileField(upload_to='supporting_docs/electricty_proof/')
    sworn_affidavit = models.FileField(upload_to='supporting_docs/sworn_affidavit/') 

    def __str__(self):
        return self.name
