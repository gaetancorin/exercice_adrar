<?php ob_start(); //NE PAS MODIFIER 
$titre = "Exo 9 :  Les tableaux"; //Mettre le nom du titre de la page que vous voulez
?>

<!-- mettre ici le code -->

<?php 
    
    $hommes = ["Marion","Geralt","Link","Shepard"];
    $femmes = ["Zelda","Triss","Peach"];

    foreach ($hommes as $key => $value){
        echo "$key : $value";
        echo "<br/>";
    }

    echo "************<br/>";

    foreach ($femmes as $key => $value){
        echo "$key : $value";
        echo "<br/>";
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
