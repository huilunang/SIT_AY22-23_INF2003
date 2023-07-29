-- tinyint: 0 - false, 1 - true, -1 approved but unsucessful

CREATE TABLE IF NOT EXISTS Users (
  UserID CHAR(36) PRIMARY KEY,
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
  UserID CHAR(36),
  FOREIGN KEY (BinID) REFERENCES Bins(BinID),
  FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS RewardTransactions (
  TransactionID INT PRIMARY KEY AUTO_INCREMENT,
  RewardID INT,
  UserID CHAR(36),
  TransactionDate DATETIME,
  Claimed BOOLEAN,
  FOREIGN KEY (RewardID) REFERENCES Rewards(RewardID) ON DELETE CASCADE,
  FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

DELETE FROM Recycles WHERE RecycledID>0;
DELETE FROM RewardTransactions WHERE TransactionID>0;	
DELETE FROM Users;
DELETE FROM Bins WHERE BinID>0;
DELETE FROM Rewards WHERE RewardID>0;

INSERT INTO Users (UserID, Name, Email, Area, Username, Password, isAdmin, Points)
VALUES
  ('ed1118c3-0297-4369-88ad-3915b6c7a970', 'Phileo Teo', 'phileo@gmail.com', 'Bishan', 'phileo', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', false, 10000),
  ('725f9329-5002-4ce4-94f5-f28ab6328eeb', 'Xue Er', 'xueer@gmail.com', 'Yishun', 'xueer', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', false, 100),
  ('ef562a89-0468-4d33-9280-b5cbec8fdf5b', 'Hui Lun', 'huilun@gmail.com', 'Jurong', 'huilun', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', true, 60),
  ('15b4002c-b194-45ec-842b-235dea4e1db5', 'Si Hui', 'sihui@gmail.com', 'Sengkang', 'sihui', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', false, 380),
  ('bdf70bee-f317-4507-9f96-6b0b472f614e', 'Shi Ya', 'shiya@gmail.com', 'Tampines', 'shiya', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', false, 50);

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
  (1, 1, '2023-02-10 09:30:00', '', 1, 'Plastic', 'ed1118c3-0297-4369-88ad-3915b6c7a970'),
  (2, 2, '2023-04-05 14:15:00', '', 1, 'Paper', '725f9329-5002-4ce4-94f5-f28ab6328eeb'),
  (3, 3, '2023-06-20 11:45:00', '', 1, 'Glass', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (4, 4, '2023-06-28 16:30:00', '', 1, 'Metal', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (5, 5, '2023-06-15 13:00:00', '', 1, 'Plastic', 'bdf70bee-f317-4507-9f96-6b0b472f614e'),
  (6, 3, '2023-07-10 11:47:00', '', 1, 'Glass', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (7, 3, '2023-06-15 10:30:00', '', 1, 'Glass', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (8, 3, '2023-06-18 18:20:00', '', 1, 'Plastic', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (9, 4, '2023-06-24 11:23:00', '', 1, 'Plastic', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (10, 3, '2023-07-20 11:50:00', '', 1, 'Plastic', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (11, 3, '2023-06-26 12:30:00', '', 1, 'Plastic', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (12, 3, '2023-07-29 19:35:00', '', 1, 'Glass', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (13, 3, '2023-07-29 11:09:00', '', 1, 'Cardboard', 'ed1118c3-0297-4369-88ad-3915b6c7a970'),
  (14, 3, '2023-07-29 11:15:00', '', 1, 'Metal', 'ed1118c3-0297-4369-88ad-3915b6c7a970'),
  (15, 5, '2023-07-30 13:00:00', '', 1, 'Plastic', 'bdf70bee-f317-4507-9f96-6b0b472f614e'),
  (16, 3, '2023-07-30 11:47:00', '', 1, 'Glass', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (17, 3, '2023-08-01 10:30:00', '', 1, 'Glass', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (18, 3, '2023-08-01 18:20:00', '', 1, 'Plastic', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (19, 4, '2023-08-02 11:23:00', '', 1, 'Cardboard', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (20, 3, '2023-08-02 11:50:00', '', 1, 'Plastic', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (21, 1, '2023-08-03 09:30:00', '', 1, 'Plastic', 'ed1118c3-0297-4369-88ad-3915b6c7a970'),
  (22, 2, '2023-08-03 14:15:00', '', 1, 'Paper', '725f9329-5002-4ce4-94f5-f28ab6328eeb'),
  (23, 3, '2023-08-04 11:45:00', '', 1, 'Glass', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (24, 4, '2023-08-04 16:30:00', '', 1, 'Metal', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (25, 5, '2023-08-05 13:00:00', '', 1, 'Plastic', 'bdf70bee-f317-4507-9f96-6b0b472f614e'),
  (26, 3, '2023-08-05 11:47:00', '', 1, 'Glass', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (27, 3, '2023-08-06 10:30:00', '', 1, 'Glass', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (28, 3, '2023-08-06 18:20:00', '', 1, 'Plastic', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (29, 4, '2023-08-07 11:23:00', '', 1, 'Plastic', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (30, 3, '2023-08-07 11:50:00', '', 1, 'Plastic', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (31, 5, '2023-08-08 09:00:00', '', 1, 'Cardboard', 'bdf70bee-f317-4507-9f96-6b0b472f614e'),
  (32, 4, '2023-08-08 13:45:00', '', 1, 'Glass', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (33, 3, '2023-08-09 11:50:00', '', 1, 'Metal', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (34, 2, '2023-08-09 10:15:00', '', 1, 'Plastic', '725f9329-5002-4ce4-94f5-f28ab6328eeb'),
  (35, 1, '2023-08-10 17:30:00', '', 1, 'Paper', 'ed1118c3-0297-4369-88ad-3915b6c7a970'),
  (36, 5, '2023-08-10 08:30:00', '', 1, 'Glass', 'bdf70bee-f317-4507-9f96-6b0b472f614e'),
  (37, 4, '2023-08-12 15:45:00', '', 1, 'Plastic', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (38, 3, '2023-08-12 10:50:00', '', 1, 'Plastic', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (39, 2, '2023-08-13 11:15:00', '', 1, 'Metal', '725f9329-5002-4ce4-94f5-f28ab6328eeb'),
  (40, 1, '2023-08-13 14:30:00', '', 1, 'Paper', 'ed1118c3-0297-4369-88ad-3915b6c7a970'),
  (41, 5, '2023-08-14 09:30:00', '', 1, 'Plastic', 'bdf70bee-f317-4507-9f96-6b0b472f614e'),
  (42, 3, '2023-08-14 11:45:00', '', 1, 'Glass', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (43, 2, '2023-08-15 13:20:00', '', 1, 'Metal', '725f9329-5002-4ce4-94f5-f28ab6328eeb'),
  (44, 1, '2023-08-15 15:30:00', '', 1, 'Plastic', 'ed1118c3-0297-4369-88ad-3915b6c7a970'),
  (45, 1, '2023-08-16 08:30:00', '', 1, 'Plastic', 'ed1118c3-0297-4369-88ad-3915b6c7a970'),
  (46, 2, '2023-08-16 10:00:00', '', 1, 'Paper', '725f9329-5002-4ce4-94f5-f28ab6328eeb'),
  (47, 3, '2023-08-17 11:30:00', '', 1, 'Glass', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (48, 4, '2023-08-17 13:00:00', '', 1, 'Metal', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (49, 5, '2023-08-18 14:30:00', '', 1, 'Plastic', 'bdf70bee-f317-4507-9f96-6b0b472f614e'),
  (50, 1, '2023-08-18 16:00:00', '', 1, 'Paper', 'ed1118c3-0297-4369-88ad-3915b6c7a970'),
  (51, 2, '2023-08-19 17:30:00', '', 1, 'Glass', '725f9329-5002-4ce4-94f5-f28ab6328eeb'),
  (52, 3, '2023-08-19 19:00:00', '', 1, 'Plastic', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (53, 4, '2023-08-20 08:30:00', '', 1, 'Metal', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (54, 5, '2023-08-20 10:00:00', '', 1, 'Glass', 'bdf70bee-f317-4507-9f96-6b0b472f614e'),
  (55, 1, '2023-08-21 11:30:00', '', 1, 'Paper', 'ed1118c3-0297-4369-88ad-3915b6c7a970'),
  (56, 2, '2023-08-21 13:00:00', '', 1, 'Glass', '725f9329-5002-4ce4-94f5-f28ab6328eeb'),
  (57, 3, '2023-08-22 14:30:00', '', 1, 'Plastic', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (58, 4, '2023-08-22 16:00:00', '', 1, 'Metal', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (59, 5, '2023-08-23 17:30:00', '', 1, 'Cardboard', 'bdf70bee-f317-4507-9f96-6b0b472f614e'),
  (60, 1, '2023-08-23 08:30:00', '', 1, 'Plastic', 'ed1118c3-0297-4369-88ad-3915b6c7a970'),
  (61, 2, '2023-08-24 10:15:00', '', 1, 'Paper', '725f9329-5002-4ce4-94f5-f28ab6328eeb'),
  (62, 3, '2023-08-24 11:45:00', '', 1, 'Glass', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (63, 4, '2023-08-25 12:30:00', '', 1, 'Metal', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (64, 5, '2023-08-25 13:00:00', '', 1, 'Plastic', 'bdf70bee-f317-4507-9f96-6b0b472f614e'),
  (65, 1, '2023-08-26 14:20:00', '', 1, 'Glass', 'ed1118c3-0297-4369-88ad-3915b6c7a970'),
  (66, 2, '2023-08-26 15:30:00', '', 1, 'Paper', '725f9329-5002-4ce4-94f5-f28ab6328eeb'),
  (67, 3, '2023-08-27 09:30:00', '', 1, 'Plastic', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (68, 4, '2023-08-27 10:45:00', '', 1, 'Glass', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (69, 5, '2023-08-28 11:50:00', '', 1, 'Metal', 'bdf70bee-f317-4507-9f96-6b0b472f614e'),
  (70, 1, '2023-08-28 12:15:00', '', 1, 'Plastic', 'ed1118c3-0297-4369-88ad-3915b6c7a970'),
  (71, 2, '2023-08-29 13:30:00', '', 1, 'Paper', '725f9329-5002-4ce4-94f5-f28ab6328eeb'),
  (72, 3, '2023-08-29 14:45:00', '', 1, 'Glass', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (73, 4, '2023-08-29 15:50:00', '', 1, 'Metal', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (74, 5, '2023-08-30 16:30:00', '', 1, 'Plastic', 'bdf70bee-f317-4507-9f96-6b0b472f614e'),
  (75, 1, '2023-08-30 17:00:00', '', 1, 'Paper', 'ed1118c3-0297-4369-88ad-3915b6c7a970');

Please note that I have generated random dates within the specified range (2023-07-05 to 2023-08-29) for the new entries. You can modify the dates as needed. Also, ensure that the existing data IDs go up to 10 before running the above SQL statement to prevent conflicts.




User
Create entries 30 to 40, keep the date within 2023-06
ChatGPT
To create entries from 30 to 40 and keep the dates within 2023-06, you can use the following SQL INSERT statement:

sql
Copy code
INSERT INTO Recycles (RecycledID, BinID, Datetime, DetectionID, Approved, MaterialType, UserID)
VALUES
  (31, 1, '2023-06-01 09:30:00', '', 1, 'Plastic', 'ed1118c3-0297-4369-88ad-3915b6c7a970'),
  (32, 2, '2023-06-02 14:15:00', '', 1, 'Paper', '725f9329-5002-4ce4-94f5-f28ab6328eeb'),
  (33, 3, '2023-06-03 11:45:00', '', 1, 'Glass', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (34, 4, '2023-06-04 16:30:00', '', 1, 'Metal', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (35, 5, '2023-06-05 13:00:00', '', 1, 'Plastic', 'bdf70bee-f317-4507-9f96-6b0b472f614e'),
  (36, 3, '2023-06-06 11:47:00', '', 1, 'Glass', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (37, 3, '2023-06-07 10:30:00', '', 1, 'Glass', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (38, 3, '2023-06-08 18:20:00', '', 1, 'Plastic', 'ef562a89-0468-4d33-9280-b5cbec8fdf5b'),
  (39, 4, '2023-06-09 11:23:00', '', 1, 'Plastic', '15b4002c-b194-45ec-842b-235dea4e1db5'),
  (40, 3, '2023-06-10 11:50:00', '', 1, 'Plastic', '15b4002c-b194-45ec-842b-235dea4e1db5');
Please note that the dates in this insert statement are within 2023-06. Adjust the dates as needed while making sure they stay within that range. Also, ensure that the existing data IDs go up to 30 before running the above SQL statement to prevent conflicts.






INSERT INTO RewardTransactions (TransactionID, RewardID, UserID, Claimed, TransactionDate)
VALUES
  (1, 1, 'ed1118c3-0297-4369-88ad-3915b6c7a970', true, '2023-07-19 13:00:00'),
  (2, 3, '725f9329-5002-4ce4-94f5-f28ab6328eeb', false, '2023-07-20 13:00:00'),
  (3, 2, 'bdf70bee-f317-4507-9f96-6b0b472f614e', true, '2023-07-21 13:00:00'),
  (4, 5, '15b4002c-b194-45ec-842b-235dea4e1db5', false, '2023-07-22 13:00:00'),
  (5, 4, 'ef562a89-0468-4d33-9280-b5cbec8fdf5b', true, '2023-07-23 13:00:00');
