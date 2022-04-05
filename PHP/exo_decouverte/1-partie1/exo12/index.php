<?php ob_start(); //NE PAS MODIFIER 
$titre = "Exo 12 :  Tableaux et fonctions - 2"; //Mettre le nom du titre de la page que vous voulez
?>

<!-- mettre ici le code -->

<?php 
    $nom = "Marc";
    $note = [ 12, 15, 13, 7, 18];
    $nom2 = "Mathieu";
    $note2 = [ 11, 14, 10, 4, 20, 8, 2];
    $note3 = [];
    array_push($note3, $note, $note2);
    
    for ($i=0; $i < count($note3); $i++){
        $noteMoyenne = moyenne($note3[$i]);
        $element = $i+1;
        echo "La note moyenne du $element ème élément est de $noteMoyenne<br/>";
    }

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
