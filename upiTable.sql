CREATE TABLE UPI (
   UPIId INT PRIMARY KEY,
   UPINumber INT NOT NULL,
   TransactionHistory VARCHAR(255),
   CustomerSupport VARCHAR(255),
   Refunds VARCHAR(255),
   UserId INT,
   CONSTRAINT CuserId_FK FOREIGN KEY (UserId) References USER(UserId)
 );
