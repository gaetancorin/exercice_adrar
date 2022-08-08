<?php
// controllers/post.php
require_once('src/lib/database.php');
require_once('src/model/post.php');
require_once('src/model/comment.php');

use Application\Model\Post\PostRepository;

function post(string $identifier)
{

	$databaseConnection = new DatabaseConnection();

	$postRepository = new PostRepository();
	$postRepository->connection = $databaseConnection;
	$post = $postRepository->getPost($identifier);

	$commentRepository = new CommentRepository();
	$commentRepository->connection = $databaseConnection;
	$comments = $commentRepository->getComments($identifier);

	require('templates/post.php');
}