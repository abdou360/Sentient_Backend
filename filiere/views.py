# {% extends "admin/base-home.html" %}
# {% load static %}{% block title %} Filieres
# {% endblock %}

# <!-- importation des fichier css  -->
# {% block stylesheets %}
# <link href="{% static 'css/filiere.css' %}" rel="stylesheet" />
# <style>
#   .form-select {
#   display: block;
#   width: 100%;
#   padding: 0.375rem 2.25rem 0.375rem 0.75rem;
#   -moz-padding-start: calc(0.75rem - 3px);
#   font-size: 1rem;
#   font-weight: 400;
#   line-height: 1.5;
#   color: #495057;
#   background-color: #fff;
#   background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%23343a40' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M2 5l6 6 6-6'/%3e%3c/svg%3e");
#   background-repeat: no-repeat;
#   background-position: right 0.75rem center;
#   background-size: 16px 12px;
#   border: 1px solid #ced4da;
#   border-radius: 0.25rem;
#   transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
#   -webkit-appearance: none;
#   -moz-appearance: none;
#   appearance: none;
# }
# </style>
# {% endblock stylesheets %} {% block content %}
# <div class="col-md-12">
#   <div class="card">
#     <div class="card-header card-header-primary card-header-flex">
#       <div class="card-header">
#         <h4 class="card-title">Table des etablissements</h4>
#         <p class="card-category">La liste des etablissements </p>
#       </div>

#       {% comment %} form pour le rechereche du filiere {% endcomment %}
#       <form
#         class="navbar-form col-md-5 adapter"
#         method="POST"
#         action="/filiere_etab/etablissement/search"
#       >
#         {% csrf_token %}
#         <div class="input-group no-border">
#           <input
#             type="text"
#             value=""
#             name="text"
#             class="form-control"
#             placeholder="Recherche..."
#           />
#           <button type="submit" class="btn btn-primary btn-round btn-just-icon">
#             <i class="fas fa-fw fa-search"></i>
#             <div class="ripple-container"></div>
#           </button>
#         </div>
#       </form>
#     </div>

#     {% comment %} affichage de la liste des differentes filiere {% endcomment %}
#     <div class="card-body">
#       <div class="table-responsive">
#         {% if data is None or data.count == 0 %}
#         <h3 class="col-md-12" style="color: red">aucune donnée trouvée !</h3>
#         {% else %}

#         <table class="table">
#           <thead class="text-primary">
#             <th class="col-md-1">ID</th>
#             <th class="col-md-2">Nom</th>
#             <th class="col-md-2">Adresse</th>
#             <th class="col-md-1">Telephone</th>
#             <th class="col-md-1">Niveau</th>
#             <th class="col-md-1">Site web</th>
#             <th class="col-md-1">Email</th>
#             <th class="col-md-1">LOGO</th>
#             <th class="col-md-1">Modifier</th>
#             <th class="col-md-1">Supprimer</th>
#           </thead>
#           <tbody>
#             <tr></tr>
#             {% for dt in data %}
#             <tr>
#               <td id="ide">{{dt.id}}</td>
#               <td id="nom">{{dt.nom}}</td>
#               <td id="adresse">{{dt.adresse}}</td>
#               <td id="telephone">{{dt.telephone}}</td>
#               <td id="niveau">{{dt.niveau}}</td>
#               <td id="website">{{dt.website}}</td>
#               <td id="email">{{dt.email}}</td>
#               <td class="image">
#                 {% if dt.logo %}
#               <img style="width: 60px;height: 46px;border-radius: 3px;" src="{{dt.logo.url}}" alt="" srcset="" />
#              {% else %}
#             <img style="width: 60px;height: 46px;border-radius: 3px;" src="{% static 'img/default.png' %}" />
#             {% endif %}

#               </td>
#               <td>
#                 {% comment %} modification de la filiere {% endcomment %}
#                 <div
#                 class="edit"
#                   data-toggle="modal"
#                   data-target="#eModal"
#                   style="color: blue; cursor: pointer"
#                 >
#                   <i class="fas fa-edit"></i>
#                 </div>
#               </td>
#               <td>
#                 {% comment %} supprission du filiere {% endcomment %}
#                 <a
#                   href="/filiere_etab/etablissement/delete/{{dt.id}}"
#                   class="delete"
#                   data-toggle="modal"
#                   data-target="#deleteModal"
#                   style="color: red"
#                   ><i class="fas fa-trash-alt"></i
#                 ></a>
#               </td>
#             </tr>
#             {% endfor %}
#           </tbody>
#         </table>
#         {% endif %}
#       </div>
#     </div>
#     <div class="card-header card-add">
#       <button
#         class="btn btn-primary"
#         data-toggle="modal"
#         data-target="#cModal"
#       >
#         Ajouter
#       </button>
#     </div>
#   </div>
# </div>

# <!-- Modal pour la confirmation de supprission  -->
# <div
#   class="modal fade"
#   id="deleteModal"
#   tabindex="-1"
#   role="dialog"
#   aria-labelledby="exampleModalLabel"
#   aria-hidden="true"
# >
#   <div class="modal-dialog" role="document">
#     <div class="modal-content">
#       <div class="modal-header">
#         <h5 class="modal-title" id="exampleModalLabel">Avertissement</h5>
#         <button
#           type="button"
#           class="close"
#           data-dismiss="modal"
#           aria-label="Close"
#         >
#           <span aria-hidden="true">&times;</span>
#         </button>
#       </div>
#       <div class="modal-body">Êtes-vous sûr de supprimer cet élément ?</div>
#       <div class="modal-footer">
#         <button type="button" class="btn btn-secondary" data-dismiss="modal">
#           Annuler
#         </button>
#         <button type="button" id="confirm" class="btn btn-primary btn-red">
#           Supprimer
#         </button>
#       </div>
#     </div>
#   </div>
# </div>

# <!-- Modal pour la creation  d'un etablissement  -->

# <div
#   class="modal fade"
#   id="cModal"
#   tabindex="-1"
#   role="dialog"
#   aria-labelledby="exampleModalLabel"
#   aria-hidden="true"
# >
#   <div class="modal-dialog" role="document">
#     <div class="modal-content">
#       <div class="modal-header">
#         <h5 class="modal-title" id="exampleModalLabel">Nouvel établissement</h5>
#         <button
#           type="button"
#           class="close"
#           data-dismiss="modal"
#           aria-label="Close"
#         >
#           <span aria-hidden="true">&times;</span>
#         </button>
#       </div>
#       <div class="modal-body">
#         <form
#           method="post"
#           action="/filiere_etab/etablissement/create"
#           enctype="multipart/form-data"
#         >
#           {% csrf_token %}
#           <div class="form-group">
#             <label for="recipient-name" class="col-form-label">Le nom de l'établissement :</label>
#             <input
#               type="text"
#               class="form-control"
#               name="nom"
#               required
#             />
#           </div>
#           <div class="form-group">
#           <label for="recipient-name" class="col-form-label"
#               >L'adresse de l'établissement :</label
#             >
#             <input
#               type="text"
#               class="form-control"
#               name="adresse"
#               required
#             />
#           </div>
#           <div class="form-group">
#           <label for="recipient-name" class="col-form-label"
#               >Numéro de Téléphone :</label
#             >
#            <input type="tel" name="telephone" placeholder="telephone ... " pattern="[0-9]{10}" maxlength="10" required/>
#           </div>
#           <div class="form-group">
#             <label for="exampleSelect1">Niveau</label>
#             <select name="niveau" class="form-select" id="exampleSelect1">
#               <option>Préscolaire</option>
#               <option>Primaire</option>
#               <option>Secondaire</option>
#               <option>Supérieur</option>
#             </select>
#           </div>
#           <div class="form-group">
#             <label for="exampleInputEmail1">Adresse email</label>
#             <input type="email" name="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email" required>
#           </div>
#           <div class="form-group">
#             <label for="exampleInputEmail1">Site web</label>
#             <input type="url" name="website" class="form-control" id="exampleInputEmail1" aria-describedby="urlHelp" placeholder="https://" required>
#           </div>
#           <div class="form-group">
#             <label for="recipient-name" class="col-form-label"
#               >Le logo de l'etablissement:</label
#             >
#             <input type="file" class="form-control" name="logo" />
#           </div>

#       </div>
#       <div class="modal-footer">
#         <button type="button" class="btn btn-secondary" data-dismiss="modal">
#           Annuler
#         </button>
#         <button type="submit" class="btn btn-primary">Creer</button>
#       </div>
#       </form>
#     </div>
#   </div>
# </div>

# <!-- Modal pour la  modification d'etablissement  -->

# <div
#   class="modal fade"
#   id="eModal"
#   tabindex="-1"
#   role="dialog"
#   aria-labelledby="exampleModalLabel"
#   aria-hidden="true"
# >
#   <div class="modal-dialog" role="document">
#     <div class="modal-content">
#       <div class="modal-header">
#         <h5 class="modal-title" id="exampleModalLabel">Modifier établissement</h5>
#         <button
#           type="button"
#           class="close"
#           data-dismiss="modal"
#           aria-label="Close"
#         >
#           <span aria-hidden="true">&times;</span>
#         </button>
#       </div>
#       <div class="modal-body">
#         <form
#           method="post"
#           id="editform"
#           enctype="multipart/form-data"
#         >
#           {% csrf_token %}
#           <div class="form-group">
#             <label for="recipient-name" class="col-form-label"
#               >Le nom de l'etablissement :</label
#             >
#             <input
#             id="input-nom"
#               type="text"
#               class="form-control"
#               name="nom"

#             />
#           </div>
#           <div class="form-group">
#           <label for="recipient-name" class="col-form-label"
#               >L'adresse de l'établissement :</label
#             >
#             <input
#             id="input-adresse"
#               type="text"
#               class="form-control"
#               name="adresse"
#               required
#             />
#           </div>
#           <div class="form-group">
#           <label for="recipient-name" class="col-form-label"
#               >Numéro de Téléphone :</label
#             >
#            <input
#            id="input-telephone"
#            type="tel" name="telephone" placeholder="telephone ... " pattern="[0-9]{10}" maxlength="10"  required/>
#           </div>
#           <div class="form-group">
#             <label for="exampleSelect1">Niveau</label>
#             <select name="niveau"  class="form-select" id="exampleSelect1">
#               <option>Préscolaire</option>
#               <option>Primaire</option>
#               <option>Secondaire</option>
#               <option>Supérieur</option>
#             </select>
#           </div>
#           <div class="form-group">
#             <label for="exampleInputEmail1">Adresse email</label>
#             <input type="email" name="email" class="form-control" id="input-email" aria-describedby="emailHelp" placeholder="Enter email" required>
#           </div>
#           <div class="form-group">
#             <label for="exampleInputEmail1">Site web</label>
#             <input type="url" name="website" class="form-control" id="input-website"  aria-describedby="urlHelp" placeholder="https://" required>
#           </div>
#           <div class="form-group">
#             <label for="recipient-name" class="col-form-label"
#               >Le logo de l'etablissement':</label
#             >
#             <input type="file" class="form-control" name="logo" />
#           </div>

#       </div>
#       <div class="modal-footer">
#         <button type="button" class="btn btn-secondary" data-dismiss="modal">
#           Annuler
#         </button>
#         <button type="submit" class="btn btn-primary">Modifier</button>
#       </div>
#       </form>
#     </div>
#   </div>
# </div>

# {% endblock content %}

# <!-- Specific Page JS goes HERE  -->
# {% block javascripts %}
# <script>

#   // prendre le lien de l'element a supprimer
#   var deleteLinks = document.querySelectorAll(".delete");
#   for (var i = 0; i < deleteLinks.length; i++) {
#     deleteLinks[i].addEventListener("click", function (event) {
#       event.preventDefault();
#       $("#confirm").attr("link", $(this).attr("href"));
#     });
#   }

#   // confirmation de supprission
#   $("#confirm").click(function (e) {
#     e.preventDefault();
#     console.log("hehehhehhe")
#     window.location.href = $(this).attr("link");
#   });
#   // placer le nom de la filiere et le lien de table vers la formule
#   $( ".edit" ).each(function(index) {
#   $(this).click(function (e) {
#   e.preventDefault();
#   $("#input-nom").val($(this).parent().parent().children("#nom").text());
#   $("#input-adresse").val($(this).parent().parent().children("#adresse").text());
#   $("#input-telephone").val($(this).parent().parent().children("#telephone").text());
#   $("#input-email").val($(this).parent().parent().children("#email").text());
#   $("#input-website").val($(this).parent().parent().children("#website").text());
#   $("#editform").attr("action","/filiere_etab/etablissement/edit/"+$(this).parent().parent().children("#ide").text());
# });
# });
# </script>
# {% endblock javascripts %}


import email
from re import T
from django.shortcuts import render

import os
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# from django.urls import reverse
from filiere.forms import FiliereForm
from filiere.forms import EtablissementForm

from rest_framework.response import Response
from rest_framework.decorators import api_view

from filiere.models import Filiere
from filiere.models import Etablissement

from .serializers import FiliereSerializer
from .serializers import EtablissementSerializer

######################################################
# gestion des Fillieres
######################################################

# Filiere rest api pour l'envoie de liste des filieres existes


@api_view(['GET'])
def filiere_liste(request, id):
    try:
        etab = Etablissement.objects.get(id=id)
        filieres = Filiere.objects.filter(etablissement__nom=etab.nom)
        serializer = FiliereSerializer(filieres, many=True)
        return Response(serializer.data)
    except Etablissement.DoesNotExist:
        return Response([])

# return la page principale


def index(request):
    context = {'segment': 'index'}
    filieres = Filiere.objects.all()
    context = {'filieres': filieres}
    html_template = loader.get_template('filieres/index.html')
    return HttpResponse(html_template.render(context, request))

# affichage du page de gestion des filieres


@login_required(login_url="/login/")
def filiere(request):
    context = {'segment': 'filiere'}
    data = Filiere.objects.all()
    data2 = Etablissement.objects.all()
    context['data'] = data
    context['data2'] = data2
    html_template = loader.get_template('filiere/filiere.html')
    return HttpResponse(html_template.render(context, request))

# supprission d'une filiere


@login_required(login_url="/login/")
def filiere_delete(request, id):
    filiere = Filiere.objects.get(id=id)
    if filiere.logo:
        if os.path.isfile(filiere.logo.path):
            os.remove(filiere.logo.path)
    filiere.delete()
    return HttpResponseRedirect('/filiere_etab/filiere')

# rechereche par nom d'une ou des filieres


@login_required(login_url="/login/")
def filiere_search(request):
    context = {}
    if request.method == "POST":
        term = request.POST['text']
        context['segment'] = 'filiere'
        data = Filiere.objects.all()
        context['data'] = data.filter(nom_filiere__icontains=term)
        html_template = loader.get_template('filiere/filiere.html')
        return HttpResponse(html_template.render(context, request))
    html_template = loader.get_template('filiere/page-404.html')
    return HttpResponse(html_template.render(context, request))

# creation d'une nouvelle filiere


@login_required(login_url="/login/")
def filiere_create(request):
    context = {}
    if request.method == "POST":
        form = FiliereForm(request.POST, request.FILES)
        if form.is_valid():
            nom_filiere = form.cleaned_data['nom_filiere']
            id = form.cleaned_data['etablissement']
            etab = Etablissement.objects.get(id=id)
            logo = form.cleaned_data['logo']
            if not logo:
                data = Filiere(nom_filiere=nom_filiere, etablissement=etab)
                data.save()
            else:
                data = Filiere(nom_filiere=nom_filiere,
                               etablissement=etab, logo=logo)
                data.save()
        return HttpResponseRedirect('/filiere_etab/filiere')
    html_template = loader.get_template('filiere/page-404.html')
    return HttpResponse(html_template.render(context, request))

# modification d'une filiere


@login_required(login_url="/login/")
def filiere_edit(request, id):
    context = {}
    if request.method == "POST":
        form = FiliereForm(request.POST, request.FILES)
        if form.is_valid():
            filiere = Filiere.objects.get(id=id)
            nom_filiere = form.cleaned_data['nom_filiere']
            id = form.cleaned_data['etablissement']
            if filiere.nom_filiere != nom_filiere:
                filiere.nom_filiere = nom_filiere
            if filiere.etablissement.id != id:
                etab = Etablissement.objects.get(id=id)
                filiere.etablissement = etab
            logo = form.cleaned_data['logo']
            if logo:
                if filiere.logo and len(filiere.logo) > 0:
                    os.remove(filiere.logo.path)
                filiere.logo = logo
            filiere.save()
        return HttpResponseRedirect('/filiere_etab/filiere')
    html_template = loader.get_template('filiere/page-404.html')
    return HttpResponse(html_template.render(context, request))

######################################################
# gestion des Etablissements
######################################################

# Filiere rest api pour l'envoie de liste des filieres existes


@api_view(['GET'])
def etablissement_liste(request):
    try:
        etablissements = Etablissement.objects.all()
        serializer = EtablissementSerializer(etablissements, many=True)
        return Response(serializer.data)
    except Etablissement.DoesNotExist:
        return Response([])

# affichage du page de gestion des etablissements


@login_required(login_url="/login/")
def etablissement(request):
    context = {'segment': 'etablissement'}
    data = Etablissement.objects.all()
    context['data'] = data
    html_template = loader.get_template('filiere/etablissement.html')
    return HttpResponse(html_template.render(context, request))

# supprission d'un etablissement


@login_required(login_url="/login/")
def etablissement_delete(request, id):
    etablissement = Etablissement.objects.get(id=id)
    if etablissement.logo:
        if os.path.isfile(etablissement.logo.path):
            os.remove(etablissement.logo.path)
    etablissement.delete()
    return HttpResponseRedirect('/filiere_etab/etablissement')

# rechereche par nom d'une ou des etablissements


@login_required(login_url="/login/")
def etablissement_search(request):
    context = {}
    if request.method == "POST":
        term = request.POST['text']
        context['segment'] = 'etablissement'
        data = Etablissement.objects.all()
        context['data'] = data.filter(nom__icontains=term)
        html_template = loader.get_template('filiere/etablissement.html')
        return HttpResponse(html_template.render(context, request))
    html_template = loader.get_template('filiere/page-404.html')
    return HttpResponse(html_template.render(context, request))

# creation d'une nouvelle etablissement


@login_required(login_url="/login/")
def etablissement_create(request):
    context = {}
    if request.method == "POST":

        form = EtablissementForm(request.POST, request.FILES)
        if form.is_valid():
            print("Test réussi")
            nom = form.cleaned_data['nom']
            adresse = form.cleaned_data['adresse']
            telephone = form.cleaned_data['telephone']
            logo = form.cleaned_data['logo']
            niveau = form.cleaned_data['niveau']
            website = form.cleaned_data['website']
            email = form.cleaned_data['email']
            if not logo:
                data = Etablissement(
                    nom=nom, adresse=adresse, telephone=telephone, niveau=niveau, website=website, email=email)
                data.save()
            else:
                data = Etablissement(nom=nom, adresse=adresse, telephone=telephone,
                                     logo=logo, niveau=niveau, website=website, email=email)
                data.save()
        return HttpResponseRedirect('/filiere_etab/etablissement')
    html_template = loader.get_template('filiere/page-404.html')
    return HttpResponse(html_template.render(context, request))

# modification d'une etablissement


@login_required(login_url="/login/")
def etablissement_edit(request, id):
    context = {}
    if request.method == "POST":
        form = EtablissementForm(request.POST, request.FILES)
        if form.is_valid():
            etablissement = Etablissement.objects.get(id=id)
            nom = form.cleaned_data['nom']
            adresse = form.cleaned_data['adresse']
            telephone = form.cleaned_data['telephone']
            niveau = form.cleaned_data['niveau']
            website = form.cleaned_data['website']
            email = form.cleaned_data['email']
            if etablissement.nom != nom:
                etablissement.nom = nom
            if etablissement.adresse != adresse:
                etablissement.adresse = adresse
            if etablissement.telephone != telephone:
                etablissement.telephone = telephone
            if etablissement.niveau != niveau:
                etablissement.niveau = niveau
            if etablissement.website != website:
                etablissement.website = website
            if etablissement.email != email:
                etablissement.email = email
            logo = form.cleaned_data['logo']
            if logo:
                if etablissement.logo and len(etablissement.logo) > 0:
                    os.remove(etablissement.logo.path)
                etablissement.logo = logo
            etablissement.save()
        return HttpResponseRedirect('/filiere_etab/etablissement')
    html_template = loader.get_template('filiere/page-404.html')
    return HttpResponse(html_template.render(context, request))
