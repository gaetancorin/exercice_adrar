<?php
    namespace App;

    class User{
        public string $name;
        public static $addToString = " est mon prénom.";
        public $nbrChildren;

        public function fullAnswer() :string {
            return $this->name.self::$addToString;
        }

        public function AddtoNbrChildren($nbr){
            $this->nbrChildren += $nbr;
        }
    }
?>