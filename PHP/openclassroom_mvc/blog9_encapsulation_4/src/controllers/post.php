<?php
// controllers/post.php
require_once('src/lib/database.php');
require_once('src/model/post.php');
require_once('src/model/comment.php');

function post(string $identifier)
{
	$postRepository = new PostRepository();
	$commentRepository = new CommentRepository();
	$databaseConnection = new DatabaseConnection();

	$postRepository->connection = $databaseConnection;
	$commentRepository->connection = $databaseConnection;

	$post = $postRepository->getPost($identifier);
	$comments = $commentRepository->getComments($identifier);

	require('templates/post.php');
}