CREATE DATABASE IF NOT EXISTS `Employees` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Employees`;

CREATE TABLE IF NOT EXISTS `Department`(
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`department_name` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
)DEFAULT CHARSET=utf8;
INSERT INTO `Department`(`department_name`)VALUES("Development");
INSERT INTO `Department`(`department_name`)VALUES("Testing");
INSERT INTO `Department`(`department_name`)VALUES("Customer Support");
INSERT INTO `Department`(`department_name`)VALUES("Marketing");

CREATE TABLE IF NOT EXISTS `Employee`(
	`id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(100) NOT NULL,
	`name` varchar(50) NOT NULL,
    `department_id` int(11),
    PRIMARY KEY (`id`),
    FOREIGN KEY (`department_id`) REFERENCES `Department`(`id`)
)DEFAULT CHARSET=utf8;

