/* This file was generated by ODB, object-relational mapping (ORM)
 * compiler for C++.
 */

DROP TABLE IF EXISTS `person`;

CREATE TABLE IF NOT EXISTS `schema_version` (
  `name` VARCHAR(255) NOT NULL PRIMARY KEY,
  `version` BIGINT UNSIGNED NOT NULL,
  `migration` TINYINT(1) NOT NULL)
 ENGINE=InnoDB;

DELETE FROM `schema_version`
  WHERE `name` = '';

CREATE TABLE `person` (
  `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `version` BIGINT UNSIGNED NOT NULL,
  `first` TEXT NOT NULL,
  `last` TEXT NOT NULL DEFAULT '',
  `age` SMALLINT UNSIGNED NOT NULL,
  `middle_name` TEXT NULL,
  `created_time` TIMESTAMP NOT NULL,
  `updated_time` DATETIME(6) NULL)
 ENGINE=InnoDB;

INSERT IGNORE INTO `schema_version` (
  `name`, `version`, `migration`)
  VALUES ('', 1, 0);
