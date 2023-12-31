# Client name: All-In-One (AIO)
# Project name: Skill Based Role Portal

# clear start for database
drop database if exists SBRP_Ais_Kachang;
create database SBRP_Ais_Kachang;
use SBRP_Ais_Kachang;

# ================== Created based on Project Specification ================== 

create table `Access_Control` (
	`Access_ID` int NOT NULL,
    `Access_Control_Name` varchar(50) NOT NULL,
    constraint Access_Control_PK primary key (`Access_ID`)
);

create table `Staff` (
	`Staff_ID` int NOT NULL AUTO_INCREMENT,
	`Staff_FName` varchar(50) NOT NULL,
	`Staff_LName` varchar(50) NOT NULL,
	`Dept` varchar(50) NOT NULL,
    `Country` text NOT NULL,
	`Email` varchar(50) NOT NULL,
	`Role` int NOT NULL,
	constraint Staff_PK primary key (`Staff_ID`),
    constraint Staff_FK1 foreign key (`Role`) references `Access_Control` (`Access_ID`)
);

create table `Role` (
	`Role_Name` varchar(50) NOT NULL,
	`Role_Desc` longtext NOT NULL,
	constraint Role_PK primary key (`Role_Name`)
);

create table `Skill` (
	`Skill_Name` varchar(50) NOT NULL,
    `Skill_Desc` longtext NOT NULL,
    constraint Skill_PK primary key (`Skill_Name`)
);

create table `Role_Skill` (
	`Role_Name` varchar(50) NOT NULL,
	`Skill_Name` varchar(50) NOT NULL,
	constraint Role_Skill_PK primary key (`Role_Name`, `Skill_Name`),
	constraint Role_Skill_FK1 foreign key (`Role_Name`) references `Role` (`Role_Name`),
    constraint Role_Skill_FK2 foreign key (`Skill_Name`) references `Skill` (`Skill_Name`)
);

create table `Staff_Skill` (
	`Staff_ID` int NOT NULL,
	`Skill_Name` varchar(50) NOT NULL,
	`Skill_Profile_Desc` longtext NULL,
	constraint Staff_Skill_PK primary key (`Staff_ID`, `Skill_Name`),
	constraint Staff_Skill_FK1 foreign key (`Staff_ID`) references `Staff` (`Staff_ID`),
	constraint Staff_Skill_FK2 foreign key (`Skill_Name`) references `Skill` (`Skill_Name`)
);

create table `Listings` (
	`listing_ID` int NOT NULL AUTO_INCREMENT,
    `Role_Name` varchar(50) NOT NULL,
	`Deadline` date NOT NULL,
    constraint Listings_PK primary key (`listing_ID`),
    constraint Listings_FK foreign key (`Role_Name`) references `Role` (`Role_Name`)
);

create table `Staff_Application` (
	`Application_ID` int NOT NULL AUTO_INCREMENT,
	`Staff_ID` int NOT NULL,
    `listing_ID` int NOT NULL,
    constraint Staff_Application_PK primary key (`Application_ID`),
    constraint Staff_Application_FK1 foreign key (`Staff_ID`) references `Staff` (`Staff_ID`),
    constraint Staff_Application_FK2 foreign key (`listing_ID`) references `Listings` (`listing_ID`)
);