let counter = document.body.querySelector("h2");
// async permet de créer une function asynchrone qui va attendre une reponse avant de poursuivre
const majCounter = async() => {
    // va chercher l'information sur l api
    // comme le mot cle "await" est employé, la recherche est asynchrone et le code attend
    let data = await fetch('http://localhost:3000/api/stuff');
    // retourne un "response" mais on a pas encore accès au données
    await console.log(data);
    // recupere les donnees du response et le transforme en objet, pareil on attend
    let count = await data.json();
    // on peut enfin recuperer les donnees comme un tableau associatif / objet
    await console.log(count);
    counter.innerHTML = count[0].title;
    counter.style.filter = "blur(0)";
}
majCounter();

var xhr = new XMLHttpRequest(),
    method = "GET",
    url = "http://localhost:3000/api/stuff";

xhr.open(method, url, true);
xhr.onreadystatechange = function () {
  if(xhr.readyState === 4 && xhr.status === 200) {
    console.log(xhr.responseText);
  }
};
xhr.send();
