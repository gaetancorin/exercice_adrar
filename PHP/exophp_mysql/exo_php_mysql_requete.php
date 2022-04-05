<?php

function requete_findUser($pseudo) {
    $db = connection_BD();
    $sql = "SELECT * FROM user WHERE user_pseudo = :pseudo";
    $req = $db->prepare($sql);
    $req->execute([
        ":pseudo"=>$pseudo
    ]);
    $data = $req->fetchAll(PDO::FETCH_OBJ);
    return $data;
        
}


?>
