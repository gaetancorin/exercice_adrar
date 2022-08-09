<?php

namespace Application\Controllers\Comment;

require_once('src/lib/database.php');
require_once('src/model/comment.php');

use Application\Lib\Database\DatabaseConnection;
use Application\Model\Comment\CommentRepository;

class Comment{

	function execute(string $identifier){

		$databaseConnection = new DatabaseConnection();

		$commentRepository = new CommentRepository();
		$commentRepository->connection = $databaseConnection;

		$comment = $commentRepository->getComment($identifier);

		require('templates/comment.php');
	}

}