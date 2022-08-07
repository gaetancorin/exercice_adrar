<?php

require_once('src/controllers/homepage.php');
require_once('src/controllers/post.php');
require_once('src/controllers/addComment.php');

if (isset($_GET['action']) && $_GET['action'] !== '') {
	if ($_GET['action'] === 'post') {
    	if (isset($_GET['id']) && $_GET['id'] > 0) {
        	$identifier = $_GET['id'];

        	post($identifier);
    	} else {
        	echo 'Erreur : aucun identifiant de billet envoyé';

        	die;
    	}

	}
	else if ($_GET['action'] === 'addcomment') {
		if (isset($_GET['id']) && $_GET['id'] > 0
			&& isset($_POST['auteur']) && $_POST['auteur'] !== ''
			&& isset($_POST['commentaire']) && $_POST['commentaire'] !== ''
			) {
			$identifier = $_GET['id'];
			$auteur = $_POST['auteur'];
			$commentaire = $_POST['commentaire'];

			addComment($identifier, $auteur, $commentaire);
			post($identifier);
		} else {
			echo 'Erreur dans le formulaire';

			die;
		}
	}
	else {
    	echo "Erreur 404 : la page que vous recherchez n'existe pas.";
	}
} else {
	homepage();
}