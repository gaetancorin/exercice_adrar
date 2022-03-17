<?php

use PHPUnit\Framework\TestCase;

    class ExemplesAssertions extends TestCase{

        /**
         * @test
         */
        public function stringsIdentiques(){
            $string1 = "une string";
            $string2 = "une string";

            $this->assertSame($string1, $string2);
            
        }

        /**
         * @test
         */
        public function intIdentiques(){
            $this->assertEquals(10,5+5);
        }
    }
?>