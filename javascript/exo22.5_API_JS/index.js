let counter = document.body.querySelector("h2");
const majCounter = async() => {
    let data = await fetch('https://api.countapi.xyz/hit/sltcava/visites');
    // console.log(data)
    let count = await data.json();
    // console.log(count)
    counter.innerHTML = count.value;
    counter.style.filter = "blur(0)";
}
majCounter()

let apiAdrar = document.body.querySelector("p");
const majApiAdrar = async() => {
    let dataAdrar = await fetch("https://adrardev.fr/task/api/task.php?cat");
    // console.log(dataAdrar)
    let countAdrar = await dataAdrar.json();
    // console.log(countAdrar)

    // for (i=0; i<countAdrar.length; i++){
    //     console.log(countAdrar[i].name_cat)
    //     apiAdrar.innerHTML += `${countAdrar[i].name_cat}<br>`;  
    // }

    countAdrar.forEach((element) => {
        nouveauP = document.createElement("p");
        nouveauP.innerHTML = `${element.id_cat} : ${element.name_cat}`;
        document.body.append(nouveauP);
    })
}
majApiAdrar()