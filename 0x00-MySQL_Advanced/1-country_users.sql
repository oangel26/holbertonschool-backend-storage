-- Write a SQL script that creates a table users following these requirements:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- country, enumeration of countries: US, CO and TN, never null
-- If the table already exists, your script should not fail

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL UNIQUE,
  `name` varchar(255),
  `country` ENUM ('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
  PRIMARY KEY (`id`)
);
