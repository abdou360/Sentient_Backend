
/**
 * EQUIPE  : CODEVERSE
 * @author : KANNOUFA FATIMA EZZAHRA
 *  
 */


 export async function getSeances(idProf) {
    let url = 'http://localhost:8000/emploie/api/prof/'+ idProf + '/seances';

    try {
        let data = await fetch(url);
        response = data.json()

        return await response;

    } catch (error) {
        console.log('Il y a eu un problème avec l\'opération fetch: ' + error.message);
    }
}