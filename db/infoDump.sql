-- There are two dataset here: info1 and info2

--
-- Table structure for table `info1`
--

CREATE TABLE `info1` (
  `id` int(2) NOT NULL,
  `type` varchar(7) NOT NULL,
  `item` varchar(294) NOT NULL,
  `recycle` varchar(5) DEFAULT NULL,
  `remarks` varchar(566) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `info1`
--

INSERT INTO `info1` (`id`, `type`, `item`, `recycle`, `remarks`) VALUES
(1, 'Paper', 'Printed paper (Glossy and non-glossy)', 'YES', ''),
(2, 'Paper', 'Writing paper', 'YES', ''),
(3, 'Paper', 'Newspaper', 'YES', ''),
(4, 'Paper', 'Flyer (Glossy and non-glossy)', 'YES', ''),
(5, 'Paper', 'Brochure (Glossy and non-glossy)', 'YES', ''),
(6, 'Paper', 'Magazine (Glossy and non-glossy)', 'YES', ''),
(7, 'Paper', 'Book / Textbook', 'YES', 'Donate if it is in good condition'),
(8, 'Paper', 'Telephone directory', 'YES', ''),
(9, 'Paper', 'Envelope (With and without plastic window)', 'YES', ''),
(10, 'Paper', 'Red packet', 'YES', ''),
(11, 'Paper', 'Namecard', 'YES', ''),
(12, 'Paper', 'Calendar', 'YES', ''),
(13, 'Paper', 'Greeting card', 'YES', ''),
(14, 'Paper', 'Gift wrapping paper', 'YES', ''),
(15, 'Paper', 'Shredded paper', 'YES', ''),
(16, 'Paper', 'Paper receipt', 'YES', ''),
(17, 'Paper', 'Carton box / Cardboard box', 'YES', 'Please flatten'),
(18, 'Paper', 'Paper packaging / Printed paper box / Paper Box', 'YES', 'Please flatten'),
(19, 'Paper', 'Egg tray', 'YES', ''),
(20, 'Paper', 'Beverage carton (e.g. milk, juice and drink packet)', 'YES', 'Please empty and rinse when necessary. Please flatten'),
(21, 'Paper', 'Paper towel and toilet roll tube', 'YES', ''),
(22, 'Paper', 'Tissue box', 'YES', 'Please flatten'),
(23, 'Paper', 'Paper bag', 'YES', ''),
(24, 'Paper', 'Paper disposables such as Paper cup, Paper plate, Glitter paper, Crayon drawing', 'NO', 'Dispose as general waste'),
(25, 'Paper', 'Tissue paper', 'NO', 'Dispose as general waste'),
(26, 'Paper', 'Paper towel', 'NO', 'Dispose as general waste'),
(27, 'Paper', 'Toilet paper', 'NO', 'Dispose as general waste'),
(28, 'Paper', 'Disposable wooden chopstick / Wooden chopsticks / Pizza boxes', 'NO', 'Dispose as general waste'),
(29, 'Paper', 'Wax paper', 'NO', 'Dispose as general waste'),
(30, 'Paper', 'Paper packaging that are contaminated with food (eg pizza box, paper bag for pastries)', 'NO', 'Dispose as general waste'),
(31, 'Plastic', 'Plastic bottle/container - Food or Beverage (e.g. Mineral water bottle, Soft drink bottle, Carbonated drink bottle, Milk bottle, Water bottle, Medicine bottle etc)', 'YES', 'Please empty and rinse when necessary'),
(32, 'Plastic', 'Plastic bottle/container - Non-food (e.g. shampoo, bodywash, facial cleanser, detergent, soap etc)', 'YES', 'Please empty and rinse when necessary'),
(33, 'Plastic', 'CD/DVD and CD/DVC casing', 'YES', ''),
(34, 'Plastic', 'Plastic bag, toilet paper packaging, tissue box packaging', 'YES', ''),
(35, 'Plastic', 'Plastic film (e.g. magazine wrapper, plastic packaging for packet drinks), bubble wrap, fruit box, ziplock bag', 'YES', ''),
(36, 'Plastic', 'Plastic packaging, bread bag, egg trays', 'YES', 'Please empty contents'),
(37, 'Plastic', 'Plastic clothes hanger', 'YES', ''),
(38, 'Plastic', 'Plastic takeaway food container, plastic cups, bubble tea cups', 'YES', ''),
(39, 'Plastic', 'Polystyrene foam product (e.g. Styrofoam cup, clam shell container)', 'NO', 'Dispose as general waste'),
(40, 'Plastic', 'Plastic disposables - cutlery and crockery', 'NO', 'Dispose as general waste'),
(41, 'Plastic', 'Plastic packaging with foil (e.g. potato chip bags, empty blister pack, expired credit card etc.)', 'NO', 'Dispose as general waste'),
(42, 'Plastic', 'Oxo- and bio-degradable bags', 'NO', 'Dispose as general waste'),
(43, 'Plastic', 'Drinking straw', 'NO', 'Dispose as general waste'),
(44, 'Plastic', 'Cassette and video tape', 'NO', 'Dispose as general waste'),
(45, 'Plastic', 'Plastic packaging contaminated with food / oil stains', 'NO', 'Dispose as general waste'),
(46, 'Plastic', 'Melamine products (e.g. Melamine cups, melamine plates etc)', 'NO', 'Dispose as general waste'),
(47, 'Glass', 'Beverage glass bottle (e.g. beer bottle, wine bottle, liquor bottle)', 'YES', 'Please empty and rinse when necessary'),
(48, 'Glass', 'Food glass bottle (e.g. sauce and condiment bottle, jam spread bottle, food jar etc)', 'YES', 'Please empty and rinse when necessary'),
(49, 'Glass', 'Cosmetic / Perfume glass bottle', 'YES', 'Please empty and rinse when necessary'),
(50, 'Glass', 'Medicine and supplement glass bottle', 'YES', 'Please empty and rinse when necessary'),
(51, 'Glass', 'Glassware - Cup, plate, drinking glass, wine glass', 'YES', ''),
(52, 'Glass', 'Borosilicate or Pyrex glassware, bakeware, tempered glass, over-safe food containers, crystal glass, glass with metal wires', 'NO', 'Dispose as general waste'),
(53, 'Glass', 'Windows', 'NO', 'Dispose as general waste'),
(54, 'Glass', 'Mirrors', 'NO', 'Donate if it is in good condition'),
(55, 'Glass', 'Ceramic product (e.g. ceramic plate, tea pot, porcelain etc)', 'NO', 'Donate if it is in good condition'),
(56, 'Glass', 'Light bulb (e.g. lamp, tube, incandescent lamp, incandescent bulb, fluorescent lamp, fluorescent bulb, LED lamp, LED bulb)', 'MAYBE', 'Can be recycled at specific collection points'),
(57, 'Metal', 'Beverage metal can (e.g. carbonated drink can, soft drink can, beer can etc)', 'YES', 'Please empty and rinse when necessary. Rusted metals should be disposed as general waste.'),
(58, 'Metal', 'Food metal can (e.g. biscuit and food tin, metal container etc)', 'YES', 'Please empty and rinse when necessary. Rusted metals should be disposed as general waste.'),
(59, 'Metal', 'Medals', 'YES', 'Rusted metals should be disposed as general waste.'),
(60, 'Metal', 'Metal bottle cap', 'YES', 'Rusted metals should be disposed as general waste.'),
(61, 'Metal', 'Aerosol can', 'YES', 'Please empty contents before recycling.'),
(62, 'Metal', 'Clean aluminium tray and foil', 'YES', 'Please rinse when necessary'),
(63, 'Metal', 'Non-food Metal Container (e.g. paint container, paint cans etc)', 'YES', 'Please empty contents before recycling. Rusted metals should be disposed as general waste.'),
(64, 'Metal', 'Rusty metal cans, dirty aluminium foil, dirty aluminium tray', 'NO', 'Dispose as general waste.'),
(65, 'Metal', 'Metal cutlery, steel wool, metal accessories', 'NO', 'Make sure that they are completely metal.'),
(66, 'Others', 'ICT Equipment: Desktop computer / Laptop / Tablet computer / Mobile phone / Computer battery / Mobile phone battery / Printer / Modem / Router / Desktop monitor / Docking station / Hard disk drive / Battery charger / Portable charger / Power bank / Electronic cables / Computer mouse / Keyboard', 'YES', 'Can be recycled at e-waste collection points here.'),
(67, 'Others', 'Electronic waste (e.g. Used mobile phone, tablet, laptop etc)', 'YES', 'Can be recycled at e-waste collection points here.'),
(68, 'Others', 'Rechargable battery', 'YES', 'Can be recycled at e-waste collection points here.'),
(69, 'Others', 'Household battery, alkaline battery', 'YES', 'Can be recycled at e-waste collection points here.'),
(70, 'Others', 'Refrigerator / Washing Machine / Dryer / Television / Air Conditioner', 'YES', 'These can be recycled through: Retailer 1-for-1 Take-back / Bulky item removal service by TCs for HDB residents / E-waste collection drive (Quarterly) / Doorstep collection (fees may apply) / To find out where you can recycle your e-waste, visit here.'),
(71, 'Others', 'Electric Mobility Devices such as Personal mobility devices / Electric scooter / Electric bicycle / Power-assisted bicycle / Electric mobility scooter', 'YES', 'These can be recycled through: Retailer 1-for-1 Take-back / Bulky item removal service by TCs for HDB residents / E-waste collection drive (Quarterly) / Doorstep collection (fees may apply) / To find out where you can recycle your e-waste, visit here.'),
(72, 'Others', 'Rice Cooker / Microwave Oven / Toaster Oven / Electric Kettle / Food Processor / Food Blender / Electric FanStanding Fan / Cd/Dvd Player / Music Player / Speaker / Audio Sound System / Radio / Vacuum Cleaner / Gaming Console', 'YES', 'These e-waste items can be recycled through: E-waste bins (non-ALBA)* (items must fit the opening of bins) / Retailer 1-for-1 Take-back / Bulky item removal service by TCs for HDB residents (small items are not applicable) / - Cash-for-Trash stations organised by Public Waste Collectors (please contact your PWCs to check that they are able to accept the e-waste) / Cash-for-Trash stations organised by Public Waste Collectors (please contact your PWCs to check that they are able to accept the e-waste) / To find out where you can recycle your e-waste, visit here.'),
(73, 'Others', 'Lamp Stand / Lamo Fixture', 'YES', 'While the lamp bulb can be disposed in the e-waste bin, lamp fixture and stand should be recycled through: - Retailer 1-for-1 Take-back - Bulky item removal service by TCs for HDB residents - Doorstep collection (fees may apply) *Please note that small household appliances will be collected and recycled under recycling programmes organised under the National Voluntary Partnership for the Proper Management of Non-Regulated Used Household Electrical/Electronic Products.'),
(74, 'Others', 'Sport Shoes / School Shoes / Football Shoes (without metal studs)', 'NO', 'Repair or donate your used shoes as far as possible. These are part of the permanent used shoe collection drive: - ActiveSG Sport Centres - Decathlon - Selected Public Parks - Selected Recreation Clubs and more! For more information, visit here.'),
(75, 'Others', 'Old items which are not in good condition (e.g. clothes, shoes, bag, soft toy, umbrella etc)', 'NO', 'Dispose as general waste'),
(76, 'Others', 'Old items which are in good condition (e.g. clothes, shoes, bag, soft toy, umbrella, spectacle etc)', 'NO', 'Donate if it is in good condition'),
(77, 'Others', 'Food waste', 'NO', 'Dispose as general waste'),
(78, 'Others', 'Leftover medicine', 'NO', 'Dispose as general waste'),
(79, 'Others', 'Diaper and sanitary pad', 'NO', 'Dispose as general waste'),
(80, 'Others', 'Stationery - Pen and pencil', 'NO', 'Donate if it is in good condition'),
(81, 'Others', 'Plant and horticultural waste', 'MAYBE', 'Only for landed estates: bag and place outside your unit on collection days'),
(82, 'Others', 'Luggage bag', 'NO', 'Donate if it is in good condition'),
(83, 'Others', 'Bulky waste (e.g. Furniture, standing fan etc)', 'NO', 'Donate if it is in good condition / Contact Town council to remove from your residential premises');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `info1`
--
ALTER TABLE `info1`
  ADD PRIMARY KEY (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


-- ================================================================================================================================================================

-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 07, 2023 at 03:54 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bloobin`
--

-- --------------------------------------------------------

--
-- Table structure for table `info2`
--

CREATE TABLE `info2` (
  `id` int(2) NOT NULL,
  `type` varchar(16) NOT NULL,
  `item` varchar(296) NOT NULL,
  `recyclable` varchar(88) DEFAULT NULL,
  `nonrecyclable` varchar(472) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `info2`
--

INSERT INTO `info2` (`id`, `type`, `item`, `recyclable`, `nonrecyclable`) VALUES
(1, 'PAPER', 'PRINTED PAPER (Glossy and non-glossy)', 'Make sure it is clean before recycling', ''),
(2, 'PAPER', 'WRITING PAPER', 'Make sure it is clean before recycling', ''),
(3, 'PAPER', 'NEWSPAPER', 'Make sure it is clean before recycling', ''),
(4, 'PAPER', 'FLYER (Glossy and non-glossy)', 'Make sure it is clean before recycling', ''),
(5, 'PAPER', 'BROCHURE (Glossy and non-glossy)', 'Make sure it is clean before recycling', ''),
(6, 'PAPER', 'MAGAZINE (Glossy and non-glossy)', 'Make sure it is clean before recycling', ''),
(7, 'PAPER', 'BOOKS TEXTBOOKS', 'Donate if it can be reused', ''),
(8, 'PAPER', 'TELEPHONE DIRECTORY', 'Make sure it is clean before recycling', ''),
(9, 'PAPER', 'ENVELOPE (with and without plastic window)', 'Make sure it is clean before recycling', ''),
(10, 'PAPER', 'RED PACKET', 'Make sure it is clean before recycling', ''),
(11, 'PAPER', 'NAMECARD', 'Make sure it is clean before recycling', ''),
(12, 'PAPER', 'CALENDAR', 'Make sure it is clean before recycling', ''),
(13, 'PAPER', 'GREETING CARD', 'Make sure it is clean before recycling', ''),
(14, 'PAPER', 'GIFT WRAPPING PAPER', 'Make sure it is clean before recycling', ''),
(15, 'PAPER', 'SHREDDED PAPER', 'Make sure it is clean before recycling', ''),
(16, 'PAPER', 'PAPER RECEIPT', 'Make sure it is clean before recycling', ''),
(17, 'PAPER', 'CARTON BOX CARDBOARD BOX', 'Please flatten before recycling', ''),
(18, 'PAPER', 'PAPER PACKAGING PRINTED PAPER BOX PAPER BOX', 'Please flatten before recycling', ''),
(19, 'PAPER', 'EGG TRAYS', 'Make sure it is clean before recycling', ''),
(20, 'PAPER', 'BEVERAGE CARTON: Milk carton / Drink packet / Juice packet', 'Please empty, rinse and flatten before recycling', ''),
(21, 'PAPER', 'PAPER TOWEL TUBE TOILET ROLL TUBE', 'Make sure it is clean before recycling', ''),
(22, 'PAPER', 'TISSUE BOX', 'Please flatten before recycling', ''),
(23, 'PAPER', 'PAPER BAG', 'Make sure it is clean before recycling', ''),
(24, 'PAPER', 'PAPER DISPOSABLES: Paper cup / Paper plate / Glitter paper / Crayon drawing', '', 'Dispose as general waste'),
(25, 'PAPER', 'TISSUE PAPER', '', 'Dispose as general waste'),
(26, 'PAPER', 'PAPER TOWEL', '', 'Dispose as general waste'),
(27, 'PAPER', 'TOILET PAPER', '', 'Dispose as general waste'),
(28, 'PAPER', 'DISPOSABLE WOODEN CHOPSTICKS / WOODEN CHOPSTICKS / PIZZA BOXES', '', 'Dispose as general waste'),
(29, 'PAPER', 'WAX PAPER', '', 'Dispose as general waste'),
(30, 'PAPER', 'PAPER PACKAGING CONTAMINATED WITH FOOD', '', 'Dispose as general waste'),
(31, 'F&B PLASTIC', 'PLASTIC BOTTLE PLASTIC CONTAINER: Mineral water bottle / Soft drink bottle / Carbonated drink bottle / Milk bottle / Water bottle / Medicine bottle', 'Please empty and rinse before recycling', ''),
(32, 'NON-FOOD PLASTIC', 'SHAMPOO BOTTLE BODYWASH BOTTLE FACIAL CLEANSER BOTTLE DETERGENT BOTTLE SOAP BOTTLE', 'Please empty and rinse before recycling', ''),
(33, 'PLASTIC', 'CD/DVD CD/DVD CASING', 'Make sure it is clean before recycling', ''),
(34, 'PLASTIC', 'PLASTIC BAG TOILET PAPER PACKAGING TISSUE BOX PACKAGING', 'Make sure it is clean before recycling', ''),
(35, 'PLASTIC', 'PLASTIC FILM (Magazine wrapper Plastic packaging for packet drink) / BUBBLE WRAP / FRUIT BOX / ZIPLOCK BAG', 'Make sure it is clean before recycling', ''),
(36, 'PLASTIC', 'PLASTIC PACKAGING BREAD BAG EGG TRAYS', 'Please empty contents before recycling', ''),
(37, 'PLASTIC', 'PLASTIC CLOTHES HANGER', 'Make sure it is clean before recycling', ''),
(38, 'PLASTIC', 'PLASTIC TAKEAWAY FOOD CONTAINER PLASTIC CUPS BUBBLE TEA CUPS', 'Please empty and rinse before recycling', ''),
(39, 'PLASTIC', 'POLYSTYRENE FOAM PRODUCT STYROFOAM STYROFOAM CUP STYROFOAM CLAMSHELL CONTAINER', '', 'Dispose as general waste'),
(40, 'PLASTIC', 'PLASTIC DISPOSABLES PLASTIC CUTLERY PLASTIC CROCKERY', '', 'Dispose as general waste'),
(41, 'PLASTIC', 'PLASTIC PACKAGING WITH FOIL / POTATO CHIP BAGS / EMPTY BLISTER PACK / BLISTER PACK / EXPIRED CREDIT CARDS', '', 'Dispose as general waste'),
(42, 'PLASTIC', 'OXO-DEGRADABLE BAG / BIO-DEGRADABLE BAG', '', 'Dispose as general waste'),
(43, 'PLASTIC', 'DRINKING STRAW', '', 'Dispose as general waste'),
(44, 'PLASTIC', 'CASSETTE / VIDEO TAPE', '', 'Dispose as general waste'),
(45, 'PLASTIC', 'PLASTIC PACKAGING CONTAMINATED WITH FOOD/OIL STAINS', '', 'Dispose as general waste'),
(46, 'PLASTIC', 'MELAMINE PRODUCTS: Melamine cups / Melamine plates', '', 'Dispose as general waste'),
(47, 'GLASS', 'BEVERAGE GLASS BOTTLE: Beer bottle / Wine bottle / Liquor bottle', 'Please empty and rinse before recycling', ''),
(48, 'GLASS', 'FOOD GLASS BOTTLE: Sauce bottle / Condiment bottle / Jam spread bottle / Food jars', 'Please empty and rinse before recycling', ''),
(49, 'GLASS', 'COSMETIC GLASS BOTTLE / PERFUME GLASS BOTTLE', 'Please empty and rinse before recycling', ''),
(50, 'GLASS', 'MEDICINE GLASS BOTTLE / SUPPLEMENT GLASS BOTTLE', 'Please empty and rinse before recycling', ''),
(51, 'GLASS', 'GLASSWARE: Glass cup / Glass plate / Drinking glass / Wine glass', 'Make sure it is clean before recycling', ''),
(52, 'GLASS', 'BOROSILICATE GLASSWARE / PYREX GLASSWARE / BAKEWARE TEMPERED GLASS / OVEN-SAFE FOOD CONTAINERS / CRYSTAL GLASS GLASS WITH METAL WIRES', '', 'Dispose as general waste'),
(53, 'GLASS', 'WINDOWS', '', 'Dispose as general waste'),
(54, 'GLASS', 'MIRRORS', '', 'Donate if it can be reused'),
(55, 'GLASS', 'CERAMIC PRODUCT: Ceramic plate / Tea pot / Porcelain', '', 'Donate if it can be reused'),
(56, 'GLASS', 'LIGHT BULB: Lamp / Tube / Incandescent lamp / Incandescent bulb / Fluorescent lamp  Fluorescent bulb / LED lamp / LED bulb', '', 'Can be recycled at e-waste collection points here.'),
(57, 'METAL', 'BEVERAGE METAL CAN: Carbonated drink can / Soft drink can / Beer can', 'Please empty and rinse when necessary Rusted metals should be disposed as general waste', ''),
(58, 'METAL', 'FOOD METAL CAN: Biscuit and Food tin, Metal Container etc', 'Please empty and rinse when necessary Rusted metals should be disposed as general waste', ''),
(59, 'METAL', 'MEDALS', 'Make sure it is clean before recycling Rusted metals should be disposed as general waste', ''),
(60, 'METAL', 'METAL BOTTLE CAP', 'Make sure it is clean before recycling Rusted metals should be disposed as general waste', ''),
(61, 'METAL', 'AEROSOL CAN', 'Please empty contents before reycling', ''),
(62, 'METAL', 'CLEAN ALUMINIUM TRAY / CLEAN ALUMINIUM FOIL', 'Please empty and rinse before recycling', ''),
(63, 'METAL', 'NON-FOOD METAL CONTAINER: Paint container / Paint cans', 'Please empty contents before recycling Rusted metals should be disposed as general waste', ''),
(64, 'METAL', 'RUSTY METAL CANS / DIRTY ALUMINIUM FOIL / DIRTY ALUMINIUM TRAY', '', 'Dispose as general waste'),
(65, 'METAL', 'METAL CUTLERY / STEEL WOOL / METAL ACCESSORIES', 'Make sure that they are completely metal', ''),
(66, 'OTHERS', 'ICT EQUIPMENT - Desktop computer - Laptop - Tablet computer - Mobile phone - Computer battery - Mobile phone battery - Printer - Modem - Router - Desktop monitor - Docking station - Hard disk drive - Battery charger - Portable charger - Power bank, - Electronic cables - Computer mouse - Keyboard', '', 'Can be recycled at e-waste collection points here.'),
(67, 'OTHERS', 'ELECTRONIC WASTE (e.g. Used mobile phone, tablet, laptop)', '', 'Can be recycled at e-waste collection points here.'),
(68, 'OTHERS', 'RECHARGEABLE BATTERY', '', 'Can be recycled at e-waste collection points here.'),
(69, 'OTHERS', 'HOUSEHOLD BATTERY / ALKALINE BATTERY', '', 'Can be recycled at e-waste collection points here.'),
(70, 'OTHERS', 'REFRIGERATOR / WASHING MACHINE / DRYER / TELEVISION / AIR CONDITIONER', '', 'These can be recycled through: - Retailer 1-for-1 Take-back - Bulky item removal service by TCs for HDB residents - E-waste collection drive (Quarterly) - Doorstep collection (fees may apply) To find out where you can recycle your e-waste, visit here.'),
(71, 'OTHERS', 'ELECTRIC MOBILITY DEVICES - Personal mobility devices - Electric scooter - Electric bicycle - Power-assisted bicycle - Electric mobility scooter', '', 'These can be recycled through: - Retailer 1-for-1 Take-back - Bulky item removal service by TCs for HDB residents - E-waste collection drive (Quarterly) - Doorstep collection (fees may apply) To find out where you can recycle your e-waste, visit here.'),
(72, 'OTHERS', 'RICE COOKER / MICROWAVE OVEN / TOASTER OVEN / ELECTRIC KETTLE / FOOD PROCESSOR / FOOD BLENDER / ELECTRIC FAN / STANDING FAN / CD/DVD PLAYER / MUSIC PLAYER / SPEAKER / AUDIO SOUND SYSTEM / RADIO / VACUUM CLEANER / GAMING CONSOLE', '', 'These e-waste items can be recycled through: - E-waste bins (non-ALBA)* (items must fit the opening of bins) - Retailer 1-for-1 Take-back - Bulky item removal service by TCs for HDB residents (small items are not applicable) - Cash-for-Trash stations organised by Public Waste Collectors (please contact your PWCs to check that they are able to accept the e-waste) To find out where you can recycle your e-waste, visit here.'),
(73, 'OTHERS', 'LAMP STAND / LAMP FIXTURE', '', 'While the lamp bulb can be disposed in the e-waste bin, lamp fixture and stand should be recycled through: - Retailer 1-for-1 Take-back - Bulky item removal service by TCs for HDB residents - Doorstep collection (fees may apply) *Please note that small household appliances will be collected and recycled under recycling programmes organised under the National Voluntary Partnership for the Proper Management of Non-Regulated Used Household Electrical/Electronic Products.'),
(74, 'OTHERS', 'SPORTS SHOES / SCHOOL SHOES / FOOTBALL SHOES (without metal studs)', '', 'Repair or donate your used shoes as far as possible. These are part of the permanent used shoe collection drive: - ActiveSG Sport Centres - Decathlon - Selected Public Parks - Selected Recreation Clubs and more! For more information, visit here.'),
(75, 'OTHERS', 'CLOTHES SHOES (other than those listed in #74) / BAG / TOY / UMBRELLA / SPECTACLES / TEXTILE / CURTAINS / BEDSHEET / BLANKET', '', 'Old items should be dipose as general waste if they are not in good condition.'),
(76, 'OTHERS', 'CLOTHES SHOES (other than those listed in #74) / BAG / TOY / UMBRELLA / SPECTACLES / TEXTILE / CURTAINS / BEDSHEET / BLANKET', '', 'Old items should be donated if they are in good condition.'),
(77, 'OTHERS', 'FOOD WASTE', '', 'Dispose as general waste'),
(78, 'OTHERS', 'LEFTOVER MEDICINE', '', 'Dispose as general waste'),
(79, 'OTHERS', 'DIAPER / SANITARY PAD', '', 'Dispose as general waste'),
(80, 'OTHERS', 'STATIONERY / PEN / PENCIL', '', 'Donate if it is in good condition'),
(81, 'OTHERS', 'PLANT WASTE / HORTICULTURAL WASTE', '', 'Only for landed estates: bag and place outside your unit on collection days'),
(82, 'OTHERS', 'LUGGAGE BAG', '', 'Donate if it is in good condition'),
(83, 'OTHERS', 'BULKY WASTE / FURNITURE', '', 'Donate if it is in good condition or contact Town Council to remove from your residential premises');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `info2`
--
ALTER TABLE `info2`
  ADD PRIMARY KEY (`id`);