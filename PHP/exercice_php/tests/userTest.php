<?php

use PHPUnit\Framework\TestCase;
use App\User;
// require './vendor/user.php';

    class UserTest extends TestCase{

        protected $user;
        protected function setUp(): void{
            $this->user = new User();
        }

        protected function tearDown(): void{
            User::$addToString = " est mon prénom.";
        }

        /**
         * @test
         */
        public function changeConcatenationOk(){
            User::$addToString = " est le prénom de votre formateur référent.";

            $this->user-> name = "Mathieu";
            
            $res = $this->user->fullAnswer();

            $this->assertSame("Mathieu est le prénom de votre formateur référent.", $res);
        }
        /**@test */
        public function testConcatenationOk(){

            $this->user->name = "Jonathan";
            $res = $this->user->fullAnswer();

            $this->assertSame("Jonathan est mon prénom.", $res);
        }
        /**
         * @test
         */
        public function UneErreurSeraLeveeSiOnTenteDajouterUnNonEntier(){
            try {
                $this->user->nbrChildren = 2;
                $this->user->addToNbrChildren('trois');
                $this->fail('une erreur a du être levée');
            }
            catch(TypeError $error){
                $this->assertStringStartsWith('Encaps\User::addToNbrChildren():', $error->getMessage());
            }
        }
    }

?>