CREATE TABLE UPI (
   UPIId INT PRIMARY KEY,
   UPINUMBER INT NOT NULL,
   TRANSACTIONHISTORY VARCHAR(255),
   CUSTOMERSUPPORT VARCHAR(255),
   REFUNDS VARCHAR(255),
   USERID INT,
   CONSTRAINT CUSERID_FK FOREIGN KEY (USERID) References USER(USERID)
 );
