<?php

include('../config/bdd.php');
include('../models/user.php');

if (
    !empty($_POST['prenom'])
    && !empty($_POST['nom'])
    && !empty($_POST['pseudo'])
    && !empty($_POST['pwd'])
    && !empty($_POST['email'])
    && !empty($_POST['fond'])
) {
    $prenom = $_POST['prenom'];
    $nom = $_POST['nom'];
    $pseudo = $_POST['pseudo'];
    $pwd = $_POST['pwd'];
    $email = $_POST['email'];
    $fond = $_POST['fond'];
    
    
    try{
        $user = new User();
        $user->set_prenom($prenom);
        $user->set_nom($nom);
        $user->set_pseudo($pseudo);
        $user->set_mot_de_passe($pwd);
        $user->set_email($email);
        $user->set_argent($fond);

        $resultat = $user->create_user();

        header('Location: ../index.php');

    } catch (Exception $e){
        die('Erreur : ' . $e->getMessage());
    }

}


    
?>