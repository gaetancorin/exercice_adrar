<?php ob_start(); //NE PAS MODIFIER 
$titre = "Exo 14 :   BONUS – Tableaux
complexes"; //Mettre le nom du titre de la page que vous voulez
?>

<!-- mettre ici le code -->

<?php 


$personne1 = [
    "Nom" => "Chris",
    "Age" => "35",
    "Sexe" => True, 
    "Note" => [ 12, 15, 13, 7],
 ];
 $personne2 = [
     "Nom" => "Claire",
     "Age" => "32",
     "Sexe" => False, 
     "Note" => [ 11, 9, 7, 4],
  ];
  $personne3 = [
    "Nom" => "Pierre",
    "Age" => "54",
    "Sexe" => True,
    "Note" => [ 8, 21, 0, 3],
 ];
 $personne4 = [
    "Nom" => "Sophie",
    "Age" => "99",
    "Sexe" => False,
    "Note" => [ 0, 5, 3, 847],
 ];

 $personneTotal = [];
array_push($personneTotal, $personne1, $personne2, $personne3, $personne4);

for ($i=0; $i < count($personneTotal); $i++){
    readArray($personneTotal[$i]);
}
 //  echo $personne1["Nom"];
//   readArray($personne1);
//   readArray($personne2);
 
 function readArray($personne){
    echo "Nom : $personne[Nom]<br/>";
    echo "Age : $personne[Age]<br/>";
    echo "Sexe : ";
    if ($personne["Sexe"]){
        echo "Homme<br/>";
    }
    else{
        echo "Femme<br/>";
    }
    for ($i=0; $i < count($personne["Note"]); $i++){
        $numeroNote = $i+1;
        echo "Note : ".$numeroNote." : ".$personne["Note"][$i]."<br/>";
    }
    $noteMoyenne = moyenne($personne["Note"]);
    echo "La moyenne est de $noteMoyenne<br/>****************<br/>";

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
