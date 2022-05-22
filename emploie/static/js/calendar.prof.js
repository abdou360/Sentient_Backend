
/**
 * EQUIPE  : CODEVERSE
 * @author : KANNOUFA FATIMA EZZAHRA
 *  
 */


// récupérer l'id du professeur connecté
idProf= $("#idProf").val();

window.onload = MyCalendar(idProf);

async function MyCalendar(idProf) {
  let data = await getSeances(idProf);
  drawCalendar(data.map( seance => {
      random_color = getRandomColor()
      return {
          title: seance.planning.libelle,
          start: dateFormat(seance.date),
          description: seance.planning.groupe.niveau.nom_niveau,
          url: "/emploie/liste-presence/" + string_to_slug(seance.planning.libelle + '-' +seance.date) + "/" + seance.id,
          color: random_color["color"],
          textColor: random_color["textColor"],
      }
  }))
}


function drawCalendar(data){
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {

        initialView: 'dayGridMonth',
        timeZone: 'local', 
        locale: 'fr',
              
        headerToolbar: {
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        
        buttonText: {
          today:    'Aujourd\'hui',
          month:    'Mois',
          week:     'Semaines',
          day:      'Jour',
        },
                
        events: data
        
  });

  calendar.render();

}





 /*
  * Utils
  */

      function string_to_slug (str) {
        str = str.replace(/^\s+|\s+$/g, ''); // trim
        str = str.toLowerCase();

        // remove accents, swap ñ for n, etc
        var from = "àáäâèéëêìíïîòóöôùúüûñç·/_,:;";
        var to   = "aaaaeeeeiiiioooouuuunc------";
        for (var i=0, l=from.length ; i<l ; i++) {
            str = str.replace(new RegExp(from.charAt(i), 'g'), to.charAt(i));
        }

        str = str.replace(/[^a-z0-9 -]/g, '') // remove invalid chars
            .replace(/\s+/g, '-') // collapse whitespace and replace by -
            .replace(/-+/g, '-'); // collapse dashes

        return str;
      }

      // read colors from json
      var colors = [
        {
          "color": "#E3E7F1",
          "textColor": "#494CA2"
        },
        {
          "color": "#FEF7DC",
          "textColor": "#A19882"
        },
        {
          "color": "#E9EFC0",
          "textColor": "#4E944F"
        },
        {
          "color": "#E9D5DA",
          "textColor": "#363062"
        },
        {
          "color": "#FDEBF7",
          "textColor": "#7A0BC0"
        },
        {
          "color": "#FED2AA",
          "textColor": "#C36A2D"
        },
        {
          "color": "#FDD2BF",
          "textColor": "#B61919"
        },
      ]

      function getRandomColor(){
      random_color = colors[Math.floor(Math.random() * colors.length)]
      return random_color
      }


      //changer le format du Date
      function dateFormat(myDate) {
      const date = new Date(myDate);

      const day = date.getDate();
      const month = date.getMonth() + 1;
      const year = date.getFullYear();    

      return year.toString() + "-" + month.toString().padStart(2,"0") + "-" +day.toString().padStart(2,"0");
      }


/*
 * fetch_data
 */
 async function getSeances(idProf) {
     let url = 'http://localhost:8000/emploie/api/prof/'+ idProf + '/seances';
 
     try {
         let data = await fetch(url);
         response = data.json()
         console.log(response)

         return await response;
 
     } catch (error) {
         console.log('Il y a eu un problème avec l\'opération fetch: ' + error.message);
     }
 } 
 