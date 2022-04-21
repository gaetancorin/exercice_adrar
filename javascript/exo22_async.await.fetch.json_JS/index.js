let counter = document.body.querySelector("h2");
// async permet de créer une function asynchrone qui va attendre une reponse avant de poursuivre
const majCounter = async() => {
    // va chercher l'information sur l api
    // comme le mot cle "await" est employé, la recherche est asynchrone et le code attend
    let data = await fetch('https://api.countapi.xyz/hit/sltcava/visites')
    // retourne un "response" mais on a pas encore accès au données
    console.log(data)
    // recupere les donnees du response et le transforme en objet, pareil on attend
    let count = await data.json()
    // on peut enfin recuperer les donnees comme un tableau associatif / objet
    console.log(count)
    counter.innerHTML = count.value;
    counter.style.filter = "blur(0)";
}
majCounter()
