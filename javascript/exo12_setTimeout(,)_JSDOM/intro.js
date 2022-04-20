let monTitre = document.querySelector("h1");
setTimeout(mafonction, 2000);

function mafonction(){
    monTitre.style.opacity = "1";
    monTitre.style.backgroundColor = "pink";
    monTitre.innerText = "Le bon jambon Fleury-Michon !";
};