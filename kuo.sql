-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2023-06-14 15:19:40
-- 伺服器版本： 10.4.28-MariaDB
-- PHP 版本： 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `kuo`
--

-- --------------------------------------------------------

--
-- 資料表結構 `photo`
--

CREATE TABLE `photo` (
  `id` int(11) NOT NULL,
  `file_name` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `time` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `photo`
--

INSERT INTO `photo` (`id`, `file_name`, `name`, `time`) VALUES
(1, 'C:/Users/user/Desktop/郭善莉的資料/大一下/coding class/summary/cat.png', 'cat', '2023-06-13 14:02:44'),
(2, 'C:/Users/user/Desktop/郭善莉的資料/大一下/coding class/summary/下載.png', 'bear', '2023-06-13 14:24:21'),
(4, 'C:/Users/user/Downloads/S__30228543.png', 'KUO', '2023-06-14 19:58:03'),
(5, 'C:/Users/user/Downloads/S__30253092.png', '17', '2023-06-14 20:51:03');

-- --------------------------------------------------------

--
-- 資料表結構 `photodt`
--

CREATE TABLE `photodt` (
  `id` int(11) NOT NULL,
  `type` varchar(255) NOT NULL,
  `file_name` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `time` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `photodt`
--

INSERT INTO `photodt` (`id`, `type`, `file_name`, `name`, `time`) VALUES
(1, 'person', 'C:/Users/user/Downloads/S__30228551.png', '品品', '2023-06-13 15:59:16'),
(2, 'person', 'C:/Users/user/Downloads/S__30228541.png', '夏西', '2023-06-13 15:59:56'),
(3, 'person', 'C:/Users/user/Downloads/S__30228543.png', 'ㄚ莉', '2023-06-13 16:00:22'),
(4, 'person', 'C:/Users/user/Downloads/S__30228544.png', '宥穎', '2023-06-13 16:01:00'),
(5, 'person', 'C:/Users/user/Downloads/S__30228545.png', '張開', '2023-06-13 16:01:17'),
(6, 'person', 'C:/Users/user/Downloads/S__30228546.png', '17', '2023-06-13 16:01:32'),
(7, 'person', 'C:/Users/user/Downloads/S__30228547.png', '宣廷', '2023-06-13 16:02:12'),
(8, 'person', 'C:/Users/user/Downloads/S__30228548.png', '又嘉', '2023-06-13 16:02:38'),
(9, 'person', 'C:/Users/user/Downloads/S__30228549.png', '搞笑', '2023-06-13 16:03:18'),
(10, 'person', 'C:/Users/user/Downloads/S__30228550.png', '燕子', '2023-06-13 16:03:37'),
(11, 'family', 'C:/Users/user/Desktop/郭善莉的資料/大一下/coding class/summary/family.png', 'family01', '2023-06-13 16:05:48'),
(12, 'family', 'C:/Users/user/Desktop/郭善莉的資料/大一下/coding class/summary/family02.png', 'family02', '2023-06-13 16:09:05'),
(13, 'family', 'C:/Users/user/Desktop/郭善莉的資料/大一下/coding class/summary/family03.png', 'family03', '2023-06-13 16:09:19'),
(14, 'family', 'C:/Users/user/Desktop/郭善莉的資料/大一下/coding class/summary/family04.png', 'family04', '2023-06-13 16:09:34'),
(15, 'family', 'C:/Users/user/Desktop/郭善莉的資料/大一下/coding class/summary/family05.png', 'family05', '2023-06-13 16:09:45'),
(16, 'person', 'C:/Users/user/Downloads/S__30253092.png', '17', '2023-06-14 15:51:37'),
(17, 'person', 'C:/Users/user/Downloads/S__30253094.png', 'yiwei', '2023-06-14 15:54:01'),
(18, 'person', 'C:/Users/user/Downloads/S__30253095.png', 'jony', '2023-06-14 15:54:17'),
(19, 'person', 'C:/Users/user/Downloads/S__30253096.png', 'army0', '2023-06-14 15:55:00'),
(20, 'person', 'C:/Users/user/Downloads/S__30253097.png', '哭又嘉', '2023-06-14 15:55:24');

-- --------------------------------------------------------

--
-- 資料表結構 `selectphone`
--

CREATE TABLE `selectphone` (
  `id` int(11) NOT NULL,
  `article` varchar(255) NOT NULL,
  `number` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `selectphone`
--

INSERT INTO `selectphone` (`id`, `article`, `number`) VALUES
(1, '朋友 王大頭 他的手機號碼 0981-231-432 用了20年了都沒有換，有好也有壞，某天多年前的朋友 S姐的手機 0988000090 號碼出現在他的來電顯示裡，接起電話說要和他結婚，興奮的滿口答應，於是S姐就請他先跟某電視台記者 K先生聯絡 (0999-999-999)，說要辦說明會，王大頭覺得怪，於是打電話給警察朋友 P先生聯絡 (0911-956-956) 請他幫忙分析有沒有可能是詐騙\n\n\n\n某天，張三拿著手機撥打 0800-000-000 的電話詢問網購的問題，但是接聽方說現在服務電話改成 (', '0981-231-432\n0988000090\n0999-999-999\n0911-956-956\n0800-000-000\n(02)27839992\n(02)2783-9993\n+886-2-2837-4699'),
(2, '朋友 王大頭 他的手機號碼 0981-231-432 用了20年了都沒有換，有好也有壞，某天多年前的朋友 S姐的手機 0988000090 號碼出現在他的來電顯示裡，接起電話說要和他結婚，興奮的滿口答應，於是S姐就請他先跟某電視台記者 K先生聯絡 (0999-999-999)，說要辦說明會，王大頭覺得怪，於是打電話給警察朋友 P先生聯絡 (0911-956-956) 請他幫忙分析有沒有可能是詐騙\n\n\n\n某天，張三拿著手機撥打 0800-000-000 的電話詢問網購的問題，但是接聽方說現在服務電話改成 (', '0981-231-432\n0988000090\n0999-999-999\n0911-956-956\n0800-000-000\n(02)27839992\n(02)2783-9993\n+886-2-2837-4699');

-- --------------------------------------------------------

--
-- 資料表結構 `student_courses`
--

CREATE TABLE `student_courses` (
  `student_id` int(32) NOT NULL,
  `name` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `course_id` varchar(10) NOT NULL,
  `course_name` varchar(50) NOT NULL,
  `instructor` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- 傾印資料表的資料 `student_courses`
--

INSERT INTO `student_courses` (`student_id`, `name`, `age`, `course_id`, `course_name`, `instructor`) VALUES
(1, 'Alice', 19, 'C001', 'Calculus', 'Dr. Lee'),
(2, 'Bob', 20, 'P101', 'Physics I', 'Prof. Wang'),
(3, 'Claire', 18, 'E101', 'English I', 'Prof. Chen'),
(4, 'David', 21, 'M201', 'Linear Algebra', 'Dr. Wu'),
(5, 'Emily', 19, 'C002', 'Discrete Math', 'Prof. Lin'),
(6, 'Jimmy', 18, 'C002', 'Discrete Math', 'Prof. Lin'),
(7, 'Ken', 20, 'C002', 'Discrete Math', 'Prof. Lin'),
(8, 'Jack', 19, 'C001', 'Calculus', 'Dr. Lee'),
(9, 'sadas', 11, 'asd', 'sadas', 'asdsad'),
(10, 'asdsa', 111, '11211221', '21212112', '2122'),
(11, 'Jimmy', 18, 'H105', 'QQ', 'Jack'),
(12, 'A', 11, 'C111', 'ada', 'aaa'),
(13, 'B', 12, 'A123', 'adx', 'bbb'),
(14, 'C', 13, 'D513', 'aca', 'ccc'),
(15, 'ab', 45, 'C111', 'ssad', 'aaa'),
(16, '111', 111, '11', '111', '11');

-- --------------------------------------------------------

--
-- 資料表結構 `users2`
--

CREATE TABLE `users2` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `users2`
--

INSERT INTO `users2` (`id`, `username`, `password`) VALUES
(1, 'KUO', 'b5e32b551a4a83f7138fda78c4fd48ff918b7c2e3b0ea10f449815908c714525'),
(6, 'test2', '6b51d431df5d7f141cbececcf79edf3dd861c3b4069f0b11661a3eefacbba918'),
(8, 'test4', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),
(10, 'Jiaa', '82a5b34244868037ea98f7c35fae370ae7992caaf32f0bc37f1de8d6aecf6628'),
(11, 'KK', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),
(12, 'Jia', '82a5b34244868037ea98f7c35fae370ae7992caaf32f0bc37f1de8d6aecf6628');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `photo`
--
ALTER TABLE `photo`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `photodt`
--
ALTER TABLE `photodt`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `selectphone`
--
ALTER TABLE `selectphone`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `student_courses`
--
ALTER TABLE `student_courses`
  ADD PRIMARY KEY (`student_id`);

--
-- 資料表索引 `users2`
--
ALTER TABLE `users2`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `photo`
--
ALTER TABLE `photo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `photodt`
--
ALTER TABLE `photodt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `selectphone`
--
ALTER TABLE `selectphone`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `student_courses`
--
ALTER TABLE `student_courses`
  MODIFY `student_id` int(32) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `users2`
--
ALTER TABLE `users2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
