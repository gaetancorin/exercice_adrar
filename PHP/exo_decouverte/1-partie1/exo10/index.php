<?php ob_start(); //NE PAS MODIFIER 
$titre = "Exo 10 :  Les tableaux - 2"; //Mettre le nom du titre de la page que vous voulez
?>

<!-- mettre ici le code -->

<?php 
    $nom = "Marc";
    $note = [ 12, 15, 13, 7, 18];
    $nom2 = "Mathieu";
    $note2 = [ 11, 14, 10, 4, 20, 8, 2];

    $moyenneNote = array_sum($note)/count($note);
    echo "La note moyenne de $nom est de $moyenneNote<br/>";
    
    $moyenneNote2 = array_sum($note2)/count($note2);
    echo "La note moyenne de $nom2 est de $moyenneNote2<br/>";

?>


<?php
/************************
 * NE PAS MODIFIER
 * PERMET d INCLURE LE MENU ET LE TEMPLATE
 ************************/
    $content = ob_get_clean();
    require "../../global/common/template.php";
?>
