CREATE TABLE `bankaccount` (
   `AccountNumber` int NOT NULL,
   `Balance` decimal(15,2) DEFAULT NULL,
   `AccountType` varchar(20) DEFAULT NULL,
   `GovtId` varchar(20) NOT NULL,
   PRIMARY KEY (`AccountNumber`),
   UNIQUE KEY `AccountNumber_UNIQUE` (`AccountNumber`),
   UNIQUE KEY `GovtId_UNIQUE` (`GovtId`),
   CONSTRAINT `GovtId` FOREIGN KEY (`GovtId`) REFERENCES `kyc` (`GovtId`)
 );