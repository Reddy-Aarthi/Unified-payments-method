CREATE TABLE USER (
   USERID INT PRIMARY KEY,
   FIRSTNAME varchar(60) NOT NULL,
   LASTNAME varchar(60) NOT NULL,
   PHONENUMBER varchar(15) NOT NULL,
   EMAILID varchar(100) NOT NULL,
   USERADDRESS varchar(255) NOT NULL,
   ZIPCODE varchar(10) NOT NULL,
   USERPASSWORD varchar(6) NOT NULL
 );
ALTER TABLE USER MODIFY USERID INT AUTO_INCREMENT;