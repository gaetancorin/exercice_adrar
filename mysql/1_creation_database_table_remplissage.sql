DROP DATABASE exo1_php;
CREATE DATABASE exo1_php;
use exo1_php;
CREATE TABLE `user`(
user_id INT AUTO_INCREMENT PRIMARY KEY,
user_pseudo VARCHAR(30) NOT NULL,
user_email VARCHAR(50) NOT NULL
);

INSERT INTO user (user_pseudo, user_email)
VALUES ('pierredu31', 'pierredu31@gmail.com'),
('pierredu33', 'pierredu33@gmail.com');