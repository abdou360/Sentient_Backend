from django.shortcuts import redirect, render
from semestre.forms.niveau.forms import NiveauForm

from semestre.models import Niveau

# Create your views here.


def niveau_list(request):
    context = {'niveau_list': Niveau.objects.all()}
    return render(request, "semestre/niveau/niveau_list.html", context)


def niveau_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = NiveauForm()
        else:
            niveau = Niveau.objects.get(pk=id)
            form = NiveauForm(instance=niveau)
        return render(request, "semestre/niveau/niveau_form.html", {'form': form})
    else:
        if id == 0:
            form = NiveauForm(request.POST)
        else:
            niveau = Niveau.objects.get(pk=id)
            form = NiveauForm(request.POST,instance= niveau)
        if form.is_valid():
            form.save()
        return redirect('/niveau/list')


def niveau_delete(request,id):
    niveau = Niveau.objects.get(pk=id)
    niveau.delete()
    return redirect('/niveau/list')
