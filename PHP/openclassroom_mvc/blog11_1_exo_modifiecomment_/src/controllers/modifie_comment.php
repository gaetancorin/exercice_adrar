<?php

namespace Application\Controllers\Modifie_comment;

require_once('src/lib/database.php');
require_once('src/model/comment.php');

use Application\Lib\Database\DatabaseConnection;
use Application\Model\Comment\CommentRepository;

class ModifieComment{

	function execute(string $identifier,string $post_id, array $input){

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

		$success = $commentRepository->modifieComment($identifier, $author, $comment);
		if (!$success) {
			throw new \Exception('Impossible de modifier le commentaire !');
		} else {
			header('Location: index.php?action=post&id=' . $post_id);
		}
	}

}