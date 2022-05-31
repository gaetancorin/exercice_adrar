<?php
class equipe
{
    //attributs
    public $id_equipe;
    public $nom_equipe;
    public $detail_equipe;

    // attribut de stockage info de connexion BDD
    public $connect;

    // constructeur
    public function __construct()
    {
        $this->connect = new ConfigDB();
        $this->connect = $this->connect->getConnection();
    }
    //getter
    public function get_id_equipe(){
        return $this->id_equipe;
    }
    public function get_nom_equipe(){
        return $this->nom_equipe;
    }
    public function get_detail_equipe(){
        return $this->detail_equipe;
    }

    //setter
    public function set_id_equipe($id_equipe){
        $this->id_equipe = $id_equipe;
    }
    public function set_nom_equipe($nom_equipe){
        $this->nom_equipe = $nom_equipe;
    }
    public function set_detail_equipe($detail_equipe){
        $this->detail_equipe = $detail_equipe;
    }

    // function CRUD
    public function lire_equipes(){
        $myQuery = "SELECT * FROM equipe";
        $stmt = $this->connect->prepare($myQuery);
        $stmt->execute();
        return $stmt;
    }

    public function lire_equipe(){
        $req = $this->connect->prepare(
            'SELECT
                    *
                FROM 
                    equipe
                WHERE 
                    equipe.nom_equipe = :nom'
        );
        $req->execute(
            array(
                ':nom' => $this->nom_equipe
            )
        );
        return $req;
    }

}
?>