-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: j5b307.p.ssafy.io    Database: ssafy_painting_game
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_accounts`
--

DROP TABLE IF EXISTS `accounts_accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_accounts` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) NOT NULL,
  `time_to_expire` datetime(6) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1132 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_accounts`
--

LOCK TABLES `accounts_accounts` WRITE;
/*!40000 ALTER TABLE `accounts_accounts` DISABLE KEYS */;
INSERT INTO `accounts_accounts` VALUES (1123,'광배긐','2021-10-08 03:15:01.901317'),(1124,'이두근','2021-10-08 03:15:39.602729'),(1125,'화쫑이','2021-10-08 03:27:09.192044'),(1127,'나는야석환','2021-10-08 03:31:56.632882');
/*!40000 ALTER TABLE `accounts_accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add accounts',1,'add_accounts'),(2,'Can change accounts',1,'change_accounts'),(3,'Can delete accounts',1,'delete_accounts'),(4,'Can view accounts',1,'view_accounts'),(5,'Can add categories',2,'add_categories'),(6,'Can change categories',2,'change_categories'),(7,'Can delete categories',2,'delete_categories'),(8,'Can view categories',2,'view_categories'),(9,'Can add room',3,'add_room'),(10,'Can change room',3,'change_room'),(11,'Can delete room',3,'delete_room'),(12,'Can view room',3,'view_room'),(13,'Can add user in room',4,'add_userinroom'),(14,'Can change user in room',4,'change_userinroom'),(15,'Can delete user in room',4,'delete_userinroom'),(16,'Can view user in room',4,'view_userinroom'),(17,'Can add score',5,'add_score'),(18,'Can change score',5,'change_score'),(19,'Can delete score',5,'delete_score'),(20,'Can view score',5,'view_score'),(21,'Can add paint',6,'add_paint'),(22,'Can change paint',6,'change_paint'),(23,'Can delete paint',6,'delete_paint'),(24,'Can view paint',6,'view_paint'),(25,'Can add log entry',7,'add_logentry'),(26,'Can change log entry',7,'change_logentry'),(27,'Can delete log entry',7,'delete_logentry'),(28,'Can view log entry',7,'view_logentry'),(29,'Can add permission',8,'add_permission'),(30,'Can change permission',8,'change_permission'),(31,'Can delete permission',8,'delete_permission'),(32,'Can view permission',8,'view_permission'),(33,'Can add group',9,'add_group'),(34,'Can change group',9,'change_group'),(35,'Can delete group',9,'delete_group'),(36,'Can view group',9,'view_group'),(37,'Can add user',10,'add_user'),(38,'Can change user',10,'change_user'),(39,'Can delete user',10,'delete_user'),(40,'Can view user',10,'view_user'),(41,'Can add content type',11,'add_contenttype'),(42,'Can change content type',11,'change_contenttype'),(43,'Can delete content type',11,'delete_contenttype'),(44,'Can view content type',11,'view_contenttype'),(45,'Can add session',12,'add_session'),(46,'Can change session',12,'change_session'),(47,'Can delete session',12,'delete_session'),(48,'Can view session',12,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'accounts','accounts'),(7,'admin','logentry'),(9,'auth','group'),(8,'auth','permission'),(10,'auth','user'),(11,'contenttypes','contenttype'),(2,'paint_game','categories'),(6,'paint_game','paint'),(3,'paint_game','room'),(5,'paint_game','score'),(4,'paint_game','userinroom'),(12,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'accounts','0001_initial','2021-10-04 04:29:18.288532'),(2,'contenttypes','0001_initial','2021-10-04 04:29:18.343723'),(3,'auth','0001_initial','2021-10-04 04:29:19.028348'),(4,'admin','0001_initial','2021-10-04 04:29:19.199984'),(5,'admin','0002_logentry_remove_auto_add','2021-10-04 04:29:19.210915'),(6,'admin','0003_logentry_add_action_flag_choices','2021-10-04 04:29:19.223222'),(7,'contenttypes','0002_remove_content_type_name','2021-10-04 04:29:19.341305'),(8,'auth','0002_alter_permission_name_max_length','2021-10-04 04:29:19.409116'),(9,'auth','0003_alter_user_email_max_length','2021-10-04 04:29:19.437885'),(10,'auth','0004_alter_user_username_opts','2021-10-04 04:29:19.449552'),(11,'auth','0005_alter_user_last_login_null','2021-10-04 04:29:19.508119'),(12,'auth','0006_require_contenttypes_0002','2021-10-04 04:29:19.513862'),(13,'auth','0007_alter_validators_add_error_messages','2021-10-04 04:29:19.526451'),(14,'auth','0008_alter_user_username_max_length','2021-10-04 04:29:19.595854'),(15,'auth','0009_alter_user_last_name_max_length','2021-10-04 04:29:19.671646'),(16,'auth','0010_alter_group_name_max_length','2021-10-04 04:29:19.698921'),(17,'auth','0011_update_proxy_permissions','2021-10-04 04:29:19.714778'),(18,'auth','0012_alter_user_first_name_max_length','2021-10-04 04:29:19.783907'),(19,'paint_game','0001_initial','2021-10-04 04:29:20.418761'),(20,'sessions','0001_initial','2021-10-04 04:29:20.467327');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paint_game_categories`
--

DROP TABLE IF EXISTS `paint_game_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paint_game_categories` (
  `word_id` int NOT NULL AUTO_INCREMENT,
  `category` varchar(50) NOT NULL,
  PRIMARY KEY (`word_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paint_game_categories`
--

LOCK TABLES `paint_game_categories` WRITE;
/*!40000 ALTER TABLE `paint_game_categories` DISABLE KEYS */;
INSERT INTO `paint_game_categories` VALUES (1,'banana'),(2,'bulb'),(3,'calculator'),(4,'carrot'),(5,'clock'),(6,'crescent'),(7,'diamond'),(8,'icecream'),(9,'strawberry'),(10,'t-shirt');
/*!40000 ALTER TABLE `paint_game_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paint_game_paint`
--

DROP TABLE IF EXISTS `paint_game_paint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paint_game_paint` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `category_id` int NOT NULL,
  `room_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paint_game_paint_category_id_930e086d_fk_paint_gam` (`category_id`),
  KEY `paint_game_paint_room_id_bed98145_fk_paint_game_room_room_id` (`room_id`),
  KEY `paint_game_paint_user_id_0ec2bb77_fk_accounts_accounts_user_id` (`user_id`),
  CONSTRAINT `paint_game_paint_category_id_930e086d_fk_paint_gam` FOREIGN KEY (`category_id`) REFERENCES `paint_game_categories` (`word_id`) ON DELETE CASCADE,
  CONSTRAINT `paint_game_paint_room_id_bed98145_fk_paint_game_room_room_id` FOREIGN KEY (`room_id`) REFERENCES `paint_game_room` (`room_id`) ON DELETE CASCADE,
  CONSTRAINT `paint_game_paint_user_id_0ec2bb77_fk_accounts_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_accounts` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1112 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paint_game_paint`
--

LOCK TABLES `paint_game_paint` WRITE;
/*!40000 ALTER TABLE `paint_game_paint` DISABLE KEYS */;
INSERT INTO `paint_game_paint` VALUES (1111,'room_717/bulb/이두근.jpg',2,717,1124);
/*!40000 ALTER TABLE `paint_game_paint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paint_game_room`
--

DROP TABLE IF EXISTS `paint_game_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paint_game_room` (
  `room_id` int NOT NULL AUTO_INCREMENT,
  `room_name` varchar(50) NOT NULL,
  `room_password` varchar(50) DEFAULT NULL,
  `problems` int NOT NULL,
  `max_head_counts` int NOT NULL,
  `is_locked` tinyint(1) NOT NULL,
  `is_started` tinyint(1) NOT NULL,
  `room_owner_id` int NOT NULL,
  PRIMARY KEY (`room_id`),
  KEY `paint_game_room_room_owner_id_ba61e49e_fk_accounts_` (`room_owner_id`),
  CONSTRAINT `paint_game_room_room_owner_id_ba61e49e_fk_accounts_` FOREIGN KEY (`room_owner_id`) REFERENCES `accounts_accounts` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=720 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paint_game_room`
--

LOCK TABLES `paint_game_room` WRITE;
/*!40000 ALTER TABLE `paint_game_room` DISABLE KEYS */;
INSERT INTO `paint_game_room` VALUES (717,'두(근)두(근)','',6,10,0,1,1124);
/*!40000 ALTER TABLE `paint_game_room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paint_game_score`
--

DROP TABLE IF EXISTS `paint_game_score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paint_game_score` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `score` double NOT NULL,
  `room_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paint_game_score_room_id_34db3ba3_fk_paint_game_room_room_id` (`room_id`),
  KEY `paint_game_score_user_id_9aca36ad_fk_accounts_accounts_user_id` (`user_id`),
  CONSTRAINT `paint_game_score_room_id_34db3ba3_fk_paint_game_room_room_id` FOREIGN KEY (`room_id`) REFERENCES `paint_game_room` (`room_id`) ON DELETE CASCADE,
  CONSTRAINT `paint_game_score_user_id_9aca36ad_fk_accounts_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_accounts` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=407 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paint_game_score`
--

LOCK TABLES `paint_game_score` WRITE;
/*!40000 ALTER TABLE `paint_game_score` DISABLE KEYS */;
INSERT INTO `paint_game_score` VALUES (406,0.29207125306129456,717,1124);
/*!40000 ALTER TABLE `paint_game_score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paint_game_userinroom`
--

DROP TABLE IF EXISTS `paint_game_userinroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paint_game_userinroom` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `room_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paint_game_userinroo_room_id_d5e81297_fk_paint_gam` (`room_id`),
  KEY `paint_game_userinroo_user_id_902d590d_fk_accounts_` (`user_id`),
  CONSTRAINT `paint_game_userinroo_room_id_d5e81297_fk_paint_gam` FOREIGN KEY (`room_id`) REFERENCES `paint_game_room` (`room_id`) ON DELETE CASCADE,
  CONSTRAINT `paint_game_userinroo_user_id_902d590d_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_accounts` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1452 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paint_game_userinroom`
--

LOCK TABLES `paint_game_userinroom` WRITE;
/*!40000 ALTER TABLE `paint_game_userinroom` DISABLE KEYS */;
INSERT INTO `paint_game_userinroom` VALUES (1449,717,1124);
/*!40000 ALTER TABLE `paint_game_userinroom` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-08 12:20:06
