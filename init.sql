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

INSERT INTO `Role` VALUES ('IT Support', 'Assist in daily user technical problems and IT equipment maintenence.');
INSERT INTO `Role` VALUES ('Clerk', 'Keyboard warrior.');
INSERT INTO `Role` VALUES ('Human Resources', 'Any member of the Human Resources team');
INSERT INTO `Role` VALUES ('Manager', 'Any manager');

create table `Role_Skill` (
	`Role_Name` varchar(20) NOT NULL,
	`Skill_Name` varchar(50) NOT NULL,
	constraint Role_Skill_PK primary key (`Skill_Name`),
	constraint Role_Skill_FK1 foreign key (`Role_Name`) references `Role` (`Role_Name`)
);

INSERT INTO `Role_Skill` (`Role_Name`, `Skill_Name`) VALUES
('IT Support', 'Networking'),
('IT Support', 'Hardware Troubleshooting'),
('IT Support', 'Software Installation and Configuration');

INSERT INTO `Role_Skill` (`Role_Name`, `Skill_Name`) VALUES
('Clerk', 'Computer Proficiency'),
('IT Support', 'Time Management'),
('IT Support', 'Attention to Detail');

INSERT INTO `Role_Skill` (`Role_Name`, `Skill_Name`) VALUES
('Human Resource', 'Performance Management'),
('IT Support', 'Employment Law Compliance'),
('IT Support', 'Conflict Resolution');

INSERT INTO `Role_Skill` (`Role_Name`, `Skill_Name`) VALUES
('Manager', 'Project Management'),
('IT Support', 'Strategic Planning'),
('IT Support', 'Leadership and Team Management');

CREATE TABLE `Staff_Skill` (
    `Staff_ID` int(10) NOT NULL,
    `Skill_Name` varchar(50) NOT NULL,
    CONSTRAINT `Staff_Skill_PK` PRIMARY KEY (`Staff_ID`, `Skill_Name`),
    CONSTRAINT `Staff_Skill_FK1` FOREIGN KEY (`Staff_ID`) REFERENCES `Staff` (`Staff_ID`),
    CONSTRAINT `Staff_Skill_FK2` FOREIGN KEY (`Skill_Name`) REFERENCES `Skills` (`Skill_Name`)
);

-- Insert staff skills for Staff_ID 1
INSERT INTO `Staff_Skill` (`Staff_ID`, `Skill_Name`)
VALUES
(1, 'Networking'),
(1, 'Hardware Troubleshooting'),
(1, 'Software Installation and Configuration');

-- Insert staff skills for Staff_ID 2
INSERT INTO `Staff_Skill` (`Staff_ID`, `Skill_Name`)
VALUES
(2, 'Computer Proficiency'),
(2, 'Time Management'),
(2, 'Attention to Detail');

-- Insert staff skills for Staff_ID 3
INSERT INTO `Staff_Skill` (`Staff_ID`, `Skill_Name`)
VALUES
(3, 'Performance Management'),
(3, 'Employment Law Compliance'),
(3, 'Conflict Resolution');

-- Insert staff skills for Staff_ID 4
INSERT INTO `Staff_Skill` (`Staff_ID`, `Skill_Name`)
VALUES
(4, 'Project Management'),
(4, 'Strategic Planning'),
(4, 'Leadership and Team Management');

-- Insert staff skills for Staff_ID 5
INSERT INTO `Staff_Skill` (`Staff_ID`, `Skill_Name`)
VALUES
(5, 'Networking'),
(5, 'Hardware Troubleshooting'),
(5, 'Software Installation and Configuration');

-- Insert staff skills for Staff_ID 6
INSERT INTO `Staff_Skill` (`Staff_ID`, `Skill_Name`)
VALUES
(6, 'Computer Proficiency'),
(6, 'Time Management'),
(6, 'Attention to Detail');


create table `Skills` (
	`Skill_Name` varchar(20) NOT NULL,
	`Skill_Profile_Desc` longtext NULL,
    constraint Staff_Application_PK primary key (`Skill_Name`),
    constraint Staff_Skill_FK2 foreign key (`Skill_Name`) references `Role_Skill` (`Skill_Name`)
);


INSERT INTO `Skills` VALUES ('Hardware Troubleshooting', 'Skill in diagnosing and resolving hardware-related issues on desktops, laptops, printers, and other peripherals');
INSERT INTO `Skills` VALUES ('Software Installation and Configuration', 'Proficiency in installing, configuring, and updating software applications and operating systems');
INSERT INTO `Skills` VALUES ('Network Troubleshooting', 'Ability to identify and resolve network connectivity issues, including LAN and WAN problems, IP configuration, and DNS troubleshooting');
INSERT INTO `Skills` VALUES ('Computer Proficiency', 'Familiarity with common office software such as Microsoft Office or Google Workspace');
INSERT INTO `Skills` VALUES ('Time Management', 'Skill in effectively managing time to prioritize tasks and meet deadlines');
INSERT INTO `Skills` VALUES ('Attention to Detail', 'Ability to focus on the accuracy and completeness of tasks');
INSERT INTO `Skills` VALUES ('Conflict Resolution', 'Skill in resolving workplace conflicts and disputes');
INSERT INTO `Skills` VALUES ('Employment Law Compliance', 'Understanding of labor laws and regulations');
INSERT INTO `Skills` VALUES ('Performance Management', 'Experience in evaluating employee performance and providing feedback');
INSERT INTO `Skills` VALUES ('Leadership and Team Management', 'Ability to lead and manage teams to achieve organizational goals');
INSERT INTO `Skills` VALUES ('Strategic Planning', 'Skill in creating and executing strategic plans');
INSERT INTO `Skills` VALUES ('Project Management', 'Experience in overseeing and successfully completing projects');

create table `Listings` (
	`listing_ID` int(10) NOT NULL AUTO_INCREMENT,
    `Role_Name` varchar(20) NOT NULL,
	`Deadline` date NOT NULL,
    constraint Listings_PK primary key (`listing_ID`),
    constraint Listings_FK foreign key (`Role_Name`) references `Role` (`Role_Name`)
);

insert into `Listings` values (1, 'IT Support', '2023-10-25');
insert into `Listings` values (2, 'Clerk', '2023-10-28');
insert into `Listings` values (3, 'Human Resources', '2023-11-18');
insert into `Listings` values (4, 'Manager', '2023-11-05');

create table `Staff_Application` (
	`Application_ID` int(10) NOT NULL AUTO_INCREMENT,
	`Staff_ID` int(10) NOT NULL,
    `listing_ID` int(10) NOT NULL,
    constraint Staff_Application_PK primary key (`Application_ID`),
    constraint Staff_Application_FK1 foreign key (`Staff_ID`) references `Staff` (`Staff_ID`),
    constraint Staff_Application_FK2 foreign key (`listing_ID`) references `Listings` (`listing_ID`)
);

insert into `Staff_Application` values (1, 6, 2);
insert into `Staff_Application` values (2, 1, 3);