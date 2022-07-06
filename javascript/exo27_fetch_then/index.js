// API explication
// *fetch récupère l'API de l'URL en méthode "Get"
// *.then attend que la requête précédent est terminer pour s'éxécuter(différent de await)
// *le fait de déclarer une fonction dans then permet de passer le résultat précédent en paramètre pour l'utiliser 

fetch("https://mockbin.com/request?greetings=salut")
.then(response => response.json())
.then(value => console.log(value))


// et le programme fonctionnel
let message 
function askHello(){
    fetch("https://mockbin.com/request?greetings=salut")
    .then(function (res){
        if (res.ok) {
            return res.json();
        }
    })
    .then(function(value){
        message = value.queryString.greetings;
    })
    .catch(function(err){
        console.log(err);
    })
}

const button = document.getElementById("ask-hello");
function buttonchange(){
    button.innerHTML = message;
}
button.addEventListener("click", () =>{
    askHello()
    setTimeout(buttonchange, 500);
})
    
// console.log(askHello());
// console.log(message);
// setTimeout(mafonction, 1000);
// function mafonction(){
//     console.log(message)
// }