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
    `Deadline` date NOT NULL,
	constraint Role_PK primary key (`Role_Name`)
);

INSERT INTO `Role` VALUES ('IT Support', 'Assit in daily user technical problems and IT equipment maintenence.', '2023-10-25');
INSERT INTO `Role` VALUES ('Clerk', 'Keyboard warrior.', '2023-10-28');
INSERT INTO `Role` VALUES ('Human Resources', 'Any member of the Human Resources team', '2023-11-18');
INSERT INTO `Role` VALUES ('Manager', 'Any manager', '2023-11-05');

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

create table `Staff_Application` (
	`Application_ID` int(10) NOT NULL AUTO_INCREMENT,
	`Staff_ID` int(10) NOT NULL,
    `Role_Name` varchar(20) NOT NULL,
    constraint Staff_Application_PK primary key (`Application_ID`),
    constraint Staff_Application_FK1 foreign key (`Staff_ID`) references `Staff` (`Staff_ID`),
    constraint Staff_Application_FK2 foreign key (`Role_Name`) references `Role` (`Role_Name`)
);

INSERT INTO `Staff_Application` VALUES ('1', 6, 'Clerk');

create table `Staff_Login` (
    `Username` varchar(20) NOT NULL,
    `Password` longtext NOT NULL,
    `Staff_ID` int(10) NOT NULL,
    constraint Staff_Login_PK primary key (`Username`),
    constraint Staff_Login_FK1 foreign key (`Staff_ID`) references `Staff` (`Staff_ID`)
);

INSERT INTO `Staff_Login` VALUES ('staff01', 'staff01password', 6);
INSERT INTO `Staff_Login` VALUES ('jude', 'jude00password', 1);
INSERT INTO `Staff_Login` VALUES ('king', 'king00password', 2);
