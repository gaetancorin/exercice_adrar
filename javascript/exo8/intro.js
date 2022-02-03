
let monTxt = document.body.querySelector("textarea");
let rendu = document.body.querySelector("div");
monTxt.value = localStorage.getItem("monSuperText");
if (monTxt.value == true){
    rendu.innerHTML = localStorage.getItem("monSuperText");
}
monTxt.addEventListener("keyup", function(){
    localStorage.setItem("monSuperText", monTxt.value);
    rendu.innerHTML = monTxt.value;
})
