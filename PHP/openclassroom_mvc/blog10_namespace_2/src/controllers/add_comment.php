<?php

namespace Application\Controllers\Add_comment;

require_once('src/lib/database.php');
require_once('src/model/comment.php');

use Application\Lib\Database\DatabaseConnection;
use Application\Model\Comment\CommentRepository;

class AddComment{

	function execute(string $post, array $input){

		$author = null;
		$comment = null;
		if (!empty($input['author']) && !empty($input['comment'])) {
			$author = $input['author'];
			$comment = $input['comment'];
		} else {
			throw new \Exception('Les données du formulaire sont invalides.');
		}

		$commentRepository = new CommentRepository();
		$databaseConnection = new DatabaseConnection();
		$commentRepository->connection = $databaseConnection;

		$success = $commentRepository->createComment($post, $author, $comment);
		if (!$success) {
			throw new \Exception('Impossible d\'ajouter le commentaire !');
		} else {
			header('Location: index.php?action=post&id=' . $post);
		}
	}

}