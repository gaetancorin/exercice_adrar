<!-- La variable title pour le layout -->
<?php $title = "Le blog de l'AVBN"; ?>

<!-- ob_start() indique le début de ob -->
<?php ob_start(); ?>

	<h1>Le super blog de l'AVBN !</h1>
	<p>Derniers billets du blog :</p>

	<?php
	foreach ($posts as $post) {
	?>
		<div class="news">
			<h3> 
				<?= htmlspecialchars($post['title']); ?>
				<em>le <?= $post['french_creation_date']; ?></em>
			</h3>
			<p>
				<?= nl2br(htmlspecialchars($post['content'])); ?>
				<br />
				<em><a href="./?action=post&id=<?= urlencode($post['identifier']) ?>">Commentaires</a></em>
			</p>
		</div>
	<?php
	} // end of the loop
	?>
<!-- ob_get_clean() récupère tout le html entre lui et ob_start() situé avant lui(get).
l'html n'est plus visible par l'utilisateur(clean). 
Si il est assigné à une variable, la variable récupère tout le html. -->
<?php $content = ob_get_clean(); ?>
<!-- La variable title et content ont leurs valeurs, on affiche donc le layout -->
<?php require('layout.php') ?>
