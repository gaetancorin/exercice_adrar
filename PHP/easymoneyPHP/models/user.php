<?php
class User
{
    // attributs par rapport à la bdd
    public $id_user;
    public $pseudo;
    public $prenom;
    public $nom;
    public $mot_de_passe;
    public $email;
    public $argent;

    // attribut de connexion à la bdd
    public $connect;

    // constructeur
    public function __construct()
    {
        $this->connect = new ConfigDB();
        $this->connect = $this->connect->getConnection();
    }

    //getter
    public function get_id_user(){
        return $this->id_user;
    }
    public function get_pseudo(){
        return $this->pseudo;
    }
    public function get_prenom(){
        return $this->prenom;
    }
    public function get_nom(){
        return $this->nom;
    }
    public function get_mot_de_passe(){
        return $this->nom;
    }
    public function get_email(){
        return $this->detail_equipe;
    }
    public function get_argent(){
        return $this->argent;
    }

    //setter
    public function set_id_user($id_user){
        $this->id_user = $id_user;
    }
    public function set_pseudo($pseudo){
        $this->pseudo = $pseudo;
    }
    public function set_prenom($prenom){
        $this->prenom = $prenom;
    }
    public function set_nom($nom){
        $this->nom = $nom;
    }
    public function set_mot_de_passe($mot_de_passe){
        $this->mot_de_passe = $mot_de_passe;
    }
    public function set_email($email){
        $this->email = $email;
    }
    public function set_argent($argent){
        $this->argent = $argent;
    }

    // // methode qui recupere tous les matchs en lien avec ses paris
    // // ranger de facon descendant(de la date la plus grande a la plus petite) 
    // public function lire_paris(){
    //     $req = $this->connect->prepare(
    //         'SELECT
    //          pseudo, nom_equipe, nom_game, mise, date_game 
    //          FROM
    //           utilisateur  
    //         inner join parier on parier.id_utilisateur = utilisateur.id_utilisateur 
    //         inner join equipe on parier.id_equipe = equipe.id_equipe 
    //         inner join game on parier.id_game = game.id_game
    //         WHERE
    //         pseudo = :pseudo;
    //         ORDER BY
    //             date_game desc;'
    //     );
    //     $req->execute(
    //         array(
    //             ':pseudo' => $this->pseudo
    //         )
    //     );
    //     return $req;
    // }
    

    // méthode qui va créer un utilisateur dans la BDD
    public function create_user(){
        try {
            //
            $maRequete = "INSERT INTO 
                                utilisateur 
                            SET 
                                pseudo = :pseudo,
                                prenom = :prenom,
                                nom = :nom,
                                mot_de_passe = :mot_de_passe,
                                email = :email";
            $req = $this->connect->prepare($maRequete);
            // pour la partie 2 je stocke le résultat de l'enregistrement dans une variable
            $req->bindParam(':pseudo', $this->pseudo);
            $req->bindParam(':prenom', $this->prenom);
            $req->bindParam(':nom', $this->nom);
            $req->bindParam(':mot_de_passe', $this->mot_de_passe);
            $req->bindParam(':email', $this->email);

            return $req->execute();
        } 
        catch (Exception $e) {
            die('Erreur : ' . $e->getMessage());
        }
    }

    // methode qui recupere un user par son pseudo et mot de passe pour connection
    public function get_one_user(){
        $req = $this->connect->prepare(
            'SELECT
                    *
                FROM 
                    utilisateur
                WHERE 
                    pseudo = :pseudo
                AND
                    mot_de_passe = :mot_de_passe'
        );
        $req->execute(
            array(
                ':pseudo' => $this->pseudo,
                ':mot_de_passe' => $this->mot_de_passe
            )
        );
        return $req;
    }

    public function lire_paris_resultats(){
        $req = $this->connect->prepare(
            'SELECT
             pseudo , equipe_parier.nom_equipe as nom_equipe_parier, equipe.nom_equipe, equipe.detail_equipe, nom_game, mise, date_game, point_equipe 
             FROM
             utilisateur  
             inner join parier on parier.id_utilisateur = utilisateur.id_utilisateur 
             inner join equipe as equipe_parier on parier.id_equipe = equipe_parier.id_equipe 
             inner join game on parier.id_game = game.id_game 
             inner join participer on participer.id_game = game.id_game 
             inner join equipe on participer.id_equipe = equipe.id_equipe 
             WHERE pseudo = :pseudo;
             ORDER BY date_game desc;'
        );
        $req->execute(
            array(
                ':pseudo' => $this->pseudo
            )
        );
        return $req;
    }

    //récupère le nom de l equipe miser et la mise de l'utilisateur connecté grace au nom_game.
    public function get_infos_mise($nom_game){
        $req = $this->connect->prepare(
            'SELECT nom_equipe, mise 
            from utilisateur 
            inner join parier on parier.id_utilisateur = utilisateur.id_utilisateur 
            inner join game on parier.id_game = game.id_game 
            inner join equipe on equipe.id_equipe = parier.id_equipe 
            where utilisateur.pseudo = :pseudo 
            and game.nom_game = :nom_game ;'
        );
        $req->execute(
            array(
                ':pseudo' => $this->pseudo,
                ':nom_game' => $nom_game
            )
        );
        while ($donnees = $req->fetch()){
            $nom_equipe_parier = $donnees["nom_equipe"];
            $mise = $donnees["mise"];

        }
        if (isset($mise)){
            return ['nom_equipe_parier' =>$nom_equipe_parier, 'mise' =>$mise,];
        }

    }

    


}