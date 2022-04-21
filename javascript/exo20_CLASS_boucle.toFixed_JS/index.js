class imc{

    constructor(nom, poids, taille){
        this.nom = nom;
        this.poids = poids;
        this.taille = taille;
        this.imc = this.calculImc(poids, taille);
    }

    calculImc(poids, taille){
        return (poids / (taille * taille)).toFixed(2);
    }

    display(){
        console.log(`${this.nom} (${this.poids} kg, ${this.taille}) a un IMC de : ${this.imc}`)
    }
}

let list = []

list.push(new imc("roger", 150, 1.50))
list.push(new imc("pierre richard", 60, 1.82))
list.push(new imc("fourmis", 0.02, 0.02))

for (let nombre = 0; nombre < list.length; nombre++){
    list[nombre].display()
};

// let moi = new imc("gaetan", 76, 1.84);
// console.log(moi.imc)
// moi.display()