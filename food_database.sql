-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 21, 2023 at 10:38 PM
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
-- Database: `food_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `addresses`
--

CREATE TABLE `addresses` (
  `address_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `address_line` varchar(255) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `postal_code` varchar(20) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `addresses`
--

INSERT INTO `addresses` (`address_id`, `user_id`, `address_line`, `city`, `state`, `postal_code`, `created_at`, `updated_at`) VALUES
(1, 2, '123 Main St', 'Cityville', 'Stateville', '12345', '2023-08-31 19:29:43', '2023-08-31 19:29:43'),
(2, 3, '456 Elm St', 'Townsville', 'Stateville', '67890', '2023-08-31 19:29:43', '2023-08-31 19:29:43');

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `admin_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`admin_id`, `user_id`, `created_at`, `updated_at`) VALUES
(1, 1, '2023-08-31 19:29:43', '2023-08-31 19:29:43');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `cid` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `image_url` varchar(255) NOT NULL,
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`cid`, `name`, `image_url`, `updated_at`, `created_at`) VALUES
(1, 'Pizza', 'search-pizza.png', '2023-09-19 21:13:05', '2023-09-19 21:25:12'),
(2, 'Burger', 'Burger.png', '2023-09-19 21:13:05', '2023-09-19 21:25:12'),
(3, 'Sandwitch', 'sandwitch.jpg', '2023-09-19 21:13:05', '2023-09-19 21:25:12'),
(4, 'Steaks', 'steak.jpg', '2023-09-19 21:13:05', '2023-09-19 21:25:12'),
(5, 'Chineese', 'chineese.jpg', '2023-09-19 21:13:05', '2023-09-19 21:25:12'),
(6, 'Ice Cream', 'icecream.jpg', '2023-09-19 21:13:05', '2023-09-19 21:25:12'),
(7, 'Sweets', 'sweets.jpg', '2023-09-19 21:13:05', '2023-09-19 21:25:12'),
(8, 'Biryani', 'Biryani.jpg', '2023-09-19 21:13:05', '2023-09-19 21:25:12'),
(9, 'Karahi', 'Karahi.jpg', '2023-09-19 21:13:05', '2023-09-19 21:25:12'),
(10, 'Bbq', 'bbq.jpg', '2023-09-19 21:13:05', '2023-09-19 21:25:12'),
(18, 'Hot Wings', 'hotwings.jpg', '2023-09-19 21:18:10', '2023-09-19 21:25:12'),
(19, 'Soups', 'soups.jfif', '2023-09-19 21:29:42', '2023-09-19 21:29:42');

-- --------------------------------------------------------

--
-- Table structure for table `cities`
--

CREATE TABLE `cities` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cities`
--

INSERT INTO `cities` (`id`, `name`, `image_url`, `updated_at`, `created_at`) VALUES
(1, 'Karachi', 'Karachi.jpg', '2023-09-19 21:13:41', '2023-09-19 21:25:12'),
(2, 'Islamabad', 'Islamabad.jpg', '2023-09-19 21:13:41', '2023-09-19 21:25:12'),
(3, 'Multan', 'Multan.jpg', '2023-09-19 21:13:41', '2023-09-19 21:25:12'),
(4, 'Lahore', 'Lahore.jpg', '2023-09-19 21:13:41', '2023-09-19 21:25:12'),
(5, 'Quetta', 'Quetta.jpg', '2023-09-19 21:13:41', '2023-09-19 21:25:12'),
(6, 'Hyderabad', 'Hyderabad.jpg', '2023-09-19 21:13:41', '2023-09-19 21:25:12'),
(7, 'Faisalabad', 'Faisalabad.jpg', '2023-09-19 21:13:41', '2023-09-19 21:25:12'),
(8, 'Murree', 'Murree.jpg', '2023-09-19 21:13:41', '2023-09-19 21:25:12'),
(9, 'Rahimyarkhan', 'Rahimyarkhan.jpg', '2023-09-19 21:13:41', '2023-09-19 21:25:12'),
(10, 'Peshawar', 'Peshawar.jpg', '2023-09-19 21:13:41', '2023-09-19 21:25:12');

-- --------------------------------------------------------

--
-- Table structure for table `foods`
--

CREATE TABLE `foods` (
  `pid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `restaurant_name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL,
  `category` varchar(70) DEFAULT NULL,
  `discount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `foods`
--

INSERT INTO `foods` (`pid`, `name`, `price`, `image_url`, `created_at`, `updated_at`, `restaurant_name`, `address`, `code`, `category`, `discount`) VALUES
(1, 'Cheeseburger', 700.00, 'cheese-burger.png', '2023-08-31 19:29:43', '2023-09-20 05:34:31', 'Stackers', 'Karachi', 'EDNALAN010', 'Burger', NULL),
(2, 'Margherita Pizza', 900.00, 'food2.jpg', '2023-08-31 19:29:43', '2023-09-20 05:34:38', 'Bricklane Pizza', 'Islamabad', 'EDNALAN01', 'Pizza', NULL),
(3, 'Hot Wings', 550.00, 'hotwings.jpg', '2023-08-31 19:29:43', '2023-09-20 05:35:00', 'Kfc', 'Karachi', 'EDNALAN06', 'Pizza', NULL),
(8, 'Chiken Biryani', 350.00, 'food1.jpg', '2023-09-04 21:54:00', '2023-09-20 05:35:07', 'Rehman Biryani', 'Karachi', 'EDNALAN08', 'Biryani', NULL),
(9, 'Chicken Roll', 150.00, 'chickenroll.jfif', '2023-09-04 21:54:55', '2023-09-20 05:35:19', 'Cafe Clifton', 'Karachi', 'EDNALAN02', 'Roll', NULL),
(10, 'Thai Soup', 500.00, 'thai-soup.png', '2023-09-04 21:56:21', '2023-09-20 05:35:14', 'Foody Man', 'Lahore', 'EDNALAN04', 'Soups', NULL),
(11, 'Crispy Sandwitch', 200.00, 'crispy-sandwitch.png', '2023-09-04 22:00:00', '2023-09-20 05:35:35', 'Fastfood Dine', 'Faisalabad', 'EDNALAN03', 'Sandwitch', NULL),
(12, 'Beef Steak', 1800.00, 'beefsteak.jpg', '2023-09-04 22:49:38', '2023-09-20 05:35:42', 'Magal Restaurant', 'Karachi', 'EDNALAN07', 'Steaks', NULL),
(13, 'Mutton Karahi', 2800.00, 'muttonkarahi.jfif', '2023-09-04 22:50:04', '2023-09-20 05:34:54', 'Shinwari Restaurant', 'Quetta', 'EDNALAN09', 'Karahi', NULL),
(14, 'Ice Cream', 290.00, 'rollicecream.jfif', '2023-09-04 22:50:08', '2023-09-20 05:34:43', 'Havmor Ice Cream', 'Hyderabad', 'EDNALAN05', 'Icecream', NULL),
(20, 'Chicken Biryani', 350.00, 'chickenbiryani.jpg', '2023-09-10 14:43:11', '2023-09-10 22:42:59', 'Student Biryani', 'Karachi', 'EDNALAN11', 'Biryani', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `total_amount` varchar(250) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_id`, `user_id`, `total_amount`, `created_at`, `updated_at`, `address`) VALUES
(1, 2, '23.98', '2023-08-31 19:29:43', '2023-08-31 19:29:43', NULL),
(2, 2, '12.99', '2023-08-31 19:29:43', '2023-08-31 19:29:43', NULL),
(3, 1, 'ertg', '2023-09-07 15:19:40', '2023-09-07 15:19:40', NULL),
(4, 2, 'ada', '2023-09-07 15:28:35', '2023-09-07 15:28:35', 'da'),
(5, 2, 'adajlj', '2023-09-07 15:31:35', '2023-09-07 15:31:35', 'da'),
(6, 2, 'adajlj', '2023-09-07 15:31:59', '2023-09-07 15:31:59', 'da'),
(7, 2, '1200', '2023-09-08 05:22:14', '2023-09-08 05:22:14', 'ghf'),
(8, 2, '1200', '2023-09-08 05:24:14', '2023-09-08 05:24:14', 'dadgjasgj'),
(9, 2, 'RS 2100.0', '2023-09-10 23:30:53', '2023-09-10 23:30:53', 'Aptech Shahre Faisal Karachi'),
(10, 2, 'RS 2300.0', '2023-09-19 07:15:18', '2023-09-19 07:15:18', 'dtdtd');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `pid` int(11) NOT NULL,
  `code` varchar(255) NOT NULL,
  `name` varchar(70) DEFAULT NULL,
  `image` varchar(255) NOT NULL,
  `category` varchar(70) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `discount` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`pid`, `code`, `name`, `image`, `category`, `price`, `discount`) VALUES
(3, 'EDNALAN01', 'Samsung Galaxy A10S', '2.jpg', 'Mobile', 520, 100),
(4, 'EDNALAN02', 'Samsung Galaxy Win Duos', '3.jpg', 'Mobile', 1600, 500),
(5, 'EDNALAN03', 'Women Summer Spaghetti Strap Down', '4.jpg', 'Woman Dresess', 2020, 1250),
(6, 'EDNALAN04', 'Honda TMX Alpha Clamp', '5.jpg', 'Motorcycle', 320, 50);

-- --------------------------------------------------------

--
-- Table structure for table `restaurants`
--

CREATE TABLE `restaurants` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `restaurants`
--

INSERT INTO `restaurants` (`id`, `name`, `image_url`, `updated_at`, `created_at`) VALUES
(3, 'Kfc', 'Kfc.png', '2023-09-19 21:13:41', '2023-09-19 21:25:12'),
(4, 'Stackers', 'Stackers.png', '2023-09-19 21:16:34', '2023-09-19 21:25:12');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password_hash` varchar(128) NOT NULL,
  `role` enum('admin','user','restaurant_owner') NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `email`, `password_hash`, `role`, `created_at`, `updated_at`) VALUES
(1, 'admin', 'faraz@example.com', 'fk101', 'admin', '2023-08-31 19:29:43', '2023-08-31 19:29:43'),
(2, 'user1', 'farazuser@example.com', 'fk101', 'user', '2023-08-31 19:29:43', '2023-08-31 19:29:43'),
(3, 'restaurant_owner1', 'farazowner@example.com', 'fk101', 'restaurant_owner', '2023-08-31 19:29:43', '2023-08-31 19:29:43'),
(4, 'faraz', 'faraz@gmail.com', 'pbkdf2:sha256:600000$gsolwiAnzh1EGXBd$8034af792ffb86b809e48dad46e33ca1e721373e279813cf2b6c4cbeab555dbc', 'user', '2023-08-31 20:23:07', '2023-08-31 20:23:07'),
(5, 'faraz123', 'faraz123@gmail.com', 'pbkdf2:sha256:600000$ERcGDB7Bw2tF1QVL$a7fae2563f3faa3c9a0e13107e6e796459bba7ecc8e33b92543502c644d67caa', 'user', '2023-08-31 23:52:16', '2023-08-31 23:52:16');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addresses`
--
ALTER TABLE `addresses`
  ADD PRIMARY KEY (`address_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`admin_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `cities`
--
ALTER TABLE `cities`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `foods`
--
ALTER TABLE `foods`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `restaurants`
--
ALTER TABLE `restaurants`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addresses`
--
ALTER TABLE `addresses`
  MODIFY `address_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `admins`
--
ALTER TABLE `admins`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `cities`
--
ALTER TABLE `cities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `foods`
--
ALTER TABLE `foods`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=250;

--
-- AUTO_INCREMENT for table `restaurants`
--
ALTER TABLE `restaurants`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `addresses`
--
ALTER TABLE `addresses`
  ADD CONSTRAINT `addresses_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `admins`
--
ALTER TABLE `admins`
  ADD CONSTRAINT `admins_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
