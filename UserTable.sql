CREATE TABLE `user` (
   `UserId` int NOT NULL,
   `FirstName` varchar(60) NOT NULL,
   `LastName` varchar(60) NOT NULL,
   `PhoneNumber` varchar(15) NOT NULL,
   `EmailId` varchar(100) NOT NULL,
   `Address` varchar(255) NOT NULL,
   `ZipCode` varchar(10) NOT NULL,
   PRIMARY KEY (`UserId`),
   UNIQUE KEY `EmailId_UNIQUE` (`EmailId`),
   UNIQUE KEY `PhoneNumber_UNIQUE` (`PhoneNumber`),
   UNIQUE KEY `UserId_UNIQUE` (`UserId`)
 );