<?php
// index.php

require_once('src/controllers/add_comment.php');
require_once('src/controllers/homepage.php');
require_once('src/controllers/post.php');

use Application\Controllers\Homepage\Homepage;
use Application\Controllers\Post\Post;
use Application\Controllers\Add_comment\Addcomment;

try {
	if (isset($_GET['action']) && $_GET['action'] !== '') {
    	if ($_GET['action'] === 'post') {
        	if (isset($_GET['id']) && $_GET['id'] > 0) {
            	$identifier = $_GET['id'];

				(new Post())->execute($identifier);
        	} else {
            	throw new Exception('Aucun identifiant de billet envoyé');
        	}
    	} elseif ($_GET['action'] === 'addComment') {
        	if (isset($_GET['id']) && $_GET['id'] > 0) {
            	$identifier = $_GET['id'];

				(new addComment())->execute($identifier, $_POST);
            	;
        	} else {
            	throw new Exception('Aucun identifiant de billet envoyé');
        	}
    	} else {
        	throw new Exception("La page que vous recherchez n'existe pas.");
    	}
	} else {
    	(new Homepage())->execute();
	}
} catch (Exception $e) { // S'il y a eu une erreur, alors...
	$errorMessage = $e->getMessage();

	require('templates/error.php');
}