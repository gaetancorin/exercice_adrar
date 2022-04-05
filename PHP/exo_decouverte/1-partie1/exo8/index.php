<?php ob_start(); //NE PAS MODIFIER 
$titre = "Exo 8 :  Les fonctions"; //Mettre le nom du titre de la page que vous voulez
?>

<!-- mettre ici le code -->

<?php 
    $monMot = "Bonjour";


    voyelle($monMot);

    function voyelle($text){
        $nouveauText = $text;
        $nouveauText = preg_replace("/a+/","",$nouveauText);
        $nouveauText = preg_replace("/e+/","",$nouveauText);
        $nouveauText = preg_replace("/i+/","",$nouveauText);
        $nouveauText = preg_replace("/o+/","",$nouveauText);
        $nouveauText = preg_replace("/u+/","",$nouveauText);
        $nouveauText = preg_replace("/y+/","",$nouveauText);
        echo "$text sans voyelle est $nouveauText";
    }
echo "<br/><br/>";

    voyelle2($monMot);

    function voyelle2($text){
        $nouveauText = $text;
        $nouveauText = str_replace(['a','e','i','o','u','y'], '', $nouveauText);
        echo "$text sans voyelle est $nouveauText";
    }

echo "<br/><br/>";

    voyelle3($monMot);

    function voyelle3($text){
        $nouveauText = "";
        $retirer = ["a","e","i","o","u","y"];
        for ($i=0; $i<strlen($text); $i++){
            if(in_array($text[$i],$retirer)){

            }
            else{
                $nouveauText = "{$nouveauText}{$text[$i]}";
            }
        }
        echo "$text sans voyelle est $nouveauText";
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
