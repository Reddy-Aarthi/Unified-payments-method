CREATE TABLE `upi` (
   `UPIId` int NOT NULL,
   `UPINumber` int NOT NULL,
   `TransactionHistory` varchar(255) DEFAULT NULL,
   `CustomerSupport` varchar(255) DEFAULT NULL,
   `Refunds` varchar(255) DEFAULT NULL,
   `UserId` int DEFAULT NULL,
   PRIMARY KEY (`UPIId`),
   UNIQUE KEY `UPIid_UNIQUE` (`UPIId`),
   UNIQUE KEY `UPINumber_UNIQUE` (`UPINumber`),
   KEY `UserId_idx` (`UserId`),
   CONSTRAINT `UserId` FOREIGN KEY (`UserId`) REFERENCES `user` (`UserId`)
 );
