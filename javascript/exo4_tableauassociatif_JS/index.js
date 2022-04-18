let voiture = {
    "vitesse" : 500,
    "nbChevaux" : 500,
    "pilotes" : ["JAKO", "JANINE"]
}

//tableau associatif
console.log(voiture["pilotes"]);
console.log(voiture.pilotes);
//Object classique
console.log(voiture.vitesse);

//un tableau associatif et un object est la même chose
// a ne pas confondre avec une class(le moule de l'object)
// exemple de class avec methode=

// class Nomdeobject{

//     constructor(nom, poids, taille){
//         this.nom = nom;
//         this.poids = poids;
//         this.taille = taille;
//         this.imc = this.calculImc(poids, taille);
//     }

//     calculImc(poids, taille){
//         return (poids / (taille * taille)).toFixed(2);
//     }

//     methode(){
//         console.log(`${this.nom} (${this.poids} kg, ${this.taille}) a un IMC de : ${this.imc}`)
//     }
// }
