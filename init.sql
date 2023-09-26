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

insert into `Staff` values(1, 'Jude', 'Smith', 'IT', 'jude.smith@aio.com', 0) ;
insert into `Staff` values(2, 'King', 'Kong', 'HR', 'king.kong@aio.com', 1) ;
insert into `Staff` values(3, 'John', 'Smith', 'IT', 'john.smith@aio.com', 1) ;
insert into `Staff` values(4, 'Little', 'Tip', 'Finance', 'little.tip@aio.com', 2) ;
insert into `Staff` values(5, 'Chicken', 'Ninja', 'HR', 'chicken.ninja@aio.com', 2) ;
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
	constraint Staff_Skill_FK1 foreign key (`Staff_ID`) references `Staff` (`Staff_ID`),
	constraint Staff_Skill_FK2 foreign key (`Skill_Name`) references `Role_Skill` (`Skill_Name`)
);

insert into `Staff_Skill` values (1, 'Networking Troubleshooting','Assist in daily user technical problems and IT equipment maintenance.');
insert into `Staff_Skill` values (1, 'Hardware Troubleshooting','Assist in daily user technical problems and IT equipment maintenance.');
insert into `Staff_Skill` values (1, 'Software Installation and Configuration','Assist in daily user technical problems and IT equipment maintenance.');
insert into `Staff_Skill` values (1, 'Computer Proficiency','Assist in daily user technical problems and IT equipment maintenance.');
insert into `Staff_Skill` values (1, 'Conflict Resolution','Assist in daily user technical problems and IT equipment maintenance.');
insert into `Staff_Skill` values (1, 'Project Management','Assist in daily user technical problems and IT equipment maintenance.');
insert into `Staff_Skill` values (1, 'Strategic Planning','Assist in daily user technical problems and IT equipment maintenance.');
insert into `Staff_Skill` values (1, 'Attention to Detail','Assist in daily user technical problems and IT equipment maintenance.');
insert into `Staff_Skill` values (1, 'Performance Management','Assist in daily user technical problems and IT equipment maintenance.');

insert into `Staff_Skill` values (2, 'Attention to Detail','Any member of the Human Resources team.');
insert into `Staff_Skill` values (2, 'Time Management','Any member of the Human Resources team.');
insert into `Staff_Skill` values (2, 'Performance Management','Any member of the Human Resources team.');
insert into `Staff_Skill` values (2, 'Employment Law Compliance','Any member of the Human Resources team.');
insert into `Staff_Skill` values (2, 'Computer Proficiency','Any member of the Human Resources team.');
insert into `Staff_Skill` values (2, 'Conflict Resolution','Any member of the Human Resources team.');

insert into `Staff_Skill` values (3, 'Networking Troubleshooting','Assist in daily user technical problems and IT equipment maintenance.');
insert into `Staff_Skill` values (3, 'Hardware Troubleshooting','Assist in daily user technical problems and IT equipment maintenance.');
insert into `Staff_Skill` values (3, 'Software Installation and Configuration','Assist in daily user technical problems and IT equipment maintenance.');
insert into `Staff_Skill` values (3, 'Computer Proficiency','Assist in daily user technical problems and IT equipment maintenance.');
insert into `Staff_Skill` values (3, 'Conflict Resolution','Assist in daily user technical problems and IT equipment maintenance.');
insert into `Staff_Skill` values (3, 'PowerPoint','Assist in daily user technical problems and IT equipment maintenance.');
insert into `Staff_Skill` values (3, 'Performance Management','Assist in daily user technical problems and IT equipment maintenance.');
insert into `Staff_Skill` values (3, 'Attention to Detail','Assist in daily user technical problems and IT equipment maintenance.');

-- Listing TABLE
create table `Listings` (
	`listing_ID` int NOT NULL AUTO_INCREMENT,
    `Role_Name` varchar(20) NOT NULL,
	`Deadline` date NOT NULL,
    constraint Listings_PK primary key (`listing_ID`),
    constraint Listings_FK foreign key (`Role_Name`) references `Role` (`Role_Name`)
);

insert into `Listings` values (1, 'IT Support', '2023-10-25');
insert into `Listings` values (2, 'Clerk', '2023-10-28');
insert into `Listings` values (3, 'Human Resource', '2023-11-18');
insert into `Listings` values (4, 'Manager', '2023-11-05');

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