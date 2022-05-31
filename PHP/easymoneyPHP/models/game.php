<?php
class game
{
    // attributs par rapport à la bdd
    public $id_game;
    public $date_game;
    public $nom_game;

    // attribut de connexion à la bdd
    public $connect;

    // constructeur
    public function __construct()
    {
        $this->connect = new ConfigDB();
        $this->connect = $this->connect->getConnection();
    }

    //getter
    public function get_id_game(){
        return $this->id_game;
    }
    public function get_date_game(){
        return $this->date_game;
    }
    public function get_nom_game(){
        return $this->nom_game;
    }

    //setter
    public function set_id_game($id_game){
        $this->id_game = $id_game;
    }
    public function set_date_game($date_game){
        $this->date_game = $date_game;
    }
    public function set_nom_game($nom_game){
        $this->nom_game = $nom_game;
    }

    // methode qui recupere toutes les infos des games avec les points
    //  de aujourd'hui jusqu'a dans le passé
    public function lire_games_finis(){
        $req = $this->connect->prepare(
            'SELECT
                    nom_game, date_game, nom_equipe, detail_equipe, point_equipe
                FROM 
                    equipe
                INNER JOIN
                    participer
                ON 
                    participer.id_equipe = equipe.id_equipe
                INNER JOIN
                    game
                ON 
                    game.id_game = participer.id_game
                WHERE 
                    date_game between "1900-01-01" and now()
                ORDER BY
                     date_game desc'
        );
        $req->execute();
        return $req;
    }

    // methode qui recupere toutes les infos des games avec les points
    //  de aujourd'hui jusqu'a dans le futur
    public function lire_games_futurs(){
        $req = $this->connect->prepare(
            'SELECT
                    nom_game, date_game, nom_equipe, detail_equipe
                FROM 
                    equipe
                INNER JOIN
                    participer
                ON 
                    participer.id_equipe = equipe.id_equipe
                INNER JOIN
                    game
                ON 
                    game.id_game = participer.id_game
                WHERE 
                    date_game between now() and "2200-01-01"
                ORDER BY
                     date_game asc'
        );
        $req->execute();
        return $req;
    }
    // méthode qui récupère toutes les informations d'une game
    public function get_one_game(){
        $req = $this->connect->prepare(
            'SELECT
            nom_game, date_game, nom_equipe, detail_equipe, point_equipe
            FROM 
                equipe
            INNER JOIN
                participer
            ON 
                participer.id_equipe = equipe.id_equipe
            INNER JOIN
                game
            ON 
                game.id_game = participer.id_game
            WHERE 
                nom_game = :nom_game
            ORDER BY
                date_game desc;'
        );
        $req->execute(
            array(
                ':nom_game' => $this->nom_game
            )
        );
        return $req;
    }

    // methode qui calcul le pourcentage d'argent miser sur chaque equipe d'un match
    public function calcul_pourcentage_miser_total($nom_equipe1,$nom_equipe2){
        // recupere tous les paris du matchs
        $req = $this->connect->prepare(
            'SELECT
             nom_game, mise, nom_equipe 
             from game 
             inner join parier on parier.id_game = game.id_game 
             inner join equipe on parier.id_equipe = equipe.id_equipe 
              where nom_game = :nom_game;'
        );
        $req->execute(
             array(
                 ':nom_game' => $this->nom_game
             )
        );
        // on enregistre le total des mises dans des variables
        $mise_total_equipe1 = 0;
        $mise_total_equipe2 = 0;
        // la mise est additionner en fonction de son nom d'equipe
        while ($donnees = $req->fetch()){

            if ($donnees["nom_equipe"] == $nom_equipe1){
                $mise_total_equipe1 += $donnees["mise"];
            }
            else if ($donnees["nom_equipe"] == $nom_equipe2){
                $mise_total_equipe2 += $donnees["mise"];
                
            }
        }
        // on transforme les mises total d'equipe en pourcentage
        // comme on ne peut pas diviser par 0, il faut gerer si aucun pari n'est pris
        if ($mise_total_equipe1 == 0 && $mise_total_equipe2 == 0){
            $pourcentage_equipe1 = 50;
            $pourcentage_equipe2 = 50;
            return [$pourcentage_equipe1, $pourcentage_equipe2];
        }
        else{
            $mise_total = $mise_total_equipe1 + $mise_total_equipe2;
            // round(nombre, arrondis) arrondis a 2 chiffres apres la virgule
            $pourcentage_equipe1 = round(($mise_total_equipe1/$mise_total*100),2);
            $pourcentage_equipe2 = round(($mise_total_equipe2/$mise_total*100),2);

            return [$pourcentage_equipe1, $pourcentage_equipe2];
        }
    }




    
}