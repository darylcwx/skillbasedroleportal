# Client name: All-In-One (AIO)
# Project name: Skill Based Role Portal

drop database if exists SBRP_Ais_Kachang;
create database SBRP_Ais_Kachang;
use SBRP_Ais_Kachang;

# ============== Original ==================
CREATE TABLE IF NOT EXISTS user(
    id INT NOT NULL AUTO_INCREMENT,
    data VARCHAR(255),
    PRIMARY KEY (id)
);

insert into user(id, data) VALUES (1, 'john smith');
insert into user(id, data) VALUES (2, 'jada smith');

CREATE TABLE IF NOT EXISTS role(
    id int NOT NULL AUTO_INCREMENT,
    name VARCHAR(255), 
    description VARCHAR(255),
    PRIMARY KEY (id)
);

INSERT INTO role(name, description) VALUES ('Staff', 'Any staff applying for roles');
INSERT INTO role(name, description) VALUES ('Human Resources', 'Any member of the Human Resources team');
INSERT INTO role(name, description) VALUES ('Manager', 'Any manager');
# ================== End of Original ================
# ================== Created based on Project Specification ================== 
# Can create more properties as needed from the project.
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

insert into `Staff` values(1, 'King', 'Kong', 'HR', 'king.kong@aio.com', 1) ;
insert into `Staff` values(1, 'John', 'Smith', 'IT', 'john.smith@aio.com', 1) ;

create table `Role` (
	`Role_Name` varchar(20) NOT NULL,
	`Role_Desc` longtext NOT NULL,
	constraint Role_PK primary key (`Role_Name`)
);

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