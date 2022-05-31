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
    <title>connexion</title>
</head>
<body class="bodyInscription">
    <?php
        include('./inc/header.php');

    ?>

    <div class="containerInscription">
        <div class="inscriptionFormulaire">
            <h1>Connecter-vous !</h1>
            <form id="form_text" action="../controllers/getConnexion.php" method="POST">
                <label for="pseudo">Quel est votre pseudo ?</label>
                <input type="text" name="pseudo" placeholder="Votre pseuso" id="pseudo" required>
                <label for="pwd">Quel est votre mot de passe ?</label>
                <input type="text" name="pwd" placeholder="Votre mot de passe" id="pwd" required>        
                <button type="submit" value="Valider">Valider</button>
            </form>
        </div>
    </div>  
</body>
</html>