<?php
    use PHPUnit\Framework\TestCase;

    class MockRolesTest extends TestCase{
        public function testMockRolesAreReturned(){
            $mockRepo = $this->createMock(\App\RoleRepository::class);
            $mockRolesArray = [
                ['id_role' => 1, 'name_role' =>'administrateur'],
                ['id_role' => 2, 'name_role' =>'modérateur'],
                ['id_role' => 3, 'name_role' =>'membre']
            ];
            $mockRepo->method('fetchRoles')->willReturn($mockRolesArray);

            $roles = $mockRepo->fetchRoles();

            $this->assertEquals('modérateur', $roles[1]['name_role']);
        }
    }