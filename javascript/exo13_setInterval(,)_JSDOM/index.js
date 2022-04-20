let monTitre = document.querySelector("h1");
let timer = 3;

monTitre.addEventListener("click", function(){
    // console.log(monTitre)
    let countDown = setInterval(mafonction, 1000);
    function mafonction(){
        if (timer > 0){
            monTitre.innerHTML = timer;
        }
        else{
            monTitre.innerHTML = "GO GO GO !";
        }
        timer -= 1;
        console.log(timer);
    }

});