CREATE TABLE KYC (
   GOVTID VARCHAR(20) PRIMARY KEY,
   FIRSTNAME VARCHAR(60) NOT NULL,
   LASTNAME VARCHAR(60) NOT NULL,
   DOB DATE  NOT NULL,
   NATIONALITY VARCHAR(50),
   GENDER VARCHAR(10) NOT NULL
 );
