create database SBRP;
use SBRP;
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