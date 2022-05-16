
/**
 * EQUIPE  : CODEVERSE
 * @author : KANNOUFA FATIMA EZZAHRA
 *  
 */


//  transformer une chaine de caractère en slug
export function string_to_slug (str) {
    str = str.replace(/^\s+|\s+$/g, ''); // trim
    str = str.toLowerCase();
  
    var from = "àáäâèéëêìíïîòóöôùúüûñç·/_,:;";
    var to   = "aaaaeeeeiiiioooouuuunc------";
    for (var i=0, l=from.length ; i<l ; i++) {
        str = str.replace(new RegExp(from.charAt(i), 'g'), to.charAt(i));
    }
  
    str = str.replace(/[^a-z0-9 -]/g, '')
        .replace(/\s+/g, '-')
        .replace(/-+/g, '-');
  
    return str;
}


//  Modifier le format du date (Format retourné : yyyy-mm-dd)
export function dateFormat(myDate) {
    const date = new Date(myDate);
  
    const day = date.getDate();
    const month = date.getMonth() + 1;
    const year = date.getFullYear();    
  
    return year.toString() + "-" + month.toString().padStart(2,"0") + "-" +day.toString().padStart(2,"0");
}
   



//  retourner un couleur aléatoire
// read colors from json
var colors = [
      {
          "color": "#eafaf7",
          "textColor": "#068686"
      },
      {
        "color": "#fd8ea3",
        "textColor": "#b44141"
      },
      {
        "color": "#58cbb6",
        "textColor": "#068686"
    },
    {
      "color": "#ffe485",
      "textColor": "#b44141"
    },
  ]

export function getRandomColor(){
  random_color = colors[Math.floor(Math.random() * colors.length)]
  return random_color
}