leTitre = document.body.querySelector("h1");
console.log(leTitre);
lesLiens = document.body.getElementsByTagName("a");
console.log(lesLiens);

lesLiens[0].addEventListener("click", myFunction);

function myFunction() {
    leTitre.classList.add('maCouleur');
}


lesLiens[1].addEventListener("click", myFunction2);

function myFunction2() {
    leTitre.classList.remove('maCouleur');
}


lesLiens[2].addEventListener("click", myFunction3);

function myFunction3() {
    leTitre.classList.toggle('maCouleur');
}