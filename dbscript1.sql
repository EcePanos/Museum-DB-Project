-- MySQL Script generated by MySQL Workbench
-- 05/10/15 15:14:43
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Room`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Room` (
  `idRoom` INT NOT NULL,
  `Theme` VARCHAR(45) NULL,
  PRIMARY KEY (`idRoom`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Artist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Artist` (
  `idArtist` INT NOT NULL,
  `F_Name` VARCHAR(45) NULL,
  `L_Name` VARCHAR(45) NULL,
  `Age` INT NULL CHECK (`Age` BETWEEN 18 AND 65),
  `Address` VARCHAR(45) NULL,
  `Phone` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NULL,
  PRIMARY KEY (`idArtist`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Employee` (
  `idEmployee` INT NOT NULL,
  `F_Name` VARCHAR(45) NULL,
  `L_Name` VARCHAR(45) NULL,
  `Age` INT NULL CHECK (`Age` BETWEEN 18 AND 65),
  `Salary` DECIMAL(7,2) NULL CHECK( `Salary`=-1 OR `Salary`>0),
  `Position` VARCHAR(45) NULL 
	CHECK (`Position` IN ('Maintenance','Supervision','Guide')) ,
  `Adress` VARCHAR(45) NULL,
  `Phone` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NULL,
  PRIMARY KEY (`idEmployee`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Artwork`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Artwork` (
  `idArtwork` INT NOT NULL,
  `Type` VARCHAR(45) NULL CHECK (`Type` IN('Painting','Sculpture','Artifact')),
  `Style` VARCHAR(45) NULL,
  `Name` VARCHAR(45) NULL,
  `Creation_Date` DATE,
  `Artist_idArtist` INT NOT NULL,
  `Room_idRoom` INT NOT NULL,
  `Employee_idEmployee` INT NOT NULL,
  PRIMARY KEY (`idArtwork`, `Artist_idArtist`, `Room_idRoom`, `Employee_idEmployee`),
  INDEX `fk_Artwork_Artist_idx` (`Artist_idArtist` ASC),
  INDEX `fk_Artwork_Room1_idx` (`Room_idRoom` ASC),
  INDEX `fk_Artwork_Employee1_idx` (`Employee_idEmployee` ASC),
  CONSTRAINT `fk_Artwork_Artist`
    FOREIGN KEY (`Artist_idArtist`)
    REFERENCES `mydb`.`Artist` (`idArtist`),
  CONSTRAINT `fk_Artwork_Room1`
    FOREIGN KEY (`Room_idRoom`)
    REFERENCES `mydb`.`Room` (`idRoom`),
  CONSTRAINT `fk_Artwork_Employee1`
    FOREIGN KEY (`Employee_idEmployee`)
    REFERENCES `mydb`.`Employee` (`idEmployee`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Supplier`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Supplier` (
  `idSupplier` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Location` VARCHAR(45) NULL,
  `Type` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NULL,
  `Phone` VARCHAR(45) NULL,
  PRIMARY KEY (`idSupplier`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Visitor_Group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Visitor_Group` (
  `idVisitor_Group` INT NOT NULL,
  `Number_Of_People` INT NULL CHECK(`Number_Of_People`>0),
  `Arrival_Date` DATE NULL,
  `Fee` DECIMAL(5,2) NULL CHECK(`Fee`>0),
  `Type` VARCHAR(45) NULL,
  `Employee_idEmployee` INT NOT NULL,
  PRIMARY KEY (`idVisitor_Group`, `Employee_idEmployee`),
  INDEX `fk_Visitor_Group_Employee1_idx` (`Employee_idEmployee` ASC),
  CONSTRAINT `fk_Visitor_Group_Employee1`
    FOREIGN KEY (`Employee_idEmployee`)
    REFERENCES `mydb`.`Employee` (`idEmployee`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Supplier_Equips_Room`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Supplier_Equips_Room` (
  `Room_idRoom` INT NOT NULL,
  `Supplier_idSupplier` INT NOT NULL,
  `Type` VARCHAR(45) NULL,
  `Quantity` FLOAT NULL CHECK(`Quantity`>0),
  `Date` DATE,
  PRIMARY KEY (`Room_idRoom`, `Supplier_idSupplier`),
  INDEX `fk_Room_has_Supplier_Supplier1_idx` (`Supplier_idSupplier` ASC),
  INDEX `fk_Room_has_Supplier_Room1_idx` (`Room_idRoom` ASC),
  CONSTRAINT `fk_Room_has_Supplier_Room1`
    FOREIGN KEY (`Room_idRoom`)
    REFERENCES `mydb`.`Room` (`idRoom`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Room_has_Supplier_Supplier1`
    FOREIGN KEY (`Supplier_idSupplier`)
    REFERENCES `mydb`.`Supplier` (`idSupplier`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Employee_Assigned_To_Room`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Employee_Assigned_To_Room` (
  `Room_idRoom` INT NOT NULL,
  `Employee_idEmployee` INT NOT NULL,
  `Hours` INT NULL CHECK(`Hours`>0),
  PRIMARY KEY (`Room_idRoom`, `Employee_idEmployee`),
  INDEX `fk_Room_has_Employee_Employee1_idx` (`Employee_idEmployee` ASC),
  INDEX `fk_Room_has_Employee_Room1_idx` (`Room_idRoom` ASC),
  CONSTRAINT `fk_Room_has_Employee_Room1`
    FOREIGN KEY (`Room_idRoom`)
    REFERENCES `mydb`.`Room` (`idRoom`),
  CONSTRAINT `fk_Room_has_Employee_Employee1`
    FOREIGN KEY (`Employee_idEmployee`)
    REFERENCES `mydb`.`Employee` (`idEmployee`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
