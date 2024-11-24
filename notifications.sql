CREATE TABLE `notifications` (
   `NotificationId` int NOT NULL,
   `Timestamp` timestamp NOT NULL,
   `Type` varchar(20) NOT NULL,
   `Message` varchar(255) DEFAULT NULL,
   `UserId` int DEFAULT NULL,
   PRIMARY KEY (`NotificationId`),
   KEY `UserId_idx` (`UserId`),
   CONSTRAINT `FK_UserId_Notifications` FOREIGN KEY (`UserId`) REFERENCES `user` (`UserId`)
 );
