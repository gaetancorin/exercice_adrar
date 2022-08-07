<?php
// we connect to database
try
{
      $database = new PDO('mysql:host=localhost;dbname=mvc_php_openclassroom;charset=utf8', 'root', '');
}
catch(Exception $e){
      die( 'Erreur : '.$e->getMessage()   );
}

// we retrieve the 5 last blog posts
// LA REPONSE A UN QUERY S APPELLE UN STATEMENT
$statement = $database->query(
   'SELECT id, titre, contenu, DATE_FORMAT(date_creation, \'%d/%m/%Y à %Hh%imin%ss\') AS date_creation_fr 
   FROM billets ORDER BY date_creation DESC LIMIT 0, 5'
   );

// CREER UNE LISTE D OBJETS AVEC LES DONNEES PERMET DE FAIRE UN FOREACH DANS LE FRONT
$posts = [];
while ($row = $statement->fetch()) {
   $post = [
      'title' => $row['titre'],
      'french_creation_date' => $row['date_creation_fr'],
      'content' => $row['contenu'],
   ];

   $posts[] = $post;
}

?>

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

      <!-- LA BOUCLE FOREACH GRACE A LA LISTE -->
      <?php
      foreach ($posts as $post){
         ?>
         <div class="news">
            <h3>
               <!-- PERMET DE TRANSFORMER PROPREMENT UNE VARIABLE EN HTML -->
               <?php echo htmlspecialchars($post['title']); ?>
               <em>le <?php echo $post['french_creation_date']; ?></em>
            </h3>
            <p>
               <?php
               // We display the post content
               // NL2BR TRANSFORME LE RETOUR A LA LIGNE EN CHAMP balise html <br>
               // IL FAUT EN BDD AVOIR "\r\n" à l'emplacement des espaces
               //" \r\n car le plus répandu "
               //(-'\n' pour Linux.-'\r\n' pour Windows.-'\r' pour Mac)
               // et un type text
               echo nl2br(htmlspecialchars($post['content']));
               ?>
               <br />
               <em><a href="#">Commentaires</a></em>
            </p>
         </div>
      <?php
      } // end of the poosts loop.
         ?>
   </body>
</html>
