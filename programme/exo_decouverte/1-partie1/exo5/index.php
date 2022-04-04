<?php ob_start(); //NE PAS MODIFIER 
$titre = "Exo 5 : La boucle for"; //Mettre le nom du titre de la page que vous voulez
?>

<!-- mettre ici le code -->

<?php 
    $multiplicateur = rand(0,9);
    echo "Voici la table de multiplication de $multiplicateur<br/><br/>";

    for($i=0; $i<=10; $i++){
        echo "$multiplicateur X $i = ".$multiplicateur*$i."<br/>";
    }



?>


<?php
/************************
 * NE PAS MODIFIER
 * PERMET d INCLURE LE MENU ET LE TEMPLATE
 ************************/
    $content = ob_get_clean();
    require "../../global/common/template.php";
?>
