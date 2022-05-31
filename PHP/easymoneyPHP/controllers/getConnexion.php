<?php

include('../config/bdd.php');
include('../models/user.php');

if ( !empty($_POST['pseudo']) && !empty($_POST['pwd']) ) {
    $pseudo = $_POST['pseudo'];
    $pwd = $_POST['pwd'];  
    
    try{
        $myUser = new User();
        $myUser->set_pseudo($pseudo);
        $myUser->set_mot_de_passe($pwd);

        $req = $myUser->get_one_user();

        // je vérifie le nombre de tuple en retour
        $nbrLignesRetournees = $req->rowCount();
        // si aucune tuple donc le mail est inexistant
        if ($nbrLignesRetournees == 0) {
            header('Location: ../views/erreurConnexion.php');
        }

        while ($donnees = $req->fetch()) {
            
            // ouverture de la session
            session_start();
            //stockage donnees dans la session
            $_SESSION['pseudo'] = $donnees['pseudo'];
            $_SESSION['prenom'] = $donnees['prenom'];
            $_SESSION['nom'] = $donnees['nom'];
            $_SESSION['email'] = $donnees['email'];
            echo '<p>Bonjour :
                    <h4>' . $_SESSION['prenom'] . ' ' . $_SESSION['nom'] . '</h4>
                    </p>';

            header('Location: ../index.php');
        }
        
    } 
    catch (Exception $e){
        die('Erreur : ' . $e->getMessage());
    }

}
    
?>