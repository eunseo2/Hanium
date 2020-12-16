-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema park
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema park
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `park` DEFAULT CHARACTER SET utf8 ;
USE `park` ;

-- -----------------------------------------------------
-- Table `park`.`parking`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `park`.`parking` (
  `parking_area_location` INT NOT NULL,
  `car_num` VARCHAR(20) NOT NULL,
  `entrance_time` DATETIME NOT NULL,
  `exit_time` DATETIME NOT NULL,
  `total_time` INT NULL,
  PRIMARY KEY (`parking_area_location`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `park`.`parking_area`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `park`.`parking_area` (
  `car_num` VARCHAR(20) NOT NULL,
  `parking_area_location` VARCHAR(20) NOT NULL,
  `parking_car_type` INT NULL,
  `img_path` TEXT NULL,
  PRIMARY KEY (`car_num`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `park`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `park`.`user` (
  `user_code` INT NOT NULL AUTO_INCREMENT, 
  `user_id` VARCHAR(45) NOT NULL,
  `user_name` VARCHAR(20) NOT NULL,
  `user_pw` VARCHAR(32) NOT NULL,
  `car_num` VARCHAR(20) NOT NULL,
  `user_phone` VARCHAR(20) NOT NULL),               PRIMARY KEY('user_code'));


-- -----------------------------------------------------
-- Table `park`.`timestamps`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `park`.`timestamps` (
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `img_path` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`img_path`));


-- -----------------------------------------------------
-- Table `park`.`resident`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `park`.`resident` (
  `resident_code` INT NOT NULL AUTO_INCREMENT, 
  `car_num` VARCHAR(20) NOT NULL,
  `name` VARCHAR(20) NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `address` TEXT NOT NULL,
  `car_type` INT NOT NULL,
  PRIMARY KEY (`resident_code`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `park`.`resident_long_term_parking`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `park`.`resident_long_term_parking` (
  `resident_code` INT NOT NULL,
  `car_num` VARCHAR(45) NOT NULL,
  `total_time` INT NOT NULL,
  PRIMARY KEY (`resident_code`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `park`.`manager`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `park`.`manager` (
  `code` INT NOT NULL AUTO_INCREMENT,
  `pw` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`code`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

# 주의할점
## 명명규칙 테이블 이름에 -가 들어가면 insert삽입이 안되니까 주의하기!
