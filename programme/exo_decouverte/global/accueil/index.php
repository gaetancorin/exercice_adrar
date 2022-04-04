<?php ob_start(); ?>

<div class="border border-dark bg-primary rounded-lg text-white p-2 mx-auto my-5" style="width:70%;">
    <h2 class="text-center pb-2">Instructions</h2>
    <p> 
        Bienvenue dans le camp d'entrainement PHP !</br></br>
        Ici les instructions sont simples, pour chaque nouvel exercice vous allez devoir créer un nouveau dossier 
        qui se nommera "exo1", "exo2", etc... en fonction de l'étape à laquelle vous êtes, et il contiendra un fichier
        "index.php". </br></br>
        Le dossier exo1 est déjà créé, pour les suivants, vous trouverez un modèle à copier, le dossier "exoExemple". </br></br>
        Mesdames, Messieurs, à vos claviers !
    </p>
    <p style="font-size:4px">*<em>ne pas s'amuser avec le responsive</em>.</p>
</div>

<?php
    $titre = "Camp d'entrainement PHP";
    $content = ob_get_clean();
    require "../../global/common/template.php";
?>
