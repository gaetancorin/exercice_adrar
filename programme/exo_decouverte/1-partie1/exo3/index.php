<?php ob_start(); //NE PAS MODIFIER 
$titre = "Exo 3 : if / else if / else"; //Mettre le nom du titre de la page que vous voulez
?>

<!-- mettre ici le code -->
<?php
    $numberRandom = rand(1,20);
    echo "Le nombre est: $numberRandom";
    echo "<br/><br/>";

    if ($numberRandom <= 5){
        echo "Il est compris entre 1 et 5";
    }
    else if ($numberRandom <= 10){
        echo "Il est compris entre 6 et 10";
    }
    else if ($numberRandom <= 15){
        echo "Il est compris entre 11 et 15";
    }
    else if ($numberRandom <= 20){
        echo "Il est compris entre 16 et 20";
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
