<?php

class InventoryTest extends \PHPUnit\Framework\TestCase {

    public function testProductsCanBeSet(){
        $mockRepo = $this->createMock(\App\ProductRepository::class);
        $inventory = new \App\Inventory($mockRepo);

        $mockProductsArray = [
            ['id' => 1, 'name' => 'Acme Radio Knobs'],
            ['id' => 2, 'name' => 'Apple iPhone'],
        ];
        $mockRepo->method('fetchProducts')->willReturn($mockProductsArray);

        // Do something
        $inventory->setProducts();

        //Make assertions
        $this->assertEquals('Acme Radio Knobs', $inventory->getProducts()[0]['name']);
        $this->assertEquals('Apple iPhone', $inventory->getProducts()[1]['name']);
    }
}