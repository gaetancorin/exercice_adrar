<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="main.css">
    <title>Register</title>
</head>

<body>
    <?php

    //partie 1
    /**
     * création du code pour créer un compte avec hash de mdp
     */

    // j'isole dans une variable le système de connexion PDO car besoin dans les parties suivantes
    $bdd = new PDO(
        'mysql:host=localhost;dbname=tplogregshow',
        'root',
        '',
        array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION)
    );

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

        $bdd->exec("set names utf8");
        try {
            //
            $req = $bdd->prepare(
                "INSERT INTO 
                        users 
                    SET 
                        name = :name,
                        first_name = :first_name,
                        mail = :mail,
                        password = :password,
                        id_role = :role"
            );
            /*$req->execute(
                array(
                    ':name' => $name,
                    ':first_name' => $first_name,
                    ':mail' => $mail,
                    ':password' => $password,
                    ':role' => $role
                )
            );*/
            // pour la partie 2 je stocke le résultat de l'enregistrement dans une variable
            $resultat = $req->execute(
                array(
                    ':name' => $name,
                    ':first_name' => $first_name,
                    ':mail' => $mail,
                    ':password' => $password,
                    ':role' => $role
                )
            );
            /**
             *  partie 2 
             */
            // si resultat ok je fais ma connexion auto après l'enregistrement
            if ($resultat) {
                //ajout session
                session_start();
                $req = $bdd->prepare(
                    'SELECT
                        *
                    FROM 
                        users
                    JOIN
                        roles
                    ON
                        users.id_role = roles.id_role
                    WHERE 
                        mail = :mail'
                );
                $req->execute(
                    array(
                        ':mail' => $mail
                    )
                );
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
    ?>
    <form action="logOut.php" method="get">
        <input type="submit" value="se déconnecter">
    </form>
    <br>
    <form action="showAllUsers.php" method="get">
        <input type="submit" value="Voir les utilisateurs">
    </form>
</body>

</html>