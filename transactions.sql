CREATE TABLE Transactions (
   TransactionsID INT PRIMARY KEY,
   TransactionsDate DATE NOT NULL,
   TransactionsTime TIMESTAMP NOT NULL,
   TransactionsLimit DECIMAL(15,2),
   TransactionsAmount DECIMAL(15,2) NOT NULL,
   TransactionsType VARCHAR(10) NOT NULL,
   Credit TINYINT(1),
   Debit TINYINT(1),
   CardNumber varchar(16),
   CONSTRAINT C_CardNum_FK FOREIGN KEY (CardNumber) REFERENCES BANKATMCARD (CardNumber)
 );
