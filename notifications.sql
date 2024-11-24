CREATE TABLE notifications (
   NotificationId INT PRIMARY KEY,
   Timestamp timestamp NOT NULL,
   Type VARCHAR(20) NOT NULL,
   Message VARCHAR(255),
   UserId INT,
   CONSTRAINT C_UserId_Notifications FOREIGN KEY (USERID) REFERENCES USER(UserId)
 );