<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercice get PHP</title>
</head>
<body>
    <form action="exo_post2.php" method="post">
    <div>
        <label for="name">Nom :</label>
        <input type="text" id="name" name="user_name">
    </div>
    <div style= "margin-top: 30px;">
        <label for="firstname">Prénom :</label>
        <input type="text" id="firstname" name="user_firstname">
    </div>
    <input type="submit" value="submit" style= "margin-top: 30px;">

    </form>

<?php
    // if (($_GET["user_name"] == "patate") or ($_GET["user_firstname"] == "patate")){
    //     echo "<h1> Une madame patate ! C'est une madame patate !!</h1>";
    // }
    // if ( isset($_POST["user_name"]) and isset($_POST["user_firstname"])){
    //     echo "<p> Bonjour ".$_POST["user_name"]." ".$_POST["user_firstname"]."</p>";
    // }
    // if ( !empty($_POST["user_name"]) and !empty($_POST["user_firstname"])){
    //     echo "<p> Bonjour ".$_POST["user_name"]." ".$_POST["user_firstname"]."</p>";
    // }
    // else if ( !empty($_POST["user_name"]) xor !empty($_POST["user_firstname"])){
    //     echo "<p> Bonjour ".$_POST["user_name"]." ".$_POST["user_firstname"].", tu remplis pas tout les champs. Tu es un rebelle toi...</p>";
    // }
    
?>
    
</body>
</html>