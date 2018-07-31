-- 1
SET @placeid:='PL1';
SELECT Elevation, Population FROM Place WHERE PlaceID = @placeid;

-- 2
SET @partname:='Vil';
SELECT PlaceID FROM SuppliedName WHERE Name LIKE CONCAT('%', @partname, '%');

-- 3
SET @latmin:=36;
SET @latmax:=38;
SET @longmin:=-121;
SET @longmax:=-119;
SELECT PlaceID FROM Place WHERE Latitude > @latmin AND Latitude < @latmax AND Longitude > @longmin AND Longitude < @longmax;

-- 4
SET @placename='GBDer1';
SELECT Type, Latitude, Longitude, Country, Population, Elevation FROM Place JOIN SuppliedName USING (PlaceID) WHERE Name = @placename;

-- 5
SET @placeid:='PL2';
SELECT Name, Language, Status AS Type, Standard FROM SuppliedName WHERE PlaceID = @placeid;

-- 6
SET @placename:='USGor1';
-- Can be done using JOIN as was done in task 4
SELECT * FROM Supplier WHERE SupplierID IN (SELECT SupplierID FROM SuppliedName WHERE Name = @placename);

-- 7
SELECT Language, COUNT(*) FROM SuppliedName WHERE LAST_DAY(CURDATE())>= DateSupplied AND DateSupplied >= DATE_FORMAT(CURDATE(),'%Y--%m--01') GROUP BY Language;

-- 8
SELECT SUM(Amount) FROM Payment WHERE LAST_DAY(CURDATE())>= Date AND Date >= DATE_FORMAT(CURDATE(),'%Y--%m--01');

-- 9
SELECT SupplierID, SUM(Amount) FROM Payment WHERE LAST_DAY(CURDATE())>= Date AND Date >= DATE_FORMAT(CURDATE(),'%Y--%m--01') GROUP BY SupplierID;

-- 10
SET @deptid:='D1';
SELECT * FROM Employee WHERE DeptID = @deptid;

-- 11
SET @deptid:='D1';
UPDATE Employee SET Salary = Salary * 1.1, Bonus = 0 WHERE DeptID = @deptid;

-- 12
SELECT e2.Name AS Manager, DeptName, e1.* FROM Employee as e1 JOIN Department USING (DeptID) JOIN Employee as e2 ON DeptHeadId=e2.EmpID ORDER BY e2.Name, e1.Name;

-- 13
SELECT Supplier.*, COUNT(DISTINCT SnID) AS Supplied_names FROM Supplier LEFT OUTER JOIN SuppliedName USING (SupplierId) WHERE (LAST_DAY(CURDATE())>= DateSupplied AND DateSupplied >= DATE_FORMAT(CURDATE(),'%Y--%m--01')) OR SnID IS NULL GROUP BY SupplierID ORDER BY Country;

-- 14
-- In worst scenario (using mysql 5.7) we will have to implement per user access rules or create an additional table with roles and try to emulate role based access level through views approach (like managers part of the task). Or we can
-- use MySQL 8.0 to implement roles approach like it is described in commented part of the provision file and grant any user required roles.

-- 15
-- I whould do it using foreign key (REFERENCES) and NOT NULL constraints for the relations and using CHECK for bonus/salary constraints. Mysql 5.7 does not support check however, so in this case triggers should be used.
