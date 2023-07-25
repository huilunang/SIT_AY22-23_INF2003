-- tinyint: 0 - false, non-zero - true

CREATE TABLE IF NOT EXISTS Users (
  UserID INT PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(255),
  Email VARCHAR(255),
  Area VARCHAR(255),
  Username VARCHAR(255),
  Password CHAR(64),
  isAdmin BOOLEAN,
  Points INT
);

CREATE TABLE IF NOT EXISTS Bins (
  BinID INT PRIMARY KEY,
  Location VARCHAR(255),
  Capacity INT
);

CREATE TABLE IF NOT EXISTS Rewards (
  RewardID INT PRIMARY KEY AUTO_INCREMENT,
  PointCost INT,
  RewardName VARCHAR(255),
  RewardImage VARCHAR(255),
  Stock INT
);

CREATE TABLE IF NOT EXISTS Recycles (
  RecycledID INT PRIMARY KEY AUTO_INCREMENT,
  BinID INT,
  Datetime DATETIME,
  BlobID VARCHAR(24),
  Approved TINYINT(1) DEFAULT 0,
  MaterialType VARCHAR(255),
  UserID INT,
  FOREIGN KEY (BinID) REFERENCES Bins(BinID),
  FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS RewardTransactions (
  TransactionID INT PRIMARY KEY,
  RewardID INT,
  UserID INT,
  Claimed BOOLEAN,
  FOREIGN KEY (RewardID) REFERENCES Rewards(RewardID) ON DELETE CASCADE,
  FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

DELETE FROM Recycles WHERE RecycledID>0;
DELETE FROM RewardTransactions WHERE TransactionID>0;	
DELETE FROM Users WHERE UserID>0;
DELETE FROM Bins WHERE BinID>0;
DELETE FROM Rewards WHERE RewardID>0;

INSERT INTO Users (Name, Email, Area, Username, Password, isAdmin, Points)
VALUES
  ('Phileo Teo', 'phileo@gmail.com', 'Bishan', 'phileo', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', false, 30),
  ('Xue Er', 'xueer@gmail.com', 'Yishun', 'xueer', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', false, 100),
  ('Hui Lun', 'huilun@gmail.com', 'Jurong', 'huilun', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', true, 60),
  ('Si Hui', 'sihui@gmail.com', 'Sengkang', 'sihui', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', false, 380),
  ('Shi Ya', 'shiya@gmail.com', 'Tampines', 'shiya', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', false, 50);

INSERT INTO Bins (BinID, Location, Capacity)
VALUES
  (1, 'Block 123 Ang Mo Kio Ave 4', 10),
  (2, 'Block 456 Bedok North Road', 14),
  (3, 'Block 789 Clementi Street 2', 0),
  (4, 'Block 101 Jurong West Ave 5', 23),
  (5, 'Block 202 Tampines Street 11', 7);

INSERT INTO Rewards (PointCost, RewardName, RewardImage, Stock)
VALUES
  (500, '$10 NTUC Voucher', 'ntuc.png', 10),
  (350, 'Movie Ticket', 'movie.jpg', 10),
  (400, 'Starbucks Gift Card', 'Starbucks.png', 10),
  (450, 'Clothing Store Voucher', 'clothing.jpg', 10),
  (250, 'Bookstore Coupon', 'bookstore.jpg', 10);

INSERT INTO Recycles (RecycledID, BinID, Datetime, BlobID, Approved, MaterialType, UserID)
VALUES
  (1, 1, '2023-02-10 09:30:00', '', 1, 'Plastic', 1),
  (2, 2, '2023-03-05 14:15:00', '', 1, 'Paper', 2),
  (3, 3, '2023-04-20 11:45:00', '', 1, 'Glass', 3),
  (4, 4, '2023-04-28 16:30:00', '', 1, 'Metal', 4),
  (5, 5, '2023-04-15 13:00:00', '', 1, 'Plastic', 5),
  (6, 3, '2023-05-10 11:47:00', '', 1, 'Glass', 4),
  (7, 3, '2023-05-15 10:30:00', '', 1, 'Glass', 3),
  (8, 3, '2023-05-18 18:20:00', '', 1, 'Plastic', 3),
  (9, 4, '2023-06-24 11:23:00', '', 1, 'Plastic', 4),
  (10, 3, '2023-06-24 11:50:00', '', 1, 'Plastic', 4),
  (11, 3, '2023-06-26 12:30:00', '', 1, 'Plastic', 4),
  (12, 3, '2023-06-26 19:35:00', '', 1, 'Glass', 4),
  (13, 3, '2023-06-28 11:09:00', '', 1, 'Metal', 4),
  (14, 3, '2023-07-10 11:15:00', '', 1, 'Metal', 5);
  
  
INSERT INTO RewardTransactions (TransactionID, RewardID, UserID, Claimed)
VALUES
  (1, 1, 1, true),
  (2, 3, 2, false),
  (3, 2, 3, true),
  (4, 5, 4, false),
  (5, 4, 5, true);
