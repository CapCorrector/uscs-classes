-- Please use MySQL
-- Uncomment if you need to drop the previous version of tables/views.
-- DROP TABLE IF EXISTS Place,Supplier,SuppliedName,Payment,Employee,Department;
-- DROP VIEW IF EXISTS Myemployees;

CREATE TABLE Place
(
PlaceID VARCHAR(30) PRIMARY KEY,
Latitude DECIMAL(9,6) NOT NULL,
Longitude DECIMAL(9,6) NOT NULL,
Elevation FLOAT,
Population BIGINT,
Type VARCHAR(20) NOT NULL,
Country VARCHAR(50),
INDEX USING BTREE (Latitude),
INDEX USING BTREE (Longitude)
);

CREATE TABLE Supplier
(
SupplierID VARCHAR(10) PRIMARY KEY,
Name VARCHAR(50) NOT NULL,
Country VARCHAR(50),
ReliabilityScore CHAR(1),
ContactInfo Text NOT NULL
);

CREATE TABLE SuppliedName
(
SnID VARCHAR(40) PRIMARY KEY,
Name VARCHAR(200) NOT NULL,
Language VARCHAR(20),
Status VARCHAR(20) NOT NULL,
Standard VARCHAR(20),
PlaceID VARCHAR(30) NOT NULL REFERENCES Place(PlaceID),
SupplierID VARCHAR(10),
DateSupplied DATE NOT NULL
);

CREATE TABLE Payment
(
SupplierID VARCHAR(10) NOT NULL REFERENCES Supplier(SupplierID),
Date DATE NOT NULL,
Amount DECIMAL(11,2) NOT NULL
);

CREATE TABLE Employee
(
EmpID VARCHAR(10) PRIMARY KEY,
Name VARCHAR(100) NOT NULL,
TaxID VARCHAR(50) NOT NULL,
Country VARCHAR(50),
HireDate DATE NOT NULL,
BirthDate DATE,
Salary DECIMAL(8,2) NOT NULL,
Bonus DECIMAL(8,2) NOT NULL DEFAULT 0,
DeptID VARCHAR(5) NOT NULL REFERENCES Department(DeptID),
-- Did not set address, country and birthdate as NOT NULL since there could be for example some remote employees about whoom we don't know that much. If this data is required then NOT NULL should be set.
AddressInfo TEXT,
-- Will not work in sql 5.7 (it would just ignore CHECK part) but that's the way to implement it.
CONSTRAINT CHK_Salary CHECK (Salar>0),
CONSTRAINT CHK_Bonus CHECK (Bonus>=Salary)
);

CREATE TABLE Department
(
DeptID VARCHAR(5) PRIMARY KEY,
DeptName VARCHAR(20) NOT NULL,
-- If we fire head then for some time department can be without head.
DeptHeadID VARCHAR(10),
-- UserID datatape is the same as data type of user in mysql 5.6 for different versions data type should be changed accordingly
DeptHeadUserID CHAR(16),
DeptAA VARCHAR(10),
ParentDeptID VARCHAR(5)
);

-- In this example i don't care about user login source so i just filter the "host" part, in case we care data type for DeptHeadID should be different and user() output should not be filtered.
CREATE VIEW Myemployees AS SELECT employee.* FROM Employee JOIN Department USING (DeptID) WHERE DeptHeadUserID = substring_index(user(),'@', 1)

-- User access part example
-- This part is for roles creation 
-- CREATE ROLE 'employee', 'hr_employee', 'somehr_employee', 'manager';
-- example of granting role to a user: GRANT 'employee', 'manager' TO 'somemanager'@'somehost';
-- GRANT SELECT ON classdb.Place TO 'employee';
-- GRANT SELECT ON classdb.SuppliedName TO 'employee';
-- GRANT SELECT ON classdb.Employee TO 'hr_employee';
-- GRANT SELECT ON classdb.Department TO 'hr_employee';
-- GRANT INSERT, UPDATE, DELETE ON classdb.Employee TO 'somehr_employee';
-- GRANT INSERT, UPDATE, DELETE ON classdb.Department TO 'somehr_employee';
-- GRANT SELECT, UPDATE (Salary, Bonus) ON classdb.Myemployees TO 'manager';
