monTitre = document.body.querySelector("h1");
console.log(monTitre)

document.addEventListener("mouseout", myFunction);

function myFunction() {
    monTitre.setAttribute("style", "display:block");
}