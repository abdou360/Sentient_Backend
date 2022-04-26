from django import forms

from users.models import Permission

DEMO_CHOICES = (
    ("1", "Naveen"),
    ("2", "Pranav"),
    ("3", "Isha"),
    ("4", "Saloni"),
)


def get_demo_choices():
    permissions = Permission.objects.all()
    list_permissions = []
    for permission in permissions:
        list_permissions.append((permission.id, permission.libelle))
    return list_permissions


class GeeksForm(forms.Form):
    geeks_field = forms.MultipleChoiceField(choices=get_demo_choices)