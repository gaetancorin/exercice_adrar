leTitre = document.body.querySelector("h1");
monInput = document.body.querySelector("input");

monInput.addEventListener("keypress", function(event){
    console.log(event);
    leTitre.innerText += event.key;
})