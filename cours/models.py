from django.db import models
from pymysql import NULL
from module.models import ElementModule
import datetime
import time
from PIL import Image

from users.models import Teachers

def upload_location(instance, filename):
        filebase, extension = filename.split('.')
        now = time.time()
        stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S')
        return 'img/cours/chapitre_images/%s.%s' % (str(stamp), extension)
    

class Chapitre(models.Model):
    libelle = models.CharField(max_length=40,null = False )
    description = models.CharField(max_length=250,null = True )
    # document = models.ForeignKey(Document , null=True,  on_delete= models.SET_NULL)
    image = models.ImageField(upload_to=upload_location, default='/img/cours/folder-files-and-folders-svgrepo-com.svg')
    element_module = models.ForeignKey(ElementModule , null=True,  on_delete= models.SET_NULL)
    professeur = models.ForeignKey(Teachers,null=False, on_delete= models.CASCADE)
    # enseignant_responsable
    # visibilite
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

class Document(models.Model):
    titre = models.CharField(max_length=40,null = False )
    type = models.CharField(max_length=20,null = False )
    path = models.CharField(max_length=100,null = False )
    image = models.ImageField(upload_to=upload_location, default=NULL)
    chapitre = models.ForeignKey(Chapitre , null=False,  on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

class Modele3D(models.Model):
    path = models.CharField(max_length=100,null = False )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

class Image(models.Model):
    type = models.CharField(max_length=20,null = False )
    path = models.CharField(max_length=100,null = False )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

class Traitement(models.Model):
    titre = models.CharField(max_length=40,null = False )
    label = models.CharField(max_length=100,null = False )
    type = models.CharField(max_length=25,null = False )
    chapitre = models.ForeignKey(Chapitre , null=False,  on_delete= models.CASCADE)
    image = models.ForeignKey(Image , null=True,  on_delete= models.SET_NULL, default=NULL)
    modele3D = models.ForeignKey(Modele3D , null=False,  on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


