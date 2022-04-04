<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>tp_1</title>
</head>
<body>

<form action="index.php" method="POST" enctype="multipart/form-data" style="display: block;">
   <p><button>Créer un compte</button></p>
   <p><button>Se connecter</button></p>
</form>


<form action="index.php" method="POST" enctype="multipart/form-data" style="display: none;">
    <h2>Créer un compte</h2>

    <label for="name">Name</label></br>
    <input type="text" id="name" name="name" required></br>

    <label for="firstname">firstname</label></br>
    <input type="text" id="firstname" name="firstname" required></br>

    <label for="mail">mail</label></br>
    <input type="email" id="mail" name="mail" required></br>

    <label for="password">password</label></br>
    <input type="text" id="password" name="password" required></br>

    <label for="role">Roles</label></br>
    <select name="role" id="roleSelect">
        <option value="">--choississez un rôle--</option>
        <option value="1">Administrateur</option>
        <option value="2">Modérateur</option>
        <option value="3">Membre</option>
    </select>

    <p><button type="submit">Validé</button></p></br>
    <p><button>Se connecter</button></p>
</form>

<form action="index.php" method="POST" enctype="multipart/form-data" style="display: none;">
    <h2>Se Connecter</h2>

    <label for="mail">mail</label></br>
    <input type="email" id="mail" name="mail" required></br>

    <label for="password">password</label></br>
    <input type="text" id="password" name="password" required></br>
    <p><button type="submit">Validé</button></p></br>
    <p><button>Créer un compte</button></p>
</form>

<script src="./tp_1_js.js"></script>
</body>
</html>