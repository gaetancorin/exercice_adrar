<?php
    namespace App;
    class Inventory{
        private $roles;
        public function __construct(private RoleRepository $rolesRepo){
        }

        public function setRoles(){
            $this->roles = $this->rolesRepo->fetchRoles();
        }

        public function getRoles(){
            return $this->roles;
        }

    }

?>