<?php
    use PHPUnit\Framework\TestCase;
    use Encaps\User;
    // require './vendor/user.php';

    class UserTest extends TestCase{

        protected $user;

        protected function setUp():void{
            $this->user = new User();
        }
        /**
         * @test
         */
        public function testConcatenation(){
            
            // $user = new User();
            $this->user->name = "Jonathan";
            $res = $this->user->fullAnswer();

            $this->assertSame("Jonathan est mon prénom.", $res);
        }

         /**
         * @test
         */
        public function changeConcate(){
            // $user = new User();
            User::$addToString = " est le prénom de votre formateur référent.";

            $this->user->name = "Maxime";
            $res = $this->user->fullAnswer();

            $this->assertSame("Maxime est le prénom de votre formateur référent.", $res);
        }
    }