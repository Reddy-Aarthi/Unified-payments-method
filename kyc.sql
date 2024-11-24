CREATE TABLE `kyc` (
   `GovtId` varchar(20) NOT NULL,
   `FirstName` varchar(60) NOT NULL,
   `LastName` varchar(60) NOT NULL,
   `DOB Date` varchar(45) NOT NULL,
   `Nationality` varchar(50) DEFAULT NULL,
   `Gender` varchar(10) DEFAULT NULL,
   PRIMARY KEY (`GovtId`),
   UNIQUE KEY `GovtId_UNIQUE` (`GovtId`)
 );
