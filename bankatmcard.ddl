CREATE TABLE `bankatmcard` (
   `CardNumber` varchar(16) NOT NULL,
   `CVV` varchar(3) DEFAULT NULL,
   `CardHolderName` varchar(100) DEFAULT NULL,
   `ExpiryMonth` int DEFAULT NULL,
   `ExpiryYear` int DEFAULT NULL,
   `UPIId` int DEFAULT NULL,
   `AccountNumber` int DEFAULT NULL,
   PRIMARY KEY (`CardNumber`),
   UNIQUE KEY `CardNumber_UNIQUE` (`CardNumber`),
   KEY `UPIId_idx` (`UPIId`),
   KEY `AccountNumber_idx` (`AccountNumber`),
   CONSTRAINT `AccountNumber` FOREIGN KEY (`AccountNumber`) REFERENCES `bankaccount` (`AccountNumber`),
   CONSTRAINT `UPIId` FOREIGN KEY (`UPIId`) REFERENCES `upi` (`UPIId`)
 );