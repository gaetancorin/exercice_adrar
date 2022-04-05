<?php ob_start(); //NE PAS MODIFIER 
$titre = "Exo 11 :  Tableaux et fonctions"; //Mettre le nom du titre de la page que vous voulez
?>

<!-- mettre ici le code -->

<?php 
    $nom = "Marc";
    $note = [ 12, 15, 13, 7, 18];
    $nom2 = "Mathieu";
    $note2 = [ 11, 14, 10, 4, 20, 8, 2];

    $noteMoyenne = moyenne($note);
    echo "La note moyenne de $nom est de $noteMoyenne<br/>";
    
    $noteMoyenne2 = moyenne($note2);
    echo "La note moyenne de $nom2 est de $noteMoyenne2<br/>";

    function moyenne($note){
        $moyenne = array_sum($note)/count($note);
        return $moyenne;
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
