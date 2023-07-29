-- tinyint: 0 - false, 1 - true, -1 approved but unsucessful

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
  DetectionID VARCHAR(24),
  Approved TINYINT(1),
  MaterialType VARCHAR(255),
  UserID INT,
  FOREIGN KEY (BinID) REFERENCES Bins(BinID),
  FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS RewardTransactions (
  TransactionID INT PRIMARY KEY AUTO_INCREMENT,
  RewardID INT,
  UserID INT,
  TransactionDate DATETIME,
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
  ('Phileo Teo', 'phileo@gmail.com', 'Bishan', 'phileo', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', false, 10000),
  ('Xue Er', 'xueer@gmail.com', 'Yishun', 'xueer', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', false, 100),
  ('Hui Lun', 'huilun@gmail.com', 'Jurong', 'huilun', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', true, 60),
  ('Si Hui', 'sihui@gmail.com', 'Sengkang', 'sihui', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', false, 380),
  ('Shi Ya', 'shiya@gmail.com', 'Tampines', 'shiya', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', false, 50);

INSERT INTO Bins (BinID, Location, Capacity)
VALUES
  (1, 'Block 123 Ang Mo Kio Ave 4', 110),
  (2, 'Block 456 Bedok North Road', 180),
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

INSERT INTO Recycles (RecycledID, BinID, Datetime, DetectionID, Approved, MaterialType, UserID)
VALUES
  (1, 1, '2023-02-10 09:30:00', '', 1, 'Plastic', 1),
  (2, 2, '2023-04-05 14:15:00', '', 1, 'Paper', 2),
  (3, 3, '2023-06-20 11:45:00', '', 1, 'Glass', 3),
  (4, 4, '2023-06-28 16:30:00', '', 1, 'Metal', 4),
  (5, 5, '2023-06-15 13:00:00', '', 1, 'Plastic', 5),
  (6, 3, '2023-07-10 11:47:00', '', 1, 'Glass', 4),
  (7, 3, '2023-06-15 10:30:00', '', 1, 'Glass', 3),
  (8, 3, '2023-06-18 18:20:00', '', 1, 'Plastic', 3),
  (9, 4, '2023-06-24 11:23:00', '', 1, 'Plastic', 4),
  (10, 3, '2023-07-20 11:50:00', '', 1, 'Plastic', 4),
  (11, 3, '2023-06-26 12:30:00', '', 1, 'Plastic', 4),
  (12, 3, '2023-07-29 19:35:00', '', 1, 'Glass', 4),
  (13, 3, '2023-07-29 11:09:00', '', 1, 'Cardboard', 1),
  (14, 3, '2023-07-29 11:15:00', '', 1, 'Metal', 1),
  (15, 5, '2023-07-30 13:00:00', '', 1, 'Plastic', 5),
  (16, 3, '2023-07-30 11:47:00', '', 1, 'Glass', 4),
  (17, 3, '2023-08-01 10:30:00', '', 1, 'Glass', 3),
  (18, 3, '2023-08-01 18:20:00', '', 1, 'Plastic', 3),
  (19, 4, '2023-08-02 11:23:00', '', 1, 'Cardboard', 4),
  (20, 3, '2023-08-02 11:50:00', '', 1, 'Plastic', 4),
  (21, 1, '2023-08-03 09:30:00', '', 1, 'Plastic', 1),
  (22, 2, '2023-08-03 14:15:00', '', 1, 'Paper', 2),
  (23, 3, '2023-08-04 11:45:00', '', 1, 'Glass', 3),
  (24, 4, '2023-08-04 16:30:00', '', 1, 'Metal', 4),
  (25, 5, '2023-08-05 13:00:00', '', 1, 'Plastic', 5),
  (26, 3, '2023-08-05 11:47:00', '', 1, 'Glass', 4),
  (27, 3, '2023-08-06 10:30:00', '', 1, 'Glass', 3),
  (28, 3, '2023-08-06 18:20:00', '', 1, 'Plastic', 3),
  (29, 4, '2023-08-07 11:23:00', '', 1, 'Plastic', 4),
  (30, 3, '2023-08-07 11:50:00', '', 1, 'Plastic', 4),
  (31, 5, '2023-08-08 09:00:00', '', 1, 'Cardboard', 5),
  (32, 4, '2023-08-08 13:45:00', '', 1, 'Glass', 4),
  (33, 3, '2023-08-09 11:50:00', '', 1, 'Metal', 3),
  (34, 2, '2023-08-09 10:15:00', '', 1, 'Plastic', 2),
  (35, 1, '2023-08-10 17:30:00', '', 1, 'Paper', 1),
  (36, 5, '2023-08-10 08:30:00', '', 1, 'Glass', 5),
  (37, 4, '2023-08-12 15:45:00', '', 1, 'Plastic', 4),
  (38, 3, '2023-08-12 10:50:00', '', 1, 'Plastic', 3),
  (39, 2, '2023-08-13 11:15:00', '', 1, 'Metal', 2),
  (40, 1, '2023-08-13 14:30:00', '', 1, 'Paper', 1),
  (41, 5, '2023-08-14 09:30:00', '', 1, 'Plastic', 5),
  (42, 3, '2023-08-14 11:45:00', '', 1, 'Glass', 3),
  (43, 2, '2023-08-15 13:20:00', '', 1, 'Metal', 2),
  (44, 1, '2023-08-15 15:30:00', '', 1, 'Plastic', 1),
  (45, 1, '2023-08-16 08:30:00', '', 1, 'Plastic', 1),
  (46, 2, '2023-08-16 10:00:00', '', 1, 'Paper', 2),
  (47, 3, '2023-08-17 11:30:00', '', 1, 'Glass', 3),
  (48, 4, '2023-08-17 13:00:00', '', 1, 'Metal', 4),
  (49, 5, '2023-08-18 14:30:00', '', 1, 'Plastic', 5),
  (50, 1, '2023-08-18 16:00:00', '', 1, 'Paper', 1),
  (51, 2, '2023-08-19 17:30:00', '', 1, 'Glass', 2),
  (52, 3, '2023-08-19 19:00:00', '', 1, 'Plastic', 3),
  (53, 4, '2023-08-20 08:30:00', '', 1, 'Metal', 4),
  (54, 5, '2023-08-20 10:00:00', '', 1, 'Glass', 5),
  (55, 1, '2023-08-21 11:30:00', '', 1, 'Paper', 1),
  (56, 2, '2023-08-21 13:00:00', '', 1, 'Glass', 2),
  (57, 3, '2023-08-22 14:30:00', '', 1, 'Plastic', 3),
  (58, 4, '2023-08-22 16:00:00', '', 1, 'Metal', 4),
  (59, 5, '2023-08-23 17:30:00', '', 1, 'Cardboard', 5),
  (60, 1, '2023-08-23 08:30:00', '', 1, 'Plastic', 1),
  (61, 2, '2023-08-24 10:15:00', '', 1, 'Paper', 2),
  (62, 3, '2023-08-24 11:45:00', '', 1, 'Glass', 3),
  (63, 4, '2023-08-25 12:30:00', '', 1, 'Metal', 4),
  (64, 5, '2023-08-25 13:00:00', '', 1, 'Plastic', 5),
  (65, 1, '2023-08-26 14:20:00', '', 1, 'Glass', 1),
  (66, 2, '2023-08-26 15:30:00', '', 1, 'Paper', 2),
  (67, 3, '2023-08-27 09:30:00', '', 1, 'Plastic', 3),
  (68, 4, '2023-08-27 10:45:00', '', 1, 'Glass', 4),
  (69, 5, '2023-08-28 11:50:00', '', 1, 'Metal', 5),
  (70, 1, '2023-08-28 12:15:00', '', 1, 'Plastic', 1),
  (71, 2, '2023-08-29 13:30:00', '', 1, 'Paper', 2),
  (72, 3, '2023-08-29 14:45:00', '', 1, 'Glass', 3),
  (73, 4, '2023-08-29 15:50:00', '', 1, 'Metal', 4),
  (74, 5, '2023-08-30 16:30:00', '', 1, 'Plastic', 5),
  (75, 1, '2023-08-30 17:00:00', '', 1, 'Paper', 1);

INSERT INTO RewardTransactions (TransactionID, RewardID, UserID,TransactionDate, Claimed)
VALUES
  (1, 1, 1, '2023-07-19 13:00:00', true),
  (2, 3, 2, '2023-07-20 13:00:00', false),
  (3, 2, 3, '2023-07-21 13:00:00', true),
  (4, 5, 4, '2023-07-22 13:00:00', false),
  (5, 4, 5, '2023-07-23 13:00:00', true);







