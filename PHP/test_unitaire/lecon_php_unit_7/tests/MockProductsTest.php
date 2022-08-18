<?php

use PHPUnit\Framework\TestCase;

class MockProductsTest extends TestCase{
    // récupère un tableau vide
    // public function testMockProductsAreReturned(){
    // $mockRepo = $this->createMock(\App\ProductRepository::class);
    // $products = $mockRepo->fetchProducts();
    // var_dump($products);
    // }
    // crée un tableau plein avec de fausses données
    public function testMockProductsAreReturned(){
        $mockRepo = $this->createMock(\App\ProductRepository::class);
        $mockProductsArray = [
            ['id' => 1, 'name' => 'Acme Radio Knobs'],
            ['id' => 2, 'name' => 'Apple Iphone'],
        ];
        $mockRepo->method('fetchProducts')->willReturn($mockProductsArray);
        $products = $mockRepo->fetchProducts();
        // dd($products);
        $this->assertEquals('Acme Radio Knobs', $products[0]['name']);
    }


}