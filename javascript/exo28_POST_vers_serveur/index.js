// récupère l'élement formulaire et lors de l'envois, envois son contenu à la fonction send
document
.getElementById("form")
.addEventListener("submit", function(e)
                  {
                  send(e);
}
);

function send(e) {
    // retire les fonctions par default du formulaire
    e.preventDefault();
    // envois au serveur grace à la méthode POST la value de l'input avec ID "value"
    // cette value est transformé en JSON pour être envoyé 
    fetch("https://mockbin.com/request", {
      method: "POST",
      headers: {
        'Accept': 'application/json', 
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({value: document.getElementById("value").value})

    })
    // une fois envoyé, on récupère une réponse du serveur que l'on transforme en json
    .then(function(res) {
      if (res.ok) {
        return res.json();
      }
    })
    // puis on l'insère dans une balise
    .then(function(value) {
        document
          .getElementById("result")
          .innerText = value.postData.text;
    });
  }