window.onload = MyCalendar;

/**
 * RESPONSABLE : CODEVERSE
 * @author : KANNOUFA FATIMA EZZAHRA
 *  
 */


/*
 * Fetching data
 */
async function getData() {
    let url = 'http://localhost:8000/api/';

    try {
        let data = await fetch(url);
        response = data.json()
        console.log(response)

        return await response;

    } catch (error) {
        console.log('Il y a eu un problème avec l\'opération fetch: ' + error.message);
    }
} // Fin getData

async function MyCalendar() {
    let data = await getData();
    drawCalendar(data.map( event => {
        return {
            title: event.quote,
            start: event.pub_date,
            url: "http://localhost:8000/api/" + event.id,
            color: '#eafaf7',
            textColor: '#068686',
        }
    }))

}


/*
 * Calendar
 */
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
      ;
}
