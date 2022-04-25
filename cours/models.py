from django.db import models
from pymysql import NULL
from module.models import ElementModule
import datetime
import time
from PIL import Image

from users.models import Professeur

def upload_location(instance, filename):
        filebase, extension = filename.split('.')
        now = time.time()
        stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S')
        return 'img/cours/chapitre_images/%s.%s' % (str(stamp), extension)
  
def document_image_upload_location(instance, filename):
        filebase, extension = filename.split('.')
        now = time.time()
        stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S')
        return 'img/cours/document_images/%s.%s' % (str(stamp), extension)  

def model_location(modelName):
        now = time.time()
        stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S')
        return 'img/cours/modeles_3d/%s-%s' % (modelName, str(stamp))  

def model_image_location(instance, filename):
        filebase, extension = filename.split('.')
        now = time.time()
        stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S')
        return 'img/cours/modeles_3d_images/%s.%s' % (str(stamp), extension)
    
#///
# def file_upload_location(foldername):
#         # now = time.time()
#         # stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S')
#         modele3d = foldername
#         return 'img/cours/%s/' % (modele3d)

# def file_upload_location(instance, filename):
#         # now = time.time()
#         # stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S')
#         modele3d = instance.modele3D.titre
#         return 'img/cours/%s/' % (modele3d)

def file_upload_location(instance, filename):
        # now = time.time()
        # stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S')
        modele3d = instance.modele3D.path
        return '%s/%s' % (modele3d, filename)

# def get_modele_3d(modele_id):
#     modele3d = Modele3D.objects.filter(id = modele_id).first()
#     return modele3d

class Chapitre(models.Model):
    libelle = models.CharField(max_length=40,null = False )
    description = models.CharField(max_length=250,null = True )
    # document = models.ForeignKey(Document , null=True,  on_delete= models.SET_NULL)
    image = models.ImageField(upload_to=upload_location, default='/img/cours/folder-files-and-folders-svgrepo-com.svg')
    element_module = models.ForeignKey(ElementModule , null=True,  on_delete= models.SET_NULL)
    professeur = models.ForeignKey(Professeur,null=False, on_delete= models.CASCADE)
    # enseignant_responsable
    # visibilite
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

class Document(models.Model):
    titre = models.CharField(max_length=40,null = False )
    type = models.CharField(max_length=20,null = False )
    path = models.CharField(max_length=100,null = False )
    image = models.ImageField(upload_to=document_image_upload_location, default=NULL)
    chapitre = models.ForeignKey(Chapitre , null=False,  on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

class Modele3D(models.Model):
    titre = models.CharField(max_length=40,null = False )
    path = models.CharField(max_length=100,null = False, default=model_location(titre) )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

# IMAGE_TYPES = ['image', 'qrcode']
class Image(models.Model):
    name = models.CharField(max_length=30,null = False, default='Sans Nom' )
    # type = models.CharField(max_length=10,null = False, default=IMAGE_TYPES[0] )
    is_qrcode = models.BooleanField(default=False)
    # path = models.CharField(max_length=100,null = False )
    path = models.FileField(upload_to=model_image_location,null = False )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

class Traitement(models.Model):
    titre = models.CharField(max_length=40,null = False )
    label = models.CharField(max_length=100,null = True )
    type = models.CharField(max_length=25,null = False )
    chapitre = models.ForeignKey(Chapitre , null=False,  on_delete= models.CASCADE)
    image = models.ForeignKey(Image , null=True,  on_delete= models.SET_NULL, default=NULL)
    modele3D = models.ForeignKey(Modele3D , null=False,  on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

class File(models.Model):
    # path = models.CharField(max_length=100,null = False )
    path = models.FileField(upload_to=file_upload_location,null = False )
    modele3D = models.ForeignKey(Modele3D , null=False,  on_delete= models.CASCADE)
    # file = models.FileField(upload_to=file_upload_location(foldername=get_modele_3d(modele3D)),null = False )
    # file = models.FileField(null = False )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)







