<?php
session_start();

$idSession = session_id();

$_SESSION["prenom"] = "Jonathan";
$_SESSION["age"] = 40;
$_SESSION["sante"] = "est covidé";


?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>test de Session</h1>
    <?php
    if($idSession){
        echo "ID de session via fonction session_id() : </br>".$idSession."</br>";
    }
    echo "</br></br>";

    if (isset($_COOKIE["PHPSESSID"])){
        echo 'ID de session récupéré via super globale $_COOKIE: </br>' .$_COOKIE["PHPSESSID"];
    }
    echo "</br></br>";
    echo "Hello ".$_SESSION["prenom"].", quel âge as-tu ? </br> oh ok ".$_SESSION["age"]."!!!  </br>et comment te sent tu ? . </br> Et bien tout simplement ".$_SESSION["prenom"]." ".$_SESSION["sante"]."</br></br>";

    if (isset($_SESSION["prenom"])){
        echo "la session est defini</br>";
    }
    else {
        echo "la session n'est pas defini</br>";
    }

    session_unset();

    if (isset($_SESSION["prenom"])){
        echo "la session est defini</br>";
    }
    else {
        echo "la session n'est pas defini</br>";
    }
    ?>
</body>
</html>