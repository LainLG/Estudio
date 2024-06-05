function identificadores(){
  let codigos  = []
  for(i=1 ; i <=20 ; i++){
    idet = "answer-"
    idet += String(i) 
    codigos.push(idet)
  }
  return codigos
}

let codigos = identificadores()


let answers = ['I','You','We','She','You','I','They','We','You','He','I','You','We','She','You','I','They','We','You','He']


document.getElementById("miFormulario").addEventListener("submit", function(event) {
  event.preventDefault(); // Evita que el formulario se envíe automáticamente
  for(i=0 ; i<20 ;i++){
    let respuestaUsuario = document.getElementById(codigos[i]).value.toLowerCase(); // Obtiene la respuesta del usuario en minúsculas

    // Palabra correcta (puedes personalizar esta lista)
  
    if (respuestaUsuario === answers[i].toLowerCase()) {
      // Cambia el color de la casilla a verde si la respuesta es correcta
      document.getElementById(codigos[i]).style.borderColor = "green";
    }
    else {
      // Cambia el color de la casilla a rojo si la respuesta es incorrecta
      document.getElementById(codigos[i]).style.borderColor = "red";
    }
  }
});
