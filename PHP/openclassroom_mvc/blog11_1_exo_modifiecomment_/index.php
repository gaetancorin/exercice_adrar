<?php
// index.php

require_once('src/controllers/add_comment.php');
require_once('src/controllers/comment.php');
require_once('src/controllers/modifie_comment.php');
require_once('src/controllers/homepage.php');
require_once('src/controllers/post.php');

use Application\Controllers\Homepage\Homepage;
use Application\Controllers\Post\Post;
use Application\Controllers\Add_comment\AddComment;
use Application\Controllers\Comment\Comment;
use Application\Controllers\Modifie_comment\ModifieComment;

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

				(new AddComment())->execute($identifier, $_POST);
            	;
        	} else {
            	throw new Exception('Aucun identifiant de billet envoyé');
        	}
    	} elseif ($_GET['action'] === 'Comment') {
        	if (isset($_GET['id']) && $_GET['id'] > 0) {
            	$identifier = $_GET['id'];

				(new Comment())->execute($identifier);
            	;
        	} else {
            	throw new Exception('Aucun identifiant de billet envoyé');
        	}
    	} elseif ($_GET['action'] === 'modifieComment') {
        	if (isset($_GET['id']) && $_GET['id'] > 0) {
            	$identifier = $_GET['id'];
				$post_id = $_GET['post_id'];

				(new ModifieComment())->execute($identifier,$post_id, $_POST);
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