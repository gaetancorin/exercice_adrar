<?php
use App\Cart;
use PHPUnit\Framework\TestCase;

class CartTest extends TestCase{
    public function testCorrectNetPriceIsReturned(){

        // require_once('Cart.php');

        $cart = new Cart();
        $cart->price = 10;
        $netPrice = $cart->getNetPrice();

        $this->assertEquals(12, $netPrice);
    }
    /** commentaire **/
    public function test_the_cart_tax_value_can_be_changed_statically(){
        // require_once('Cart.php');
        Cart::$tax = 1.5;

        $cart = new Cart();
        $cart->price = 10;
        $netPrice = $cart->getNetPrice();
        $this->assertEquals(15, $netPrice);
    }
}