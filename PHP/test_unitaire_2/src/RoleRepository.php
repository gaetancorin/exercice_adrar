<?php
        namespace App;
        
        class RoleRepository{
            protected $pdo;

            protected function getPdo(): \PDO{
                if ($this->pdo === null){
                    $option = [
                        \PDO::ATTR_ERRMODE => \PDO::ERRMODE_EXCEPTION,
                        \PDO::ATTR_DEFAULT_FETCH_MODE => \PDO::FETCH_ASSOC
                    ];
                    try {
                        $this->pdo = new \PDO("mysql:host=127.0.0.1;dbname=tplogregshow;charset=utf8mb4", 'root', '', $options);
                    }
                    catch (\PDOException $pdoException){
                        throw new \PDOException($pdoException->getMessage(), $pdoException->getCode());
                    }
                }
                return $this->pdo;
            }
            /**
             * Fetch un tableau de roles à partir de la BDD
             * 
             * @return array
             */
            public function fetchRoles(){
                return $this->getPdo()->prepare('SELECT * FROM roles')->fetchAll(\PDO::FETCH_ASSOC);
            }

        }



?>