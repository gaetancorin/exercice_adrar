<?php

class exemple extends \PHPUnit\Framework\TestCase{
    public function testThatStringsMatch(){
        $string1 = 'testing';
        $string2 = 'testing';
        $string3 = 'Testing';

        $this->assertSame($string1, $string2);
        // $this->assertSame($string1, $string3);
    }
    public function testThatNumbersMatch(){
        $this->assertSame(10, 5+5);
    }

}
