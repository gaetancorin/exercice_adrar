<?php
require('../models/bdd.php');
require('../models/user.php');
include('../views/vue.php');
// je vérifie que mes champs ne sont pas vides
if (
    !empty($_POST['name'])
    && !empty($_POST['first_name'])
    && !empty($_POST['mail'])
    && !empty($_POST['password'])
    && !empty($_POST['role'])
) {
    $name = $_POST['name'];
    $first_name = $_POST['first_name'];
    $mail = $_POST['mail'];
    // je hache le password
    $password = password_hash($_POST['password'], PASSWORD_BCRYPT);
    $role = $_POST['role'];

    try {

        $myUser = new User();
        $myUser->name = $name;
        $myUser->first_name = $first_name;
        $myUser->mail = $mail;
        $myUser->password = $password;
        $myUser->id_role = $role;
        $resultat = $myUser->createUser();
        if ($resultat) {
            //ajout session
            session_start();
            $req = $myUser->getSingleUser();
            while ($donnees = $req->fetch()) {
                // stockage des donnees dans super globale $_session
                $_SESSION['name'] = $donnees['name'];
                $_SESSION['first_name'] = $donnees['first_name'];
                $_SESSION['mail'] = $donnees['mail'];
                $_SESSION['id_role'] = $donnees['id_role'];
                $_SESSION['name_role'] = $donnees['name_role'];
            }
            echo '<p>Bienvenue : <h4>' . $_SESSION['name'] . ' ' . $_SESSION['first_name'] . '</h4></p>';
        } else {
            echo "<p>Erreur lors de l'enregistrement</p>";
        }
    } catch (Exception $e) {
        die('Erreur : ' . $e->getMessage());
    }
}
