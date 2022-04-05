<?php
class User{
    public $id_user;
    public $name;
    public $first_name;
    public $mail;
    public $password;
    public $id_role;
    public $connect;

    public function __construct(){
        $this->connect = myConnection();
    }

    public function getSingleUser(){
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
                ':mail' => $this ->mail
            )
        );
        return $req;
    }

    public function createUser(){
        echo("a voir plus tard");
    }

}
?>