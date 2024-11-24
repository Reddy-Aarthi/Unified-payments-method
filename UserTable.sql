CREATE TABLE USER (
   UserId INT PRIMARY KEY,
   FirstName varchar(60) NOT NULL,
   LastName varchar(60) NOT NULL,
   PhoneNumber varchar(15) NOT NULL,
   EmailId varchar(100) NOT NULL,
   UserAddress varchar(255) NOT NULL,
   ZipCode varchar(10) NOT NULL,
   UserPassword varchar(6) NOT NULL
 );