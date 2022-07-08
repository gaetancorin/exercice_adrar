let maVariable 

function remplirVariable(){
    fetch("https://mockbin.com/request?greetings=salut")
    .then( res => res.json())
    // .then( value => maVariable = value.queryString.greetings)
    .then(function(value){
        maVariable = value.queryString.greetings;
        console.log("remplirVariablePendant = "+ maVariable)
    })
    .then( console.log("remplirVariableApres = "+ maVariable))
}

document.getElementById("ask-hello")
.addEventListener("click", async() =>{
    await remplirVariable();
    await console.log("maVariableListener = "+ maVariable);
})
