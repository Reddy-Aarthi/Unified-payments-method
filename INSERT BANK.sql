ALTER TABLE Bank CHANGE ISFC IFSC VARCHAR(20);
INSERT INTO Bank (IFSC, BANKNAME, ZIPCODE)
VALUES ('IFSC1', 'BankName1', '123456');

INSERT INTO Bank (IFSC, BANKNAME, ZIPCODE)
VALUES ('IFSC2', 'BankName2', '234567');

INSERT INTO Bank (IFSC, BANKNAME, ZIPCODE)
VALUES ('IFSC3', 'BankName3', '345678');

INSERT INTO Bank (IFSC, BANKNAME, ZIPCODE)
VALUES ('IFSC4', 'BankName4', '456789');

INSERT INTO Bank (IFSC, BANKNAME, ZIPCODE)
VALUES ('IFSC5', 'BankName5', '567890');

INSERT INTO Bank (IFSC, BANKNAME, ZIPCODE)
VALUES ('IFSC6', 'BankName6', '678901');

INSERT INTO Bank (IFSC, BANKNAME, ZIPCODE)
VALUES ('IFSC7', 'BankName7', '789012');

INSERT INTO Bank (IFSC, BANKNAME, ZIPCODE)
VALUES ('IFSC8', 'BankName8', '890123');

INSERT INTO Bank (IFSC, BANKNAME, ZIPCODE)
VALUES ('IFSC9', 'BankName9', '901234');

INSERT INTO Bank (IFSC, BANKNAME, ZIPCODE)
VALUES ('IFSC10', 'BankName10', '012345');