<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../style.css">
    <script src="https://kit.fontawesome.com/8e8d5e63b3.js"></script>
    
    <title>Profil</title>
</head>
<body class="bodyProfil">
<?php include('./inc/header.php');?>

    <h1>Les Paris en cours:</h1>
        
    <?php include('../controllers/getMatchFutur.php');?>
<br>
    <h1>Les Paris terminés:</h1>
        
    <?php include('../controllers/getMatchFini.php');?>

</p> 
</div>
</div>
</body>
</html>