CREATE TABLE `transactions` (
   `TransactionsID` int NOT NULL,
   `TransactionsDate` date DEFAULT NULL,
   `TransactionsTime` timestamp NULL DEFAULT NULL,
   `TransactionsLimit` decimal(15,2) DEFAULT NULL,
   `TransactionsAmount` decimal(15,2) DEFAULT NULL,
   `TransactionsType` varchar(10) DEFAULT NULL,
   `Credit` tinyint(1) DEFAULT NULL,
   `Debit` tinyint(1) DEFAULT NULL,
   `CardNumber` varchar(16) DEFAULT NULL,
   PRIMARY KEY (`TransactionsID`),
   UNIQUE KEY `TransactionsID_UNIQUE` (`TransactionsID`),
   KEY `CardNumber_idx` (`CardNumber`),
   CONSTRAINT `CardNumber` FOREIGN KEY (`CardNumber`) REFERENCES `bankatmcard` (`CardNumber`)
 )
