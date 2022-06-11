from django import template
import markdown
from django.utils.safestring import mark_safe
import os, cv2

from users.models import Professeur

register = template.Library()

# tags
@register.simple_tag
def connected_prof_id(user):
    prof = Professeur.objects.get(user_id=user.id)
    if prof:    
        return prof.id

# template filter
@register.filter(name='presence_filter')
def presenceFilter(presence):
    if presence == 1:
        str = '<span class="badge badge-pill badge-success center"> Présent(e)</span>'
    
    if presence == 0:
        str = '<span class="badge badge-pill badge-danger center"> Absent(e)</span>'
    
    return mark_safe(markdown.markdown(str))


@register.filter(name='photo_filter')
def photoFilter(profile_picture):
    if profile_picture :
        str =f'<img class="rounded-circle " width="50px" src="/media/{profile_picture}" />'
    
    else:
        str = '<img class="rounded-circle " width="50px" src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png" />'
    
    return mark_safe(markdown.markdown(str))


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

@register.simple_tag
def show_images(filiere="IRISI", niveau="IRISI_1", groupe="G1", idSeance=1):
    path = filiere + "/" + niveau + "/" + groupe + "/" + str(idSeance) + "/"
    path_dir = "face_recognition/service_metier/backup/" + path
    
    list_images = os.listdir(path_dir)
    
    images = []
    for i in range(len(list_images)):
        imagePath = path + list_images[i]
        print(imagePath)
        images += [imagePath]
    return {'images': images}

