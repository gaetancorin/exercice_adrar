<?php ob_start(); //NE PAS MODIFIER 
$titre = "Exo 7 :  La boucle while"; //Mettre le nom du titre de la page que vous voulez
?>

<!-- mettre ici le code -->

<?php 
    $numberRandom = rand(1,20);
    $essai = 0;
    while ($numberRandom <=15){
        $essai += 1;
        echo "Essaie $essai : $numberRandom, c'est inférieur à 15<br/>";
        $numberRandom = rand(1,20);
    }
    $essai +=1;
    echo "Essaie $essai : $numberRandom, c'est supérieur à 15<br/>";

?>


<?php
/************************
 * NE PAS MODIFIER
 * PERMET d INCLURE LE MENU ET LE TEMPLATE
 ************************/
    $content = ob_get_clean();
    require "../../global/common/template.php";
?>
