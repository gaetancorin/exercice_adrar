<?php

class Post{
	public string $title;
	public string $frenchCreationDate;
	public string $content;
	public string $identifier;
}

// : array signifie que l'on type le return en tableau
function getPosts() :array
 {
	// We connect to the database.
	$database = dbConnect();
	// We retrieve the 5 last blog posts.
	$statement = $database->query(
    	"SELECT 
			id, title, content, 
			DATE_FORMAT(creation_date, '%d/%m/%Y à %Hh%imin%ss') AS french_creation_date 
		FROM 
			posts 
		ORDER BY creation_date DESC LIMIT 0, 5"
	);
	$posts = [];
	while (($row = $statement->fetch())) {
		$post = new Post;
		$post->title = $row['title'];
        $post->frenchCreationDate = $row['french_creation_date'];
        $post->content = $row['content'];
        $post->identifier = $row['id'];

    	$posts[] = $post;
	}

	return $posts;
}

function getPost($identifier) :Post
{
	$database = dbConnect();
    $statement = $database->prepare(
        "SELECT 
			id, title, content, DATE_FORMAT(creation_date, '%d/%m/%Y à %Hh%imin%ss') AS french_creation_date 
		FROM 
			posts 
		WHERE 
			id = ?"
    );
    $statement->execute([$identifier]);
 
    $row = $statement->fetch();
	$post = new Post;
	$post->title = $row['title'];
	$post->frenchCreationDate = $row['french_creation_date'];
	$post->content = $row['content'];
	$post->identifier = $row['id'];
 
    return $post;
}

function dbConnect(){

	$database = new PDO('mysql:host=localhost;dbname=mvc_php_openclassroom;charset=utf8', 'root', '');

	return $database;
}