CREATE TABLE IF NOT EXISTS Users (
  UserID INT PRIMARY KEY,
  Name VARCHAR(255),
  Email VARCHAR(255),
  Area VARCHAR(255),
  Username VARCHAR(255),
  Password VARCHAR(255),
  isAdmin BOOLEAN,
  Points INT
);

TRUNCATE Users;

INSERT INTO Users (UserID, Name, Email, Area, Username, Password, isAdmin, Points)
VALUES
  (1, 'Phileo Teo', 'phileo@gmail.com', 'Bishan', 'phileo', '123', false, 3),
  (2, 'Xue Er', 'xueer@gmail.com', 'Yishun', 'xueer', '123', false, 10),
  (3, 'Hui Lun', 'huilun@gmail.com', 'Jurong', 'huilun', '123', true, 6),
  (4, 'Si Hui', 'sihui@gmail.com', 'Sengkang', 'sihui', '123', false, 4),
  (5, 'Shi Ya', 'shiya@gmail.com', 'Tampines', 'shiya', '123', false, 5);

CREATE TABLE IF NOT EXISTS Bins (
  BinID INT PRIMARY KEY,
  Location VARCHAR(255),
  Capacity INT
);

TRUNCATE Bins;

INSERT INTO Bins (BinID, Locations, Capacity)
VALUES
  (1, 'Block 123 Ang Mo Kio Ave 4', 10),
  (2, 'Block 456 Bedok North Road', 14),
  (3, 'Block 789 Clementi Street 2', 0),
  (4, 'Block 101 Jurong West Ave 5', 23),
  (5, 'Block 202 Tampines Street 11', 7);



CREATE TABLE IF NOT EXISTS Recycles (
  RecycledID INT PRIMARY KEY,
  BinID INT,
  Datetime DATETIME,
  Image blob,
  MaterialType VARCHAR(255),
  UserID INT,
  FOREIGN KEY (BinID) REFERENCES Bin(BinID),
  FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

TRUNCATE Recycles;

INSERT INTO Recycles (RecycledID, BinID, Datetime, Image, MaterialType, UserID)
VALUES
  (1, 1, '2023-06-10 09:30:00', '', 'Plastic', 1),
  (2, 2, '2023-07-05 14:15:00', '', 'Paper', 2),
  (3, 3, '2023-05-20 11:45:00', '', 'Glass', 3),
  (4, 4, '2023-06-28 16:30:00', '', 'Metal', 4),
  (5, 5, '2023-07-15 13:00:00', '', 'Plastic', 5);

CREATE TABLE IF NOT EXISTS Rewards (
  RewardID INT PRIMARY KEY,
  PointCost FLOAT,
  RewardName VARCHAR(255),
  RewardImage BLOB,
  Stock INT
);

TRUNCATE Rewards;

INSERT INTO Rewards (RewardID, PointCost, RewardName, RewardImage)
VALUES
  (1, 50, 'NTUC Voucher', NULL, 10),
  (2, 35, 'Movie Ticket', NULL, 10),
  (3, 40, 'Starbucks Gift Card', NULL, 10),
  (4, 45, 'Clothing Store Voucher', NULL, 10),
  (5, 25, 'Bookstore Coupon', NULL, 10);

CREATE TABLE IF NOT EXISTS RewardTransactions (
  TransactionID INT PRIMARY KEY,
  RewardID INT,
  UserID INT,
  Claimed BOOLEAN,
  FOREIGN KEY (RewardID) REFERENCES Rewards(RewardID),
  FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

TRUNCATE RewardTransactions;

INSERT INTO RewardTransactions (TransactionID, RewardID, UserID, Claimed)
VALUES
  (1, 1, 1, true),
  (2, 3, 2, false),
  (3, 2, 3, true),
  (4, 5, 4, false),
  (5, 4, 5, true);


