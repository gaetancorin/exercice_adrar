<?php ob_start(); //NE PAS MODIFIER 
$titre = "Exo 4 : if / else if / else - 2"; //Mettre le nom du titre de la page que vous voulez
?>

<!-- mettre ici le code -->

<?php 
    $chiffre1 = rand(-99,99);
    $chiffre2 = rand(-99,99);
    echo "chiffre 1: $chiffre1<br/>";
    echo "chiffre 2: $chiffre2<br/><br/>";

    if ((25 < abs($chiffre1) and abs($chiffre1) < 75) and (25 < abs($chiffre2) and abs($chiffre2) < 75)){
        echo "La valeur absolue de $chiffre1 - $chiffre2 est compris entre 25 et 75";
    }
    else{
        echo "La valeur absolue de $chiffre1 - $chiffre2 n'est pas compris entre 25 et 75";
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
