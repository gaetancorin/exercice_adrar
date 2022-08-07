<?php

require_once('src/model.php');

function addComment(string $identifier, string $auteur, string $commentaire) {
    
	addOneComment($identifier, $auteur, $commentaire);
}