
CREATE DATABASE IF NOT EXISTS MilkAdulterationDB;
USE MilkAdulterationDB;

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    FullName VARCHAR(50) NOT NULL,
    Email VARCHAR(50) UNIQUE,
    City VARCHAR(30),
    DateJoined DATE,
    Status VARCHAR(10),
    Age INT,
    ReferralCode VARCHAR(10)
);

INSERT INTO Customers (FullName, Email, City, DateJoined, Status, Age, ReferralCode) VALUES
('Aarav Kumar', 'aarav@example.com', 'Delhi', '2022-01-15', 'Active', 28, 'REF001'),
('Riya Sharma', 'riya@example.com', 'Mumbai', '2021-12-10', 'Active', 24, 'REF002'),
('Aman Verma', 'aman@example.com', 'Delhi', '2023-03-05', 'Inactive', 32, 'REF003'),
('Neha Singh', NULL, 'Lucknow', '2022-06-25', 'Active', 30, NULL),
('Karan Patel', 'karan@example.com', NULL, '2021-11-19', 'Blocked', 35, 'REF005'),
('Deepa Joshi', 'deepa@example.com', 'Bangalore', '2021-05-03', 'Active', 27, 'REF006'),
('Sanjay Rao', NULL, 'Chennai', '2022-09-01', 'Inactive', 40, NULL),
('Meera Iyer', 'meera@example.com', 'Bangalore', '2023-01-11', 'Active', 25, 'REF007'),
('Raj Malhotra', 'rajm@example.com', 'Delhi', '2022-04-14', 'Blocked', 31, 'REF008'),
('Alok Pandey', 'alok@example.com', 'Mumbai', '2021-08-19', 'Active', 29, NULL),
('Tina Dsouza', 'tina@example.com', 'Goa', '2023-03-12', 'Active', 23, 'REF009'),
('Farhan Khan', 'farhan@example.com', NULL, '2022-11-30', 'Inactive', 34, NULL),
('Zara Shaikh', 'zara@example.com', 'Hyderabad', '2023-02-18', 'Active', 26, 'REF010'),
('Yusuf Ansari', NULL, 'Kolkata', '2021-10-05', 'Blocked', 38, NULL),
('Lakshmi Nair', 'lakshmi@example.com', 'Chennai', '2022-07-20', 'Active', 33, 'REF011'),
('Divya Jain', 'divya@example.com', 'Delhi', '2023-04-01', 'Inactive', 27, NULL),
('Rakesh Roy', 'rakesh@example.com', 'Lucknow', '2022-12-23', 'Active', 36, 'REF012'),
('Sneha Das', NULL, 'Kolkata', '2021-06-14', 'Blocked', 31, 'REF013'),
('Manoj Mehta', 'manoj@example.com', 'Bangalore', '2022-03-09', 'Active', 28, NULL),
('Nikita Saini', 'nikita@example.com', 'Goa', '2023-03-10', 'Active', 22, 'REF014'),
('Ankit Rana', 'ankit@example.com', NULL, '2021-09-18', 'Inactive', 35, 'REF015'),
('Komal Raj', 'komal@example.com', 'Delhi', '2022-08-22', 'Active', 29, 'REF016'),
('Harshita Dubey', 'harshita@example.com', 'Mumbai', '2023-02-04', 'Blocked', 34, NULL),
('Sunil Jadhav', 'sunil@example.com', 'Pune', '2021-04-25', 'Inactive', 40, 'REF017'),
('Jyoti Bhosale', NULL, 'Mumbai', '2023-01-29', 'Active', 26, 'REF018');

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    OrderDate DATE,
    Product VARCHAR(50),
    Quantity INT,
    Price DECIMAL(10,2),
    PaymentStatus VARCHAR(10),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

INSERT INTO Orders (CustomerID, OrderDate, Product, Quantity, Price, PaymentStatus) VALUES
(1, '2023-01-15', 'Milk Analyzer', 2, 4500.00, 'Paid'),
(2, '2023-01-20', 'Fat Meter', 1, 2500.00, 'Unpaid'),
(3, '2023-02-05', 'Milk Analyzer', 1, 4500.00, 'Paid'),
(4, '2023-03-12', 'Test Kit', 3, 300.00, 'Paid'),
(5, '2023-01-25', 'Fat Meter', 2, 5000.00, 'Unpaid'),
(6, '2023-02-18', 'pH Strip', 4, 100.00, 'Paid'),
(7, '2023-03-01', 'Turbidity Sensor', 1, 1200.00, 'Paid'),
(8, '2023-03-05', 'Milk Analyzer', 2, 9000.00, 'Unpaid'),
(9, '2023-03-10', 'Lactometer', 3, 450.00, 'Paid'),
(10, '2023-03-14', 'TCS34725', 1, 1800.00, 'Paid'),
(11, '2023-03-16', 'pH Strip', 5, 125.00, 'Unpaid'),
(12, '2023-03-20', 'Fat Meter', 1, 2500.00, 'Paid'),
(13, '2023-03-23', 'Milk Analyzer', 2, 4500.00, 'Unpaid'),
(14, '2023-03-26', 'Turbidity Sensor', 3, 3600.00, 'Paid'),
(15, '2023-03-29', 'Test Kit', 1, 100.00, 'Paid'),
(16, '2023-04-02', 'pH Strip', 6, 150.00, 'Paid'),
(17, '2023-04-05', 'Fat Meter', 2, 5000.00, 'Unpaid'),
(18, '2023-04-08', 'Milk Analyzer', 1, 4500.00, 'Paid'),
(19, '2023-04-10', 'TCS34725', 2, 3600.00, 'Paid'),
(20, '2023-04-12', 'Lactometer', 1, 150.00, 'Unpaid'),
(21, '2023-04-14', 'Test Kit', 2, 200.00, 'Paid'),
(22, '2023-04-16', 'Turbidity Sensor', 1, 1200.00, 'Unpaid'),
(23, '2023-04-18', 'Fat Meter', 1, 2500.00, 'Paid'),
(24, '2023-04-20', 'pH Strip', 3, 75.00, 'Paid'),
(25, '2023-04-21', 'Lactometer', 1, 150.00, 'Unpaid');

CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(50),
    Category VARCHAR(30),
    UnitPrice DECIMAL(10,2),
    Stock INT,
    Manufacturer VARCHAR(50)
);

INSERT INTO Products (ProductName, Category, UnitPrice, Stock, Manufacturer) VALUES
('Milk Analyzer', 'Sensor', 4500.00, 10, 'AgroTech Ltd.'),
('Fat Meter', 'Sensor', 2500.00, 15, 'DairyTools'),
('pH Strip', 'Testing Kit', 25.00, 200, 'ChemSense'),
('Turbidity Sensor', 'Sensor', 1200.00, 8, 'AgroTech Ltd.'),
('TCS34725', 'Sensor', 1800.00, 12, 'ColorTech'),
('Lactometer', 'Testing Kit', 150.00, 50, 'DairyTools'),
('Test Kit', 'Testing Kit', 100.00, 70, 'ChemSense'),
('Milk Analyzer Pro', 'Sensor', 6500.00, 5, 'AgroTech Ltd.'),
('Smart pH Meter', 'Sensor', 3000.00, 4, 'LabX'),
('Deluxe Fat Meter', 'Sensor', 2800.00, 6, 'DairyTools'),
('Mini Turbidity Sensor', 'Sensor', 1000.00, 7, 'AgroTech Ltd.'),
('Color Sensor v2', 'Sensor', 2100.00, 9, 'ColorTech'),
('Advanced Kit', 'Testing Kit', 500.00, 20, 'ChemSense'),
('Basic Kit', 'Testing Kit', 80.00, 30, 'ChemSense'),
('Standard Lactometer', 'Testing Kit', 160.00, 40, 'DairyTools'),
('Lab Strip Pack', 'Testing Kit', 60.00, 100, 'LabX'),
('Sensor Combo', 'Sensor', 7000.00, 3, 'AgroTech Ltd.'),
('Sensor Lite', 'Sensor', 2900.00, 6, 'DairyTools'),
('Fat Meter Junior', 'Sensor', 2000.00, 8, 'DairyTools'),
('Quick Test', 'Testing Kit', 90.00, 60, 'ChemSense'),
('Smart Analyzer', 'Sensor', 4700.00, 4, 'AgroTech Ltd.'),
('Color Reader', 'Sensor', 2200.00, 7, 'ColorTech'),
('Field pH Kit', 'Testing Kit', 70.00, 150, 'LabX'),
('Eco Turbidity Sensor', 'Sensor', 950.00, 11, 'AgroTech Ltd.'),
('Elite Fat Meter', 'Sensor', 3100.00, 5, 'DairyTools');
