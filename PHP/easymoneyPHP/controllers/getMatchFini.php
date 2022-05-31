<?php 
// Je vérifie si l utilisateur est connecter
if (isset($_SESSION['pseudo'])){
    $pseudo = $_SESSION['pseudo'];
    $connexion=True;
}
else{
    $connexion=False;
}

// Je lis tous les matchs finis
$game = new game();
$games_finis =$game->lire_games_finis();

// lire_games_finis() fournis un tableau ou chaque match représente 2 enregistrements(un pour chaque equipe).
// On utilise un compteur qui s'incrémente, modulo %1 pour séparer les enregistrement 2 par 2(pour séparer chaque match)
$compteur = 0;
$matchs_miser = [];
while($donnees = $games_finis->fetch()){

    if ($compteur == 0){
        $nom_game = $donnees["nom_game"];
        $date_game = $donnees["date_game"];
        $nom_equipe1 = $donnees["nom_equipe"];
        $detail_equipe1 = $donnees["detail_equipe"];
        $point_equipe1 = $donnees["point_equipe"];

        $compteur += 1;     
    }
    else if ($compteur == 1){
        $nom_equipe2 = $donnees["nom_equipe"];
        $detail_equipe2 = $donnees["detail_equipe"];
        $point_equipe2 = $donnees["point_equipe"];

        // je me sert du nom de la game et du nom des equipes
        // pour récupérer le pourcentage total de paris par equipe  
        $game->set_nom_game($nom_game);
        $pourcentage_mise = $game->calcul_pourcentage_miser_total($nom_equipe1,$nom_equipe2);
        $pourcentage_equipe1 = $pourcentage_mise[0];
        $pourcentage_equipe2 = $pourcentage_mise[1];


        if ($connexion){
            // je reinitialise la variable $equipeparier_mise 
            $equipeparier_mise = 0;
            // je recupère la mise et l equipe sur lequel a miser l'utilisateur 
            // uniquement sur ce match
            $myUser = new User();
            $myUser->set_pseudo($pseudo); 
            $equipeparier_mise = $myUser->get_infos_mise($nom_game);
            if (isset($equipeparier_mise['mise'])){
                $nom_equipe_parier = $equipeparier_mise['nom_equipe_parier'];
                $mise = $equipeparier_mise['mise'];
            }
            
        
 
        }
        


        // Une fois toutes les informations dans des variables, je le met dans un tableau associatif
        if (isset($equipeparier_mise['mise'])){
            $match = [
                'nom_game' => $nom_game, 
                'date_game' => $date_game, 
                'nom_equipe1' => $nom_equipe1,
                'detail_equipe1' => $detail_equipe1,
                'point_equipe1' => $point_equipe1,
                'pourcentage_equipe1' => $pourcentage_equipe1,
                'nom_equipe2' => $nom_equipe2,
                'detail_equipe2' => $detail_equipe2,           
                'point_equipe2' => $point_equipe2,
                'pourcentage_equipe2' => $pourcentage_equipe2,
                'nom_equipe_parier' => $nom_equipe_parier,
                'mise' =>  $mise,
            ];
        }
        else{
            $match = [
                'nom_game' => $nom_game, 
                'date_game' => $date_game, 
                'nom_equipe1' => $nom_equipe1,
                'detail_equipe1' => $detail_equipe1,
                'point_equipe1' => $point_equipe1,
                'pourcentage_equipe1' => $pourcentage_equipe1,
                'nom_equipe2' => $nom_equipe2,
                'detail_equipe2' => $detail_equipe2,           
                'point_equipe2' => $point_equipe2,
                'pourcentage_equipe2' => $pourcentage_equipe2,

                ];
        }

        // Puis je met ce tableau dans un autre tableau contenant tous les matchs futur
        array_push($matchs_miser, $match);

        //Je modulo pour passer au match suivant
        $compteur = $compteur%1;
    }
}

// je souhaite récupérer la date sur le dernier match fini
// echo $matchs[0]["date_game"];

echo '<ul class="tilesWrap">';
for ($i=0; $i< 5; $i++){
    echo'<li>
		<h2>'.$matchs_miser[$i]["date_game"].'</h2>
		<h4> '.$matchs_miser[$i]["nom_equipe1"].' Vs '.$matchs_miser[$i]["nom_equipe2"].'</h3>
		<p>'.$matchs_miser[$i]["detail_equipe1"].' face à '. $matchs_miser[$i]["detail_equipe2"].'</p>
        <p>'.$matchs_miser[$i]["point_equipe1"].' pour les '.$matchs_miser[$i]["nom_equipe1"].'<br>'
        .$matchs_miser[$i]["point_equipe2"].' pour les '.$matchs_miser[$i]["nom_equipe2"].'</p></br>
		<p>
			'.$matchs_miser[$i]['pourcentage_equipe1'].'% miser contre '. $matchs_miser[$i]['pourcentage_equipe2'].'%
		</p>';
        if (isset(($matchs_miser[$i]['mise']))){
            echo '<p>Tu as misé '.$matchs_miser[$i]['mise'].' euros pour '.$matchs_miser[$i]['nom_equipe_parier'].'</p>';
        }
	echo '</li>';

}
echo '</ul>';

?>