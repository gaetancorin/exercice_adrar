<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="main.css">
    <title>TP</title>
</head>

<body>
    <form id="reg" action="./controllers/register.php" method="POST">
        <p>Créer un compte</p>
        <p>name</p>
        <input type="text" name="name">
        <br>
        <p>first_name</p>
        <input type="text" name="first_name">
        <br>
        <p>mail</p>
        <input type="text" name="mail">
        <br>
        <p>password</p>
        <input type="text" name="password">
        <br>
        <br>
        <label for="rolesSelect">Roles</label>
        <br>
        <select name="role" id="rolesSelect">
            <option value="">--Choisissez un rôle--</option>
            <option value="1">Administrateur</option>
            <option value="2">Modérateur</option>
            <option value="3">Membre</option>
        </select>
        <br>
        <br>
        <input type="submit" value="Valider">
    </form>
    <br>
    <form id="log" action="./controllers/login.php" method="POST">
        <p>Se Connecter</p>
        <p>mail</p>
        <input type="text" name="mail">
        <br>
        <p>password</p>
        <input type="text" name="password">
        <br>
        <br>
        <input type="submit" value="Valider">
    </form>
    <br>
    <button id="regBt" style>Créer un compte</button>
    <br>
    <button id="logBt">Se connecter</button>
    <br>
    <script type='text/javascript' src="main.js"></script>
</body>

</html>