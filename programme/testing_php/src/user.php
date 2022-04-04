<?php

namespace Encaps;

class User{
    public $name;
    public static $addToString = " est mon prénom.";

    public function fullAnswer(){
        return $this->name.self::$addToString;
    }
}
?>