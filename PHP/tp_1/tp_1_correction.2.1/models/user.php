<?php
class User
{
    // attributs par rapport à la bdd
    public $id_user;
    public $name;
    public $first_name;
    public $mail;
    public $password;
    public $id_role;

    // attribut de connexion à la bdd
    public $connect;

    // constructeur
    public function __construct()
    {
        // j'injecte les informations bdd à l'attribut 
        // au moment de l'instanciation d'un utilisateur
        $this->connect = myConnection();
    }

    // méthode qui retourne 1 utilisateur selon son mail avec jointure
    public function getSingleUser()
    {
        $req = $this->connect->prepare(
            'SELECT
                    *
                FROM 
                    users
                JOIN
                    roles
                ON
                    users.id_role = roles.id_role
                WHERE 
                    mail = :mail'
        );
        $req->execute(
            array(
                ':mail' => $this->mail
            )
        );
        return $req;
    }

    // méthode qui va créer un utilisateur dans la BDD
    public function createUser()
    {
        try {
            //
            $maRequete = "INSERT INTO 
                                users 
                            SET 
                                name = :name,
                                first_name = :first_name,
                                mail = :mail,
                                password = :password,
                                id_role = :role";
            $req = $this->connect->prepare($maRequete);
            // pour la partie 2 je stocke le résultat de l'enregistrement dans une variable
            $req->bindParam(':name', $this->name);
            $req->bindParam(':first_name', $this->first_name);
            $req->bindParam(':mail', $this->mail);
            $req->bindParam(':password', $this->password);
            $req->bindParam(':role', $this->id_role);

            return $req->execute();
        } catch (Exception $e) {
            die('Erreur : ' . $e->getMessage());
        }
    }
}
