from datetime import datetime, date
from modulefinder import Module
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from module.models import *
from semestre.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def add_module(request):
    semestres = Semestre.objects.all()
    return render(request, "modules/add_module_template_no_tree.html", {"semestres": semestres})
@login_required
def add_module_level(request,name_):
    niveau = Niveau.objects.get(nom_niveau=name_)
    semestres = Semestre.objects.filter(niveau=niveau)
    
    return render(request, "modules/add_module_template.html", {"semestres": semestres , "filiere" : niveau.filiere , "niveau" : niveau})


@login_required
def add_module_save(request):
    if request.method != "POST":
        return HttpResponse("<h2> Get or whatever method is not allowed here </h2>")
    else:
        module_libelle = request.POST.get("module")
        semestre_id = request.POST.get("semestre_id")
        semestre = Semestre.objects.get(id=semestre_id)
        try:
            course = Module.objects.create(
                libelle_module=module_libelle, semestre=semestre)
            course.save()
            messages.success(request, "Le module est ajouté avec succès !")
            return HttpResponseRedirect(reverse(add_module_level,  kwargs={'name_':semestre.niveau.nom_niveau}))

        except:
            messages.error(request, "Echec d'ajout du module !")
            return HttpResponseRedirect(reverse(add_module_level))


@login_required
def add_element_module_level(request,name_):
    niveau = Niveau.objects.get(nom_niveau=name_)
    semestre = Semestre.objects.filter(niveau=niveau) 
    modules = Module.objects.filter(semestre__in=semestre)
    profs = Professeur.objects.all()
    prerequis = ElementModule.objects.all()
    
    if modules.exists() :
        return render(request, "modules/add_elem_module_template.html", {"profs": profs, "modules": modules, "element_modules": prerequis,"niveau": niveau,"filiere":niveau.filiere})
    else :
        messages.error(request, "Ajoutez au moins un module ")
        return render(request, "modules/add_elem_module_template.html", {"profs": profs, "modules": modules, "element_modules": prerequis,"niveau": niveau,"filiere":niveau.filiere})
        
        
     


@login_required
def add_element_module_save(request):
    if request.method != "POST":
        return HttpResponse("<h2> Get or whatever method is not allowed here </h2>")
    else:
        libelle_element_module = request.POST.get("libelle_element_module")
        module_id = request.POST.get("module_id")
        prerequis_id = request.POST.getlist("prerequis_id")
        volumeHoraire = request.POST.get("volumeHoraire")
        objectif = request.POST.get("objectif")
        prof_id = request.POST.getlist("prof")
        module = Module.objects.get(id=module_id)
        responsable = request.POST.get("responsable")
        niveau = request.POST.get("niveau")
        try:

            respo = Professeur.objects.get(id=responsable)
            element_module = ElementModule.objects.create(libelle_element_module=libelle_element_module, volumeHoraire=volumeHoraire,
                                                          objectif=objectif,
                                                          module=module, responsable=respo)

            for pr in prof_id:
                prof = Professeur.objects.get(id=pr)
                element_module.prof_id.add(prof)
                element_module.save()
         
            for preq in prerequis_id:
                preqd = ElementModule.objects.get(id=int(preq))
                d = Perequis.objects.create(
                    element_module_id=element_module, prerequis_id=preqd)
                d.save()

            messages.success(
                request, "L'élément de module est ajouté avec succès !")
            return HttpResponseRedirect(reverse(add_element_module_level,  kwargs={'name_':niveau}))

        except:

            messages.error(
                request, "Echec au niveau d'ajout de l'element de module ! ")
            return HttpResponseRedirect(reverse(add_element_module_level,  kwargs={'name_':niveau}))


@login_required
def edit_element_module_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method is Not Allowed</h2>")
    else:
        libelle_element_module = request.POST.get("libelle_element_module")
        module_id = request.POST.get("module_id")
        element_id = request.POST.get("element_id")
        prerequis_id = request.POST.getList("prerequis_id")
        volumeHoraire = request.POST.get("volumeHoraire")
        objectif = request.POST.get("objectif")
        prof_id = request.POST.get("prof")

        try:
            module = Module.objects.get(id=module_id)
            prerequis = ElementModule.objects.get(id=prerequis_id)
            prof = Professeur.objects.get(id=prof_id)
            element_module = ElementModule.objects.get(id=element_id)

            element_module.libelle_element_module = libelle_element_module
            element_module.volumeHoraire = volumeHoraire
            element_module.objectif = objectif
            element_module.module_id = module
            element_module.prof_id = prof

            prerequis_ = Perequis.objects.get(id=prerequis)
            prerequis_.element_module_id = element_module
            prerequis_.prerequis_id = prerequis
            element_module.save()
            prerequis_.save()

            messages.success(
                request, "L'élément de module est modifié avec succès")
            return HttpResponse(reverse("edit_module", kwargs={"element_id": element_id}))
        except:
            messages.error(
                request, "Echec au niveau de modifier l'element de module ! ")
            return HttpResponseRedirect(reverse(add_element_module))


@login_required
def edit_module_save(request):
    if request.method != "POST":
        return HttpResponse("<h2> Get or whatever method is not allowed here </h2>")
    else:
        module_libelle = request.POST.get("module")
        semestre_id = request.POST.get("semestre_id")
        module_id = request.POST.get("module_id")
        semestre = Semestre.objects.get(id=semestre_id)
        try:
            course = Module.objects.get(id=module_id)
            course.libelle_module = module_libelle
            course.semestre = semestre
            course.save()
            messages.success(request, "Le module est modifié avec succès !")
            return HttpResponseRedirect(reverse(manage_modules))

        except:
            messages.error(request, "Echec de la modification !")
            return HttpResponseRedirect(reverse(manage_modules))


@login_required
def manage_modules(request):
    modules = Module.objects.all().order_by('-created_at')
    semestres = Semestre.objects.filter(id=4444)
    niveaux = Niveau.objects.filter(id=4444)
    filieres = Filiere.objects.all()
    
    page = request.GET.get('page', 1)

    paginator = Paginator(modules, 5)
    try:
        modules_ = paginator.page(page)
    except PageNotAnInteger:
        modules_ = paginator.page(1)
    except EmptyPage:
        modules_ = paginator.page(paginator.num_pages)

    return render(request, "modules/manage_modules.html", {"modules": modules_,"filieres":filieres,"semestres":semestres,"niveaux":niveaux})


def search_module(request):
    query = request.GET.get('q')
    modules = Module.objects.filter(libelle_module__icontains=query).order_by('-created_at')
    semestres = Semestre.objects.filter(id=4444)
    niveaux = Niveau.objects.filter(id=4444)
    filieres = Filiere.objects.all()
    
    page = request.GET.get('page', 1)

    paginator = Paginator(modules, 5)
    try:
        modules_ = paginator.page(page)
    except PageNotAnInteger:
        modules_ = paginator.page(1)
    except EmptyPage:
        modules_ = paginator.page(paginator.num_pages)

    return render(request, "modules/manage_modules.html", {"modules": modules_,"filieres":filieres,"semestres":semestres,"niveaux":niveaux})


@login_required
def search_modules_semestres(request,name_):
       
    semestres = Semestre.objects.filter(libelle_semestre=name_)
    semestres_ = Semestre.objects.values('libelle_semestre').distinct()
    modules = Module.objects.filter(semestre__in=semestres)
    niveaux = Niveau.objects.all()
    filieres = Filiere.objects.all()
    
    page = request.GET.get('page', 1)

    paginator = Paginator(modules, 5)
    try:
        modules_ = paginator.page(page)
    except PageNotAnInteger:
        modules_ = paginator.page(1)
    except EmptyPage:
        modules_ = paginator.page(paginator.num_pages)

    return render(request, "modules/manage_modules.html", {"modules": modules_,"filieres":filieres,"semestres":semestres_,"niveaux":niveaux})

@login_required
def search_modules_filiere(request,name_):
       
    filiere = Filiere.objects.get(nom_filiere=name_)
    filieres = Filiere.objects.all()
    niveaux = Niveau.objects.filter(filiere=filiere)
    semestres = Semestre.objects.filter(niveau__in=niveaux)
    modules = Module.objects.filter(semestre__in=semestres)
    
    
    page = request.GET.get('page', 1)

    paginator = Paginator(modules, 5)
    try:
        modules_ = paginator.page(page)
    except PageNotAnInteger:
        modules_ = paginator.page(1)
    except EmptyPage:
        modules_ = paginator.page(paginator.num_pages)

    return render(request, "modules/manage_modules.html", {"modules": modules_,"filieres":filieres,"semestres":semestres,"niveaux":niveaux})

@login_required
def search_modules_niveau(request,name_):
       
    
    filieres = Filiere.objects.all()
    niveaux = Niveau.objects.all()
    niveau = Niveau.objects.filter(nom_niveau=name_)
    semestres = Semestre.objects.filter(niveau__in=niveau)
    modules = Module.objects.filter(semestre__in=semestres)
    
    
    page = request.GET.get('page', 1)

    paginator = Paginator(modules, 5)
    try:
        modules_ = paginator.page(page)
    except PageNotAnInteger:
        modules_ = paginator.page(1)
    except EmptyPage:
        modules_ = paginator.page(paginator.num_pages)

    return render(request, "modules/manage_modules.html", {"modules": modules_,"filieres":filieres,"semestres":semestres,"niveaux":niveaux})


@login_required
def search_elem_modules_filiere(request,name_): 
    filiere = Filiere.objects.get(nom_filiere=name_)
    niveaux = Niveau.objects.filter(filiere=filiere)
    semestres = Semestre.objects.filter(niveau__in=niveaux)
    modules = Module.objects.filter(semestre__in=semestres)
    filieres = Filiere.objects.all()
    elem_modules = ElementModule.objects.filter(module__in=modules).order_by('-created_at')
    prerequis = Perequis.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(elem_modules, 5)
    try:
        elem_modules_ = paginator.page(page)
    except PageNotAnInteger:
        elem_modules_ = paginator.page(1)
    except EmptyPage:
        elem_modules_ = paginator.page(paginator.num_pages)
    
    return render(request, "modules/manage_elem_modules.html", {"elem_modules": elem_modules_,"prerequis":prerequis , "filieres":filieres,"semestres":semestres,"niveaux":niveaux,"modules":modules})

@login_required
def search_elem_modules_niveau(request,name_): 
    filieres = Filiere.objects.all()
    niveaux = Niveau.objects.all()
    niveau = Niveau.objects.filter(nom_niveau=name_)
    semestres = Semestre.objects.filter(niveau__in=niveau)
    modules = Module.objects.filter(semestre__in=semestres)
    filieres = Filiere.objects.all()
    elem_modules = ElementModule.objects.filter(module__in=modules).order_by('-created_at')
    prerequis = Perequis.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(elem_modules, 5)
    try:
        elem_modules_ = paginator.page(page)
    except PageNotAnInteger:
        elem_modules_ = paginator.page(1)
    except EmptyPage:
        elem_modules_ = paginator.page(paginator.num_pages)
    
    return render(request, "modules/manage_elem_modules.html", {"elem_modules": elem_modules_,"prerequis":prerequis , "filieres":filieres,"semestres":semestres,"niveaux":niveaux,"modules":modules})


@login_required
def search_elem_modules_semestres(request,name_): 
    semestres = Semestre.objects.filter(libelle_semestre=name_)
    semestres_ = Semestre.objects.values('libelle_semestre').distinct()
    modules = Module.objects.filter(semestre__in=semestres)
    niveaux = Niveau.objects.all()
    filieres = Filiere.objects.all()
    elem_modules = ElementModule.objects.filter(module__in=modules).order_by('-created_at')
    prerequis = Perequis.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(elem_modules, 5)
    try:
        elem_modules_ = paginator.page(page)
    except PageNotAnInteger:
        elem_modules_ = paginator.page(1)
    except EmptyPage:
        elem_modules_ = paginator.page(paginator.num_pages)
    
    return render(request, "modules/manage_elem_modules.html", {"elem_modules": elem_modules_,"prerequis":prerequis , "filieres":filieres,"semestres":semestres_,"niveaux":niveaux,"modules":modules})


@login_required
def search_elem_modules_modules(request,name_): 
    semestres = Semestre.objects.values('libelle_semestre').distinct()
    modules = Module.objects.filter(libelle_module=name_)
    modules_ = Module.objects.all()
    niveaux = Niveau.objects.all()
    filieres = Filiere.objects.all()
    elem_modules = ElementModule.objects.filter(module__in=modules).order_by('-created_at')
    prerequis = Perequis.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(elem_modules, 5)
    try:
        elem_modules_ = paginator.page(page)
    except PageNotAnInteger:
        elem_modules_ = paginator.page(1)
    except EmptyPage:
        elem_modules_ = paginator.page(paginator.num_pages)
    
    return render(request, "modules/manage_elem_modules.html", {"elem_modules": elem_modules_,"prerequis":prerequis , "filieres":filieres,"semestres":semestres,"niveaux":niveaux,"modules":modules_})


@login_required
def search_elem_module(request): 
    semestres = Semestre.objects.filter(id=4444)
    niveaux = Niveau.objects.filter(id=4444)
    filieres = Filiere.objects.all()
    query = request.GET.get('q')
    elem_modules = ElementModule.objects.filter(libelle_element_module__icontains=query).order_by('-created_at')
    prerequis = Perequis.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(elem_modules, 5)
    try:
        elem_modules_ = paginator.page(page)
    except PageNotAnInteger:
        elem_modules_ = paginator.page(1)
    except EmptyPage:
        elem_modules_ = paginator.page(paginator.num_pages)
    
    return render(request, "modules/manage_elem_modules.html", {"elem_modules": elem_modules_,"prerequis":prerequis , "filieres":filieres,"semestres":semestres,"niveaux":niveaux})


@login_required
def manage_elem_modules(request): 
    semestres = Semestre.objects.filter(id=4444)
    niveaux = Niveau.objects.filter(id=4444)
    modules = Module.objects.filter(id=4444)
    filieres = Filiere.objects.all()
    elem_modules = ElementModule.objects.all()
    prerequis = Perequis.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(elem_modules, 5)
    try:
        elem_modules_ = paginator.page(page)
    except PageNotAnInteger:
        elem_modules_ = paginator.page(1)
    except EmptyPage:
        elem_modules_ = paginator.page(paginator.num_pages)
    
    return render(request, "modules/manage_elem_modules.html", {"elem_modules": elem_modules_,"prerequis":prerequis , "filieres":filieres,"semestres":semestres,"niveaux":niveaux ,"modules":modules})


@login_required
def delete_module(request, id_):
    try:
        Module.objects.filter(id=id_).delete()
        messages.success(request, "Le module est supprimé avec succès !")
        return HttpResponseRedirect(reverse(manage_modules))
    except:
        messages.error(request, "Echec de la suppression !")
        return HttpResponseRedirect(reverse(manage_modules))


@login_required
def delete_elem_module(request, id_):
    try:
        ElementModule.objects.filter(id=id_).delete()
        messages.success(request, "Le module est supprimé avec succès !")
        return HttpResponseRedirect(reverse(manage_elem_modules))

    except:
        messages.error(request, "Echec de la suppression !")
        return HttpResponseRedirect(reverse(manage_modules))


@login_required
def edit_module(request, name_,id_):
    
    module = Module.objects.get(id=id_)
    niveau = Niveau.objects.get(nom_niveau=name_)
    semestres = Semestre.objects.filter(niveau=niveau)
    # return HttpResponse(niveau.filiere)
    return render(request, "modules/edit_module_template.html", {"module":module,"semestres": semestres , "filiere" : niveau.filiere , "niveau" : niveau})




@login_required
def display_majors(request):
    filieres = Filiere.objects.all()

    return render(request, "modules/filieres_template.html", {"filieres": filieres})

@login_required
def display_levels(request,name_):
    filiere = Filiere.objects.get(nom_filiere=name_)
    niveaux = Niveau.objects.filter(filiere=filiere)

    return render(request, "modules/niveau_template.html", {"filiere": filiere , "niveaux" : niveaux})

