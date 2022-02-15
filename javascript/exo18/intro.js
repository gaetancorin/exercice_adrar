class Pme{

    constructor(nom, equipeDeSalarie, revenu, fraisFixes, fraisdAchat){
        this.nom = nom;
        this.equipeDeSalarie = equipeDeSalarie;
        this.revenu = revenu;
        this.fraisFixes = fraisFixes;
        this.fraisdAchat = fraisdAchat;
        this.fraisEquipeDeSalarie = this.calculFraisEquipe();
    }

    bilan(){
        console.log(`Nom de la Pme : ${this.nom}`);
        console.log(`Revenu annuel : ${this.revenu}`);
        console.log(`frais Fixes : ${this.fraisFixes}`);
        console.log(`frais d'achat : ${this.fraisdAchat}`);
        console.log(`frais de l'Equipe : ${this.fraisEquipeDeSalarie}`);
        console.log(`Revenu net : ${this.calculBilan()}`);
    }

    calculFraisEquipe(){
        let fraisTotalEquipe = 0
        this.equipeDeSalarie.forEach(salarie => 
            fraisTotalEquipe += salarie.chargeTotal())
        return fraisTotalEquipe
    }

    calculBilan(){
        return this.revenu - (this.fraisFixes + this.fraisdAchat + this.fraisEquipeDeSalarie)
    }

}

class Employee{

    constructor(nom, prenom, age, salaireMensuel){
        this.nom = nom;
        this.prenom = prenom;
        this.age = age;
        this.salaireMensuel = salaireMensuel;
        this.payeParAn = 12;
        this.chargePatronal = 0.9;
    }

    chargeTotal(){
        let chargetotal = this.salaireMensuel * this.payeParAn;
        chargetotal = chargetotal + chargetotal * this.chargePatronal;
        return chargetotal;
    }
}

// a = new Employee ("Duval", "Paul", 30, 2000);
// console.log(a.chargeTotal())

const pme = new Pme (
        "Ma Petite Entreprise", 
        [new Employee("Duval", "Paul", 30, 2000),
        new Employee("Durand", "Alain", 40, 3000),
        new Employee("Dois", "Sylvia", 50, 4000),],
        300000,
        20000,
        50000);
        
pme.bilan();

