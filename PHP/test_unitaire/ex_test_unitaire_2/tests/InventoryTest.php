<?php
    use PHPUnit\Framework\TestCase;

    class InventoryTest extends TestCase{
        public function testRolesCanbeSet(){
            $mockRepo = $this->createMock(\App\RoleRepository::class);
            $roleInventory = new \App\Inventory($mockRepo);
            $mockRolesArray = [
                ['id_role' => 1, 'name_role' =>'administrateur'],
                ['id_role' => 2, 'name_role' =>'modérateur'],
                ['id_role' => 3, 'name_role' =>'membre']
            ];
            $mockRepo->method('fetchRoles')->willReturn($mockRolesArray);

            $roleInventory->setRoles();
            $this->assertEquals('administrateur', $roleInventory->getRoles()[0]['name_role']);
            $roleInventory->setRoles();
            $this->assertEquals('membre', $roleInventory->getRoles()[2]['name_role']);
        }
    }