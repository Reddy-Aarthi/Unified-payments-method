CREATE TABLE BANKACCOUNT (
   ACCOUNTNUMBER INT PRIMARY KEY,
   BALANCE DECIMAL(15,2) NOT NULL,
   ACCOUNTTYPE VARCHAR(20) NOT NULL,
   GOVTID VARCHAR(20) NOT NULL,
   CONSTRAINT CGOVTID_FK  FOREIGN KEY (GOVTID) REFERENCES KYC(GOVTID)
 );