<?php ob_start(); //NE PAS MODIFIER 
$titre = "Exo 2 : Variables et Ternaires"; //Mettre le nom du titre de la page que vous voulez
?>

<!-- mettre ici le code -->
<?php
     $nom = "Julie";
    $age = 40;
    $homme = false;

    $nom2 = "Joe";
    $age2 = 46;
    $homme2 = true;

    echo "$nom a $age ans et c'est ";
    echo $homme ? "un homme" : "une femme"; 

    echo "<br/><br/>";

    echo "$nom2 a $age2 ans et c'est ";
    echo $homme2 ? "un homme" : "une femme"; 


?>


<?php
/************************
 * NE PAS MODIFIER
 * PERMET d INCLURE LE MENU ET LE TEMPLATE
 ************************/
    $content = ob_get_clean();
    require "../../global/common/template.php";
?>
