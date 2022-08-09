<!-- templates/post.php -->

<?php $title = "Le blog de l'AVBN"; ?>

<?php ob_start(); ?>
<h1>Le super blog de l'AVBN !</h1>
<p><a href="index.php">Retour à la liste des billets</a></p>

<div class="news">
	<h3>
    	<?= htmlspecialchars($comment->author) ?>
    	<em>le <?= $comment->frenchCreationDate ?></em>
	</h3>

	<p>
    	<?= nl2br(htmlspecialchars($comment->comment)) ?>
	</p>
</div>

<h2>Modifier le Commentaire</h2>

<form action="index.php?action=modifieComment&id=<?= $comment->identifier ?>&post_id=<?= $comment->post_id ?>" method="post">
   <div>
  	<label for="author">Auteur</label><br />
  	<input type="text" id="author" name="author" />
   </div>
   <div>
  	<label for="comment">Commentaire</label><br />
  	<textarea id="comment" name="comment"></textarea>
   </div>
   <div>
  	<input type="submit" />
   </div>
</form>

<?php $content = ob_get_clean(); ?>

<?php require('layout.php') ?>
