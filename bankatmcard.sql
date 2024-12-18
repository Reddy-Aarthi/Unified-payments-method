CREATE TABLE BANKATMCARD(
   CARDNUMBER VARCHAR(16) PRIMARY KEY,
   CVV VARCHAR(3) NOT NULL,
   CARDHOLDERNAME VARCHAR(100) NOT NULL,
   EXPIRYMONTH int NOT NULL,
   EXPIRYYEAR int NOT NULL,
   UPIId int NOT NULL,
   ACCOUNTNUMBER int NOT NULL,
   CONSTRAINT C_AccNum_FK FOREIGN KEY (ACCOUNTNUMBER) REFERENCES BANKACCOUNT(ACCOUNTNUMBER),
   CONSTRAINT C_UPIId_FK FOREIGN KEY (UPIId) REFERENCES  UPI(UPIID)
 );