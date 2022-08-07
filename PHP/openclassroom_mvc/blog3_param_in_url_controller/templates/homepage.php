<!DOCTYPE html>
<html>
	<head>
    	<meta charset="utf-8" />
    	<title>Le blog de l'AVBN</title>
    	<link href="style.css" rel="stylesheet" />
	</head>

	<body>
    	<h1>Le super blog de l'AVBN !!</h1>
    	<p>Derniers billets du blog :</p>

    	<?php
    	foreach ($posts as $post) {
    	?>
        	<div class="news">
            	<h3> 
            <!-- On utilise un "short echo tags" 
               < ?php echo VARIABLE ?> est remplacé par
               < ?= VARIABLE ?>
                   -->
                	<?= htmlspecialchars($post['title']); ?>
                	<em>le <?= $post['french_creation_date']; ?></em>
            	</h3>
            	<p>
                	<?= nl2br(htmlspecialchars($post['content'])); ?>
                	<br />
					<!-- urlencode(variable) permet de passé une variable a l'url
					il doit être utilisé avant ?id= de la méthode GET pour donner un paramètre get à l'url d'arrivé
					 -->
                	<em><a href="post.php?id=<?= urlencode($post['identifier']) ?>">Commentaires</a></em>
            	</p>
        	</div>
    	<?php
    	} // end of the loop
    	?>
	</body>
</html>