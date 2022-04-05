<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercice PHP mysql</title>
</head>
<body>
    <form method="get">
    <div>
        <label  for="pseudo">Pseudo :</label>
        <input style= "margin-top: 30px;" type="text" id="pseudo" name="pseudo">
    </div>
    <input type="submit" value="submit" style= "margin-top: 30px; margin-left: 50px;">

    </form>

<?php
include("exo_php_mysql_pdo.php");
include("exo_php_mysql_requete.php");

if (isset($_GET['pseudo'])) {
    $data = requete_findUser($_GET['pseudo']);
    if ($data) {
        var_dump($data);
        echo "<p>Bonjour " . ucfirst($data[0]->user_pseudo) . ", vous êtes l'id numéro : " . $data[0]->user_id . "</p>";
    } else if (empty($_GET['pseudo'])){
        echo "<p>Veuillez remplir le champ !</p>";
    } else {
        echo "<p>Tu vois bien que je ne suis pas dans la liste !</p>";
    }
}

    
?>
    
</body>
</html>