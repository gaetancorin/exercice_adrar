<?php ob_start(); //NE PAS MODIFIER 
$titre = "Exo 13 :   Tableaux associatifs"; //Mettre le nom du titre de la page que vous voulez
?>

<!-- mettre ici le code -->

<?php 
$personne1 = [
   "Nom" => "Chris",
   "Age" => "35",
   "Sexe" => True, 
];
$personne2 = [
    "Nom" => "Claire",
    "Age" => "32",
    "Sexe" => False, 
 ];

//  echo $personne1["Nom"];
 readArray($personne1);
 readArray($personne2);

function readArray($personne){
echo "Nom : $personne[Nom]<br/>";
echo "Age : $personne[Age]<br/>";
echo "Sexe : ";
if ($personne["Sexe"]){
    echo "Homme<br/><br/><br/>";
}
else{
    echo "Femme<br/><br/><br/>";
}
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
