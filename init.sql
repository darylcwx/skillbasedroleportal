# Client name: All-In-One (AIO)
# Project name: Skill Based Role Portal

# clear start for database
drop database if exists SBRP_Ais_Kachang;
create database SBRP_Ais_Kachang;
use SBRP_Ais_Kachang;

# ================== Created based on Project Specification ================== 
# Can create more properties as needed for the project.
# To add more dummy data for testing purposes.

create table `Staff` (
	`Staff_ID` int(10) NOT NULL AUTO_INCREMENT,
	`Staff_FName` varchar(50) NOT NULL,
	`Staff_LName` varchar(50) NOT NULL,
	`Dept` varchar(50) NOT NULL,
	`Email` varchar(50) NOT NULL,
	`Access_Rights` int(2) NOT NULL, # 0 = admin, 1 = user, 2 = manager
	constraint Staff_PK primary key (`Staff_ID`)
);

insert into `Staff` values(1, 'Jude', 'Smith', 'IT', 'jude.smith@aio.com', 0) ;
insert into `Staff` values(2, 'King', 'Kong', 'HR', 'king.kong@aio.com', 1) ;
insert into `Staff` values(3, 'John', 'Smith', 'IT', 'john.smith@aio.com', 1) ;
insert into `Staff` values(4, 'Little', 'Tip', 'Finance', 'little.tip@aio.com', 2) ;
insert into `Staff` values(5, 'Chicken', 'Ninja', 'HR', 'chicken.ninja@aio.com', 2) ;
insert into `Staff` values(6, 'staff', '01', 'IT', 'staff.01@aio.com', 1) ;

create table `Role` (
	`Role_Name` varchar(20) NOT NULL,
	`Role_Desc` longtext NOT NULL,
	constraint Role_PK primary key (`Role_Name`)
);

INSERT INTO `Role` VALUES ('IT Support', 'Assit in daily user technical problems and IT equipment maintenence.');
INSERT INTO `Role` VALUES ('Clerk', 'Keyboard warrior.');
INSERT INTO `Role` VALUES ('Human Resources', 'Any member of the Human Resources team');
INSERT INTO `Role` VALUES ('Manager', 'Any manager');

create table `Role_Skill` (
	`Role_Name` varchar(20) NOT NULL,
	`Skill_Name` varchar(50) NOT NULL,
	constraint Role_Skill_PK primary key (`Skill_Name`),
	constraint Role_Skill_FK1 foreign key (`Role_Name`) references `Role` (`Role_Name`)
);

create table `Staff_Skill` (
	`Staff_ID` int(10) NOT NULL,
	`Skill_Name` varchar(50) NOT NULL,
	`Skill_Profile_Desc` longtext NULL,
	constraint Staff_Skill_PK primary key (`Staff_ID`, `Skill_Name`),
	constraint Staff_Skill_FK1 foreign key (`Staff_ID`) references `Staff` (`Staff_ID`),
	constraint Staff_Skill_FK2 foreign key (`Skill_Name`) references `Role_Skill` (`Skill_Name`)
);

create table `Listings` (
	`listing_ID` int(10) NOT NULL AUTO_INCREMENT,
    `Role_Name` varchar(20) NOT NULL,
	`Deadline` date NOT NULL,
    constraint Listings_PK primary key (`listing_ID`),
    constraint Listings_FK foreign key (`Role_Name`) references `Role` (`Role_Name`)
);

insert into `Listings` values (1, 'IT Support', '2023-10-25');
insert into `Listings` values (1, 'Clerk', '2023-10-28');
insert into `Listings` values (1, 'Human Resources', '2023-11-18');
insert into `Listings` values (1, 'Manager', '2023-11-05');

create table `Staff_Application` (
	`Application_ID` int(10) NOT NULL AUTO_INCREMENT,
	`Staff_ID` int(10) NOT NULL,
    `listing_ID` int(10) NOT NULL,
    constraint Staff_Application_PK primary key (`Application_ID`),
    constraint Staff_Application_FK1 foreign key (`Staff_ID`) references `Staff` (`Staff_ID`),
    constraint Staff_Application_FK2 foreign key (`listing_ID`) references `Listings` (`listing_ID`)
);

insert into `Staff_Application` values (1, 6, 'Clerk');
insert into `Staff_Application` values (2, 1, 'Human Resources');