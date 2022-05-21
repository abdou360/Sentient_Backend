
/**
 * EQUIPE : CODEVERSE et AROPEDIA
 * @authors : + KANNOUFA F. EZZAHRA
 *            + MOUZAFIR ABDELHADI
 */


 const Form = document.getElementById('modele-admin-form')

 const FiliereDataBox = document.getElementById('filiere-data-box')
 const NiveauDataBox = document.getElementById('niveau-data-box')
 const GroupeDataBox = document.getElementById('groupe-data-box')

 const FiliereInput = document.getElementById('filieres') 
 const NiveauInput = document.getElementById('niveaux') 
 const GroupeInput = document.getElementById('groupes') 
 
 const dropdownFilieres = document.getElementById('dropdownFilieres')
 const dropdownNiveaux = document.getElementById('dropdownNiveaux')
 const dropdownGroupes = document.getElementById('dropdownGroupes')
 
 const btnBox = document.getElementById('btnBox')
 
 $.ajax({
     type: 'GET',
     url: '/filieres-json/',
     success: function(response){
         console.log(response.data)
         const filieresData = response.data
         filieresData.map( item => {
             const option = document.createElement('div')
             option.textContent = item.nom_filiere
             option.setAttribute('class', 'dropdown-item')
             option.setAttribute('id', item.nom_filiere)
             FiliereDataBox.appendChild(option)
         })
 
     },
     error: function(error){
         console.log(error)
     }
 })
 
 var selectedFiliere
 var selectedNiveau
 var selectedGroupe

 FiliereInput.addEventListener('click', e=>{
     console.log(e.target.id)
     selectedFiliere = e.target.id
 
 
     
     btnBox.classList.add('disabled')
 

     NiveauDataBox.innerHTML = ""
     GroupeDataBox.innerHTML = ""
     dropdownFilieres.textContent = e.target.id
 
     
 
     $.ajax({
         type: 'GET',
         url: `/niveaux-json/${selectedFiliere}`,
         success: function(response){
             console.log(response.data) 
             const niveauxData = response.data
             niveauxData.map( item => {
                 const option = document.createElement('div')
                 option.textContent = item.nom_niveaux
                 option.setAttribute('class', 'dropdown-item')
                 option.setAttribute('id', item.nom_niveaux)
                 NiveauDataBox.appendChild(option)
             })

     
     
         },
         error: function(error){
             console.log(error)
         }
     })
 
     
 
     
 })
 