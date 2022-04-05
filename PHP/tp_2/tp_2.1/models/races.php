<?php

class Races 
{
    public $id_races;
    public $nom_races;
}

// attribut de stockage info de connexion BDD
public $connect;

// constructeur
public function __construct()
{
    $this->connect = $this->connect->getConnection();
}

public function getid_races(){
    return $this->id_races;
}
public function getnom_races(){
    return $this->nom_races;
}

public function setnom_races($nom_races){
    $this->nom_races = $nom_races;
}

// function CRUD
public function readAll(){
    $myQuery = "SELECT * FROM Races";

    $stmt = $this->connect->prepare($myQuery);
    $stmt->execute();
    return $stmt;
}

public function readSingle(){
    $myQuery = "SELECT * FROM Races
    WHERE id_race = :id_races";

    $stmt = $this->connect->prepare($myQuery);
    $stmt-> execute();
    return $stmt;

}

public function createOne(){
    $myQuery = "INSERT INTO Races
    SET id_race = :id_races,
        nom_race = :nom_races";

    $stmt = $this->connect->prepare($myQuery);
    $stmt->bindParam(":id_races", $this->id_races);
    $stmt->bindParam(":nom_races", $this->nom_races);
    $stmt->execute();
    return $stmt;

}

public function updateOne(){
    $myQuery = "INSERT INTO Races
    SET nom_race = :nom_races
    WHERE id_race = :id_races";

    $stmt = $this->connect->prepare($myQuery);
    $stmt->bindParam(":nom_races", $this->nom_races);
    $stmt->bindParam(":id_races", $this->id_races);
    $stmt->execute();
    return $stmt;
}

public function deleteOne(){
    "DELETE Races
    WHERE id_race = :id_races";

    $stmt = $this->connect->prepare($myQuery);
    $stmt->bindParam(":id_races", $this->id_races);
    $stmt->execute();
    return $stmt;
}
}





}

?>