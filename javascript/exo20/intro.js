class CompteBancaire{

    constructor(nom){
        this.nom = nom;
        this.montant = 0;  
        this.credit(1000) 
    }

    credit(somme){
        this.montant += somme;
        console.log(`Ajout de: ${somme} pour: ${this.nom}`);
    }

    retrait(somme){
        try {
            if (somme> this.montant) {
                throw this.nom + ", retrait de: " +  somme + " refusé avec solde: " + this.montant;           
            }
            this.montant -= somme;
            console.log(`Retrait de: ${somme} pour: ${this.nom}`);
        }
        catch (error) {
            //Quand il y a une exception elle est détectée par catch
            //Qui va afficher l'erreur (msg de throw) dans un console log
                console.log (error);
        }
    }

    visualisation(){
        console.log(`Titulaire: ${this.nom}, solde: ${this.montant} pépettes`);
    }
}



function virEntreCompte(debiteur, crediteur, somme){
    try {
        if (somme> debiteur.montant) {
            throw `Le transfert de ${debiteur.nom} et ${crediteur.nom} n'as pas eu lieu par manque d'argent`;           
        }
        debiteur.retrait(somme);
        crediteur.credit(somme);
    }
    catch (error) {
        //Quand il y a une exception elle est détectée par catch
        //Qui va afficher l'erreur (msg de throw) dans un console log
            console.log (error);
    }
}

const lesComptes = {
    "Alex" : new CompteBancaire("Alex"),
    "Clovis" : new CompteBancaire("Clovis"),
    "Marco" : new CompteBancaire("Marco"),
} 


lesComptes["Alex"].retrait(100)
virEntreCompte(lesComptes["Marco"], lesComptes["Clovis"], 300)
lesComptes["Alex"].retrait(1200)

lesComptes["Alex"].visualisation()
lesComptes["Clovis"].visualisation()
lesComptes["Marco"].visualisation()
lesComptes.Marco.visualisation()