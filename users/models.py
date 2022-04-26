from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.core.validators import RegexValidator
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save


class SessionYearModel(models.Model):
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    objects = models.Manager()


class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"), (2, "Teacher"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Teachers(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Students(models.Model):
    cne = models.CharField(max_length=10, default="")
    adresse = models.CharField(max_length=100, default="")
    path_photos = models.CharField(max_length=200, default="")
    telephone = models.CharField(max_length=10, default="")
    code_apogee = models.CharField(max_length=10, default="")
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


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
            Teachers.objects.create(admin=instance)
        if instance.user_type == 3:
            Students.objects.create(admin=instance,
                                    # course_id=
                                    session_year_id=SessionYearModel.objects.get(id=1),
                                    address="",
                                    profile_pic="",
                                    gender="")


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.teachers.save()
    if instance.user_type == 3:
        instance.students.save()

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


# ---------------------------

class Permission(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle


class Role(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ManyToManyField(CustomUser)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.libelle
