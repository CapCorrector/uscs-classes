/*
Filling the table with test data
*/
INSERT INTO Employee
(EmpID, Name, TaxID, Country, HireDate, BirthDate, Salary, Bonus, DeptID, AddressInfo)
VALUES
('X431', 'Alice', 'TAX431', 'US', '2018-05-15', '1980-01-15', 40000, 1000, 'D1', 'Test address'),
('X432', 'Bob', 'TAX432', 'US', '2018-04-14', '1981-01-13', 40000, 1000, 'D1', 'Test address'),
('X433', 'Ellie', 'TAX433', 'US', '2018-03-21', '1979-01-10', 40000, 1000, 'D2', 'Test address'),
('X434', 'Ann', 'TAX434', 'US', '2018-01-03', '1980-04-21', 40000, 1000, 'D2', 'Test address')
;


INSERT INTO Department
(DeptID, DeptName, DeptHeadID, DeptHeadUserID, DeptAA, ParentDeptID)
VALUES
('D1', 'Dept1', 'X431', 'root', 'X432', NULL),
('D2', 'Dept2', 'X433', 'notroot', 'X434', 'D1')
;

INSERT INTO Place
(PlaceID, Latitude, Longitude, Elevation, Population, Type, Country)
VALUES
('PL1', 55, -2.5, 100, 1000, 'Vilage', 'GB'),
('PL2', 52.4, 0.981515, 150, 1500000, 'City', 'GB'),
('PL3', 37, -120, -100, 1000, 'Vilage', 'US'),
('PL4', 35, -113, 300, 1000000, 'City', 'US'),
('PL5', 40, -100, 1100, 10000, 'Town', 'US')
;

INSERT INTO Supplier
(SupplierID, Name, Country, ReliabilityScore, ContactInfo)
VALUES
('Sup1', 'Suppl1', 'GB', 'A', 'Some contact info'),
('Sup2', 'Suppl2', 'US', 'A', 'Some contact info'),
('Sup3', 'Suppl3_pot', 'AU', NULL, 'Some AU contact info')
;

INSERT INTO Payment
(SupplierID, Date, Amount)
VALUES
('Sup1', '2018-05-15', 10000),
('Sup1', '2018-04-15', 10000),
('Sup1', '2018-06-15', 10000),
('Sup2', '2018-05-15', 15000),
('Sup2', '2018-04-15', 15000),
('Sup2', '2018-06-15', 15000)
;

INSERT INTO SuppliedName
(SnID, Name, Language, Status, Standard, PlaceID, SupplierID, DateSupplied)
VALUES
('Sn1', 'GBVil1', 'English', 'Current', NULL, 'PL1', 'Sup1', '2018-06-01'),
('Sn2', 'GBDer1', 'Russian', 'Local', 'STD2', 'PL1', 'Sup1', '2018-06-01'),
('Sn3', 'GBCit1', 'English', 'Current', 'STD2', 'PL2', 'Sup1', '2018-06-01'),
('Sn4', 'GBGor1', 'Russian', 'Local', 'STD1', 'PL2', 'Sup1', '2018-04-01'),
('Sn5', 'USVil1', 'English', 'Current', NULL, 'PL3', 'Sup2', '2018-04-01'),
('Sn6', 'USDer1', 'Russian', 'Local', 'STD1', 'PL3', 'Sup2', '2018-05-01'),
('Sn7', 'USTow1', 'English', 'Current', 'STD3', 'PL4', 'Sup2', '2018-05-01'),
('Sn8', 'USNp1', 'Russian', 'Local', 'STD3', 'PL4', 'Sup2', '2018-06-01'),
('Sn9', 'USGor1', 'English', 'Current', 'SomeSTD', 'PL5', 'Sup2', '2018-06-01'),
('Sn10', 'USGor1', 'Russian', 'Local', NULL, 'PL5', 'Sup2', '2018-04-01')
;
