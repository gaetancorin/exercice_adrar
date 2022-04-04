<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="main.css">
    <title>Login</title>
</head>

<body>
    <?php
    $bdd = new PDO(
        'mysql:host=localhost;dbname=tplogregshow',
        'root',
        '',
        array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION)
    );

    //partie 3 ajout du login
    /**
     * login
     */

    if (
        isset($_POST['mail'])
        && isset($_POST['password'])
    ) {
        $mail = $_POST['mail'];
        $password = $_POST['password'];

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
            // je vérifie le nombre de tuple en retour
            $nbrLignesRetournees = $req->rowCount();
            // si aucune tuple donc le mail est inexistant
            if ($nbrLignesRetournees == 0) {
                echo "<h5>Erreur de mail</h5>";
            } else {
                //je vérifie mon mdp
                if (password_verify($password, $donnees['password'])) {
                    // avec session
                    session_start();
                    //stockage donnees dans la session
                    $_SESSION['name'] = $donnees['name'];
                    $_SESSION['first_name'] = $donnees['first_name'];
                    $_SESSION['mail'] = $donnees['mail'];
                    $_SESSION['id_role'] = $donnees['id_role'];
                    $_SESSION['name_role'] = $donnees['name_role'];
                    echo '<p>Bonjour :
                        <h4>' . $_SESSION['name'] . ' ' . $_SESSION['first_name'] . '</h4>
                        </p>';
                } else {
                    echo "<p>Erreur de mot de passe</p>";
                }
            }
        }
    }
    ?>
    <br>

    <form action="logOut.php" method="get">
        <input type="submit" value="se déconnecter">
    </form>
    <br>
    <form action="showAllUsers.php" method="get">
        <input type="submit" value="Voir les utilisateurs">
    </form>
</body>

</html>