let createh1 = document.createElement("h1");
createh1.innerText = "Super";
document.body.append(createh1)

function ajoutText(pseudo, duTxt){
    nouveauTxt = document.createElement("p");
    nouveauTxt.innerText = pseudo+" : "+ duTxt;
    document.body.append(nouveauTxt)
}

ajoutText("Michel", "il est très fort")

