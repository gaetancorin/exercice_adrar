let maVariable; 

document.getElementById("ask-hello")
.addEventListener("click", async function(){
    await ui();
    await console.log("maVariableListener = "+ maVariable);
})
function ui(){ 
    fetch("https://mockbin.com/request?greetings=salut%22")
    .then(response => response.json())
    .then(value => maVariable = value.queryString.greetings);

    console.log("mavariabledansui = "+maVariable);
    return 0; };
