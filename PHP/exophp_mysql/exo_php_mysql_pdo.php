<?php

function connection_BD(){
try {
    $db = new PDO("mysql:host=localhost;dbname=exo1_php;charset=utf8", "root", "");
    return $db;
    } 
catch (Exception $e) {
    die($e->getMessage());
    }
return $db;
}
?>
