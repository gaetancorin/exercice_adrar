const login = document.querySelector("#login");
const password = document.querySelector("#password");
const resultatPassword = document.querySelector("#resultatPassword");

login.addEventListener("keyup", function(){
    //maRegex, is a regex for the login/mail input
    //dans ce cas, pour un email : 
    //Avant le @ : [a-z0-9._-], on accepte les lettre de a à z, les chiffres de 0 à 9
    //Ainsi que le ".", le "-", le "_"
    //Après le @ : [a-z0-9._-], on accepte les lettre de a à z, les chiffres de 0 à 9
    //Ainsi que le ".", le "-", le "_"
    //Après le "." : +\.[a-z]{2,6}, on accepte les lettre de a à z, on accepte entre 2 et 6 lettre après 
    // le . de l'adresse mail (.fr, .com, etc...)
    let maRegex = /^[a-z0-9._-]+@[a-z0-9._-]+\.[a-z]{2,6}$/;
    //Ensuite on test notre regex avec la value de l'input login
    //Si le test fail alors on met le bgColor de l'input en rouge, sinon c'est good le bgColor est en vert
    if(!maRegex.test(login.value)){
        console.log(login.value);
        login.style.backgroundColor = "red";
    }
    else{
        login.style.backgroundColor = "green";
    }
});