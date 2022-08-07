<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Le blog de l'AVBN</title>
        <link href="style.css" rel="stylesheet" />
    </head>
 
    <body>
        <h1>Le super blog de l'AVBN !</h1>
        <p><a href="index.php">Retour à la liste des billets</a></p>

        <div class="news">
            <h3>
                <?= htmlspecialchars($post['title']) ?>
                <em>le <?= $post['french_creation_date'] ?></em>
            </h3>
 
            <p>
                <?= nl2br(htmlspecialchars($post['content'])) ?>
            </p>
        </div>
 
        <h2>Commentaires</h2>
 
        <?php
        foreach ($comments as $comment) {
        ?>
        <p><strong><?= htmlspecialchars($comment['author']) ?></strong> le <?= $comment['french_creation_date'] ?></p>
        <p><?= nl2br(htmlspecialchars($comment['comment'])) ?></p>
        <?php
        }
        ?>
        <p>Ajouter un commentaire:</p>
        <form action= "./?action=addcomment&id= <?= urlencode($identifier) ?>" method="POST">
            <label for=auteur>auteur</label>
            <input type="text" name="auteur" id="auteur" maxlength="20">
            <label for=commentaire>commentaire</label>
            <input type="text" name="commentaire" id="commentaire" >
            <input type="submit" name="submit" value="Valider">
        </form>
    </body>
</html>