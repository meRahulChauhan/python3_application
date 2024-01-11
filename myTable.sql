-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 11, 2024 at 03:55 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `USER_MANAGEMENT`
--

-- --------------------------------------------------------

--
-- Table structure for table `myTable`
--

CREATE TABLE `myTable` (
  `userId` bigint(20) NOT NULL,
  `custumId` varchar(32) DEFAULT NULL,
  `passcode` varchar(32) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `email` varchar(32) DEFAULT NULL,
  `phone` varchar(32) DEFAULT NULL,
  `age` varchar(3) DEFAULT NULL,
  `city` varchar(32) DEFAULT NULL,
  `country` varchar(32) DEFAULT NULL,
  `cnfStatus` enum('yes','no') DEFAULT 'no',
  `postalCode` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `myTable`
--

INSERT INTO `myTable` (`userId`, `custumId`, `passcode`, `name`, `email`, `phone`, `age`, `city`, `country`, `cnfStatus`, `postalCode`) VALUES
(100000001, '', 'ubuntuue', 'Uma Frye', 'ornare.tortor.at@google.org', '1-328-844-6661', '12', 'Ap #892-9410 Curabitur Rd.', 'Germany', 'no', '624646'),
(1000004002, 'rc5565931@gmail.com', 'NoneType', 'RahulChauhan', 'rc5565931@gmail.com', '8127006993', '24', 'Lucknow', 'India', 'no', '226017'),
(1000004003, 'savi@email.com', 'noneType2', 'savi', 'savi@email.com', '9219011866', '36', 'mau', 'India', 'no', '275105'),
(1000004004, 'rc5565932@gmail.com', '145879365', 'rahul', 'rc5565932@gmail.com', '7052461609', '24', 'Ara', 'Nepal', 'no', '245896'),
(1000004005, 'some@email.com', 'jkglk535', 'rahul', 'some@email.com', '1458795684', '24', 'delhi', 'Srilanka', 'no', '245896'),
(1000004006, 'xiaoyu@email.com', 'ghuiomkbm', 'xiaoyu', 'xiaoyu@email.com', '1245879632', '26', 'shen', 'china', 'no', '145698'),
(1000004007, 'sdfg@ty.hjk', 'dftymivvc', 'nonew', 'sdfg@ty.hjk', '1478569541', '45', 'dfbeht', 'wdfgng', 'no', '547854');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `myTable`
--
ALTER TABLE `myTable`
  ADD PRIMARY KEY (`userId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `myTable`
--
ALTER TABLE `myTable`
  MODIFY `userId` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1000004008;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
