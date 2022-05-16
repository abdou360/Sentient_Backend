from django.db import models
from django.contrib.auth.models import AbstractUser
# from PIL import Image
from django.core.validators import RegexValidator
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save


class SessionYearModel(models.Model):
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    objects = models.Manager()


# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"), (2, "Professeur"), (3, "Etudiant"))
    user_type = models.CharField(
        default=1, choices=user_type_data, max_length=10)


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.admin.username


class Professeur(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    specialite = models.CharField(max_length=45, default="informatique")
    matricule = models.CharField(max_length=45, default="")
    telephone = models.CharField(max_length=10, default="")
    objects = models.Manager()

# UnivIt responsable : ismail errouk


class Students(models.Model):
    cne = models.CharField(max_length=100, default="")
    adresse = models.CharField(max_length=100, default="")
    path_photos = models.CharField(max_length=200, default="")
    telephone = models.CharField(max_length=100, default="")
    code_apogee = models.CharField(max_length=100, default="")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    profile_pic = models.FileField(null=True)
    groupes = models.ManyToManyField('semestre.Groupe', null=True)


# Creating Django Signals

# It's like trigger in database. It will run only when Data is Added in CustomUser model

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in Admin, Teacher or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            Admin.objects.create(admin=instance)
        if instance.user_type == 2:
            Professeur.objects.create(admin=instance)
        if instance.user_type == 3:
            Students.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.teachers.save()
    if instance.user_type == 3:
        instance.students.save()

# ---------------------------
# UnivIt responsable : ismail errouk


class Permission(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle

# UnivIt responsable : ismail errouk


class Role(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ManyToManyField(CustomUser)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.libelle
