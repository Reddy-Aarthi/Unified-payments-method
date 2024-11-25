CREATE TABLE NOTIFICATIONS (
   NOTIFICATIONID INT PRIMARY KEY,
   TIMESTAMP TIMESTAMP NOT NULL,
   TYPE VARCHAR(20) NOT NULL,
   MESSAGE VARCHAR(255),
   USERID INT,
   CONSTRAINT C_UserId_Notifications FOREIGN KEY (USERID) REFERENCES USER(UserId)
 );