<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+Display:ital,wght@0,400;0,500;0,600;0,700;1,500;1,700&display=swap" rel="stylesheet"> 
    <link rel="stylesheet" href="../style.css">
    <script src="https://kit.fontawesome.com/8e8d5e63b3.js"></script>
    <title>Inscription</title>
</head>
<body class="bodyInscription">
    <?php
        include('./inc/header.php');

    ?>

    <div class="containerInscription">
        <div class="inscriptionFormulaire">
            <h1>Inscrivez-vous !</h1>
            <form id="form_text" action="../controllers/getInscription.php" method="POST">
                <label for="prenom">Quel est votre prénom</label>
                <input type="text" name="prenom" placeholder="Votre prénom" id="prenom" required>
                <label for="nom">Quelle est votre nom ?</label>
                <input type="text" name="nom" placeholder="Votre nom" id="nom" required>
                <label for="pseudo">Choisissez un pseudo:</label>
                <input type="text" name="pseudo" placeholder="Votre pseuso" id="pseudo" required>
                <label for="pwd">Quel est votre mot de passe ?</label>
                <input type="text" name="pwd" placeholder="Votre mot de passe" id="pwd" required>
                <label for="pseudo">Quel est votre email:</label>
                <input type="text" name="email" placeholder="Votre email" id="email" required>
                <label for="pseudo">Avez vous des fonds ? Si oui, combien ?</label>
                <input type="text" name="fond" placeholder="Vos fonds" id="fond" required>

        
                <button type="submit" value="Valider">Valider</button>
            </form>
        </div>
    </div>  
</body>
</html>