<?php
function myConnection(){
    $bdd = new PDO(
        'mysql:host=localhost;dbname=tplogregshow',
        'root',
        '',
        array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION)
    );
    $bdd->exec("set names utf8");
    return $bdd;
}
?>