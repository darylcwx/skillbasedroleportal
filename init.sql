# Client name: All-In-One (AIO)
# Project name: Skill Based Role Portal

# clear start for database
drop database if exists SBRP_Ais_Kachang;
create database SBRP_Ais_Kachang;
use SBRP_Ais_Kachang;



# ================== Created based on Project Specification ================== 
# Can create more properties as needed for the project.
# To add more dummy data for testing purposes.

-- Staff TABLE
create table `Staff` (
	`Staff_ID` int NOT NULL AUTO_INCREMENT,
	`Staff_FName` varchar(50) NOT NULL,
	`Staff_LName` varchar(50) NOT NULL,
	`Dept` varchar(50) NOT NULL,
	`Email` varchar(50) NOT NULL,
	`Access_Rights` int NOT NULL, # 0 = admin, 1 = user, 2 = manager
	constraint Staff_PK primary key (`Staff_ID`)
);

insert into `Staff` values(1, 'Jude', 'Smith', 'HR', 'jude.smith@aio.com', 0) ;
insert into `Staff` values(2, 'King', 'Kong', 'IT', 'king.kong@aio.com', 1) ;
insert into `Staff` values(3, 'John', 'Smith', 'IT', 'john.smith@aio.com', 1) ;
insert into `Staff` values(4, 'Little', 'Tip', 'Finance', 'little.tip@aio.com', 1) ;
insert into `Staff` values(5, 'Chicken', 'Ninja', 'Management', 'chicken.ninja@aio.com', 2) ;
insert into `Staff` values(6, 'staff', '01', 'IT', 'staff.01@aio.com', 1) ;

-- Role TABLE
create table `Role` (
	`Role_Name` varchar(20) NOT NULL,
	`Role_Desc` longtext NOT NULL,
	constraint Role_PK primary key (`Role_Name`)
);

insert into `Role` values ('IT Support', 'Assist in daily user technical problems and IT equipment maintenance.');
insert into `Role` values ('Clerk', 'Keyboard warrior.');
insert into `Role` values ('Human Resource', 'Any member of the Human Resources team');
insert into `Role` values ('Manager', 'Any manager');

-- Role_Skill TABLE
create table `Role_Skill` (
	`Role_Name` varchar(20) NOT NULL,
	`Skill_Name` varchar(50) NOT NULL,
	constraint Role_Skill_PK primary key (`Skill_Name`),
	constraint Role_Skill_FK1 foreign key (`Role_Name`) references `Role` (`Role_Name`)
);

insert into `Role_Skill` values ('Clerk', 'Excel');
insert into `Role_Skill` values ('Clerk', 'PowerPoint');
insert into `Role_Skill` values ('Clerk', 'Words');
insert into `Role_Skill` values ('Clerk', 'Outlook');

insert into `Role_Skill` values ('IT Support', 'Networking Troubleshooting');
insert into `Role_Skill` values ('IT Support', 'Hardware Troubleshooting');
insert into `Role_Skill` values ('IT Support', 'Software Installation and Configuration');
insert into `Role_Skill` values ('IT Support', 'Computer Proficiency');

insert into `Role_Skill` values ('Human Resource', 'Time Management');
insert into `Role_Skill` values ('Human Resource', 'Attention to Detail');
insert into `Role_Skill` values ('Human Resource', 'Performance Management');
insert into `Role_Skill` values ('Human Resource', 'Employment Law Compliance');

insert into `Role_Skill` values ('Manager', 'Conflict Resolution');
insert into `Role_Skill` values ('Manager', 'Project Management');
insert into `Role_Skill` values ('Manager', 'Strategic Planning');
insert into `Role_Skill` values ('Manager', 'Leadership and Team Management');


-- Staff_Skill TABLE
create table `Staff_Skill` (
	`Staff_ID` int NOT NULL,
	`Skill_Name` varchar(50) NOT NULL,
	`Skill_Profile_Desc` longtext NULL,
	constraint Staff_Skill_PK primary key (`Staff_ID`, `Skill_Name`),
);

INSERT INTO `Staff_Skill` VALUES (1, 'Attention to Detail', 'Known for an exceptional eye for detail, ensuring precision in HR processes.');
INSERT INTO `Staff_Skill` VALUES (1, 'Time Management', 'Efficiently manages time to meet HR teams demands and deadlines.');
INSERT INTO `Staff_Skill` VALUES (1, 'Performance Management', 'Proficient in assessing and enhancing HR team performance.');
INSERT INTO `Staff_Skill` VALUES (1, 'Employment Law Compliance', 'Keeps the HR team compliant with all relevant employment laws and regulations.');
INSERT INTO `Staff_Skill` VALUES (1, 'Computer Proficiency', 'Adept at using various HR software tools to streamline HR processes.');
INSERT INTO `Staff_Skill` VALUES (1, 'Conflict Resolution', 'Experienced in resolving conflicts within the HR team and promoting a collaborative atmosphere.');

INSERT INTO `Staff_Skill` VALUES (2, 'Networking Troubleshooting', 'Expert in diagnosing and resolving complex network issues.');
INSERT INTO `Staff_Skill` VALUES (2, 'Hardware Troubleshooting', 'Skilled at identifying and repairing hardware problems.');
INSERT INTO `Staff_Skill` VALUES (2, 'Software Installation and Configuration', 'Proficient in installing and configuring software for enhanced user productivity.');
INSERT INTO `Staff_Skill` VALUES (2, 'Computer Proficiency', 'Highly skilled in using a wide range of computer tools and applications.');
INSERT INTO `Staff_Skill` VALUES (2, 'Conflict Resolution', 'Experienced in mediating conflicts and fostering a harmonious work environment.');
INSERT INTO `Staff_Skill` VALUES (2, 'Project Management', 'Capable of leading and executing IT projects efficiently.');
INSERT INTO `Staff_Skill` VALUES (2, 'Strategic Planning', 'Adept at developing long-term IT strategies to support organizational goals.');
INSERT INTO `Staff_Skill` VALUES (2, 'Attention to Detail', 'Known for meticulous attention to detail in all IT tasks and projects.');
INSERT INTO `Staff_Skill` VALUES (2, 'Performance Management', 'Skilled in optimizing system performance and ensuring efficient IT operations.');

INSERT INTO `Staff_Skill` VALUES (3, 'Networking Troubleshooting', 'Known for quickly resolving network issues and ensuring minimal downtime.');
INSERT INTO `Staff_Skill` VALUES (3, 'Hardware Troubleshooting', 'Skilled in diagnosing and repairing hardware problems to maintain smooth operations.');
INSERT INTO `Staff_Skill` VALUES (3, 'Software Installation and Configuration', 'Efficiently installs and configures software to enhance user experience.');
INSERT INTO `Staff_Skill` VALUES (3, 'Computer Proficiency', 'Highly proficient in utilizing various computer tools to address technical problems.');
INSERT INTO `Staff_Skill` VALUES (3, 'Conflict Resolution', 'Experienced in mediating conflicts and maintaining a positive IT environment.');
INSERT INTO `Staff_Skill` VALUES (3, 'PowerPoint', 'Expertise in creating impactful presentations using PowerPoint.');
INSERT INTO `Staff_Skill` VALUES (3, 'Performance Management', 'Dedicated to optimizing IT system performance and ensuring reliability.');
INSERT INTO `Staff_Skill` VALUES (3, 'Attention to Detail', 'Known for an impeccable attention to detail in IT tasks.');

INSERT INTO `Staff_Skill` VALUES (4, 'Video Editing', 'Proficient in video editing techniques to create compelling visual content.');

INSERT INTO `Staff_Skill` VALUES (5, 'Conflict Resolution', 'Skilled at mediating conflicts and promoting a positive work environment, ensuring harmonious relations among team members.');
INSERT INTO `Staff_Skill` VALUES (5, 'Strategic Planning', 'Experienced in developing long-term strategies to drive organizational growth and success.');
INSERT INTO `Staff_Skill` VALUES (5, 'Project Management', 'Adept at leading and executing projects efficiently, ensuring timely delivery of results.');
INSERT INTO `Staff_Skill` VALUES (5, 'Leadership and Team Management', 'Known for effective leadership and team management skills, driving collaboration and achieving team goals.');
INSERT INTO `Staff_Skill` VALUES (5, 'Employment Law Compliance', 'Dedicated to ensuring HR team compliance with all relevant employment laws and regulations.');
INSERT INTO `Staff_Skill` VALUES (5, 'Computer Proficiency', 'Proficient in using various HR software tools to streamline HR processes and enhance efficiency.');
INSERT INTO `Staff_Skill` VALUES (5, 'Attention to Detail', 'Renowned for an exceptional eye for detail, ensuring precision and accuracy in all HR processes.');
INSERT INTO `Staff_Skill` VALUES (5, 'Time Management', 'Efficiently manages time and resources to meet HR team demands and strict deadlines.');
INSERT INTO `Staff_Skill` VALUES (5, 'Performance Management', 'Proficient in assessing and enhancing HR team performance, driving excellence within the department.');

-- Listing TABLE
create table `Listings` (
	`listing_ID` int NOT NULL AUTO_INCREMENT,
    `Role_Name` varchar(20) NOT NULL,
	`Deadline` date NOT NULL,
    constraint Listings_PK primary key (`listing_ID`),
    constraint Listings_FK foreign key (`Role_Name`) references `Role` (`Role_Name`)
);

insert into `Listings` values (1, 'IT Support', '2023-09-25');
insert into `Listings` values (2, 'Clerk', '2023-10-28');
insert into `Listings` values (3, 'Human Resource', '2023-11-18');
insert into `Listings` values (4, 'Manager', '2023-11-05');
insert into `Listings` values (5, 'Clerk', '2025-01-01');

-- Staff_Application TABLE
create table `Staff_Application` (
	`Application_ID` int NOT NULL AUTO_INCREMENT,
	`Staff_ID` int NOT NULL,
    `listing_ID` int NOT NULL,
    constraint Staff_Application_PK primary key (`Application_ID`),
    constraint Staff_Application_FK1 foreign key (`Staff_ID`) references `Staff` (`Staff_ID`),
    constraint Staff_Application_FK2 foreign key (`listing_ID`) references `Listings` (`listing_ID`)
);

insert into `Staff_Application` values (1, 2, 1);
insert into `Staff_Application` values (2, 3, 1);

insert into `Staff_Application` values (4, 1, 2);
insert into `Staff_Application` values (5, 3, 2);

insert into `Staff_Application` values (7, 1, 3);
insert into `Staff_Application` values (8, 2, 3);

insert into `Staff_Application` values (9, 1, 4);
insert into `Staff_Application` values (10, 2, 4);
insert into `Staff_Application` values (11, 3, 4);