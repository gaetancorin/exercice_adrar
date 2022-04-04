<?php
include('../models/bdd.php');
include('../views/vue.php');

session_start();
if (isset($_GET)) {

    $bdd = new PDO(
        'mysql:host=localhost;dbname=tplogregshow',
        'root',
        '',
        array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION)
    );

    $bdd->exec("set names utf8");
    try {

        $req = $bdd->prepare(
            'SELECT
                *
            FROM 
                users
            JOIN
                roles
            ON
                users.id_role = roles.id_role'
        );
        $req->execute();
        while ($donnees = $req->fetch()) {
            // je demande à afficher que les utilisateurs autres que mon utilisateur
            if ($_SESSION['mail'] != $donnees['mail']) {
                // également je vais vouloir filtrer le résultat selon le rôle
                // si membre => je vois que les membres
                // si modérateur => je vois membres et modérateurs
                // si administrateur => je vois tous les utilisateurs.
                if ($_SESSION['id_role'] <= $donnees['id_role']) {
                    echo '<section>
                        <h5>' . $donnees['id_user'] . '</h5>
                        <h4>' . $donnees['name'] . '</h4>
                        <h4>' . $donnees['first_name'] . '</h4>
                        <h5>' . $donnees['mail'] . '</h5>
                        <p>' . $donnees['name_role'] . '</p>
                    </section>
                    <br>';
                }
            }
        }
    } catch (Exception $e) {
        die('Erreur : ' . $e->getMessage());
    }
}
?>