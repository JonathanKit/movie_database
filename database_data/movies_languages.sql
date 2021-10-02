CREATE DATABASE  IF NOT EXISTS `movies` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `movies`;
-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: movies
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `languages`
--

DROP TABLE IF EXISTS `languages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `languages` (
  `languageID` int NOT NULL AUTO_INCREMENT,
  `language` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`languageID`)
) ENGINE=InnoDB AUTO_INCREMENT=130 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `languages`
--

LOCK TABLES `languages` WRITE;
/*!40000 ALTER TABLE `languages` DISABLE KEYS */;
INSERT INTO `languages` VALUES (16,'German'),(17,'English'),(18,'Spanish'),(19,'Norwegian'),(20,'French'),(25,'Hindi'),(26,'Bengali'),(27,'Nan'),(28,'Cantonese'),(29,'Japanese'),(30,'Tulu'),(31,'Serbian'),(32,'Serbo-Croatian'),(33,'Croatian'),(34,'Greek'),(35,'Finnish'),(36,'Italian'),(37,'Telugu'),(38,'Tamil'),(39,'Swedish'),(40,'Bosnian'),(41,'Mandarin'),(42,'Danish'),(43,'Portuguese'),(44,'Pushto'),(45,'Thai'),(46,'None'),(47,'Korean'),(48,'Polish'),(49,'Dutch'),(50,'Estonian'),(51,'Malayalam'),(52,'Russian'),(53,'Hebrew'),(54,'Kannada'),(55,'Sinhalese'),(56,'Czech'),(57,'Swiss German'),(58,'Filipino'),(59,'Turkish'),(60,'Arabic'),(61,'Punjabi'),(62,'Flemish'),(63,'Chinese'),(64,'Saami'),(65,'Hungarian'),(66,'Vietnamese'),(67,'Persian'),(68,'Ukrainian'),(69,'Romanian'),(70,'Urdu'),(71,'Sicilian'),(72,'Breton'),(73,'Marathi'),(74,'Amharic'),(75,'Bhojpuri'),(76,'Icelandic'),(77,'Panjabi'),(78,'Lao'),(79,'More'),(80,'Albanian'),(81,'Armenian'),(82,'Azerbaijani'),(83,'Cree'),(84,'Divehi'),(85,'Burmese'),(86,'Tibetan'),(87,'Ibo'),(88,'Latvian'),(89,'Bulgarian'),(90,'Malay'),(91,'Maya'),(92,'Kurdish'),(93,'Aboriginal'),(94,'Low German'),(95,'Dari'),(96,'Bambara'),(97,'Georgian'),(98,'Indonesian'),(99,'Swahili'),(100,'Hmong'),(101,'Latin'),(102,'Nepali'),(103,'Uzbek'),(104,'Zulu'),(105,'Gujarati'),(106,'Irish'),(107,'Xhosa'),(108,'Chechen'),(109,'Belarusian'),(110,'Yiddish'),(111,'Hawaiian'),(112,'Slovak'),(113,'Afrikaans'),(114,'Oriya'),(115,'Guarani'),(116,'American Sign Language'),(117,'Tagalog'),(118,'Basque'),(119,'Romany'),(120,'Limbu'),(121,'Khmer'),(122,'Karen'),(123,'Akan'),(124,'Neapolitan'),(125,'Hopi'),(126,'Catalan'),(127,'Aramaic'),(128,'Min Nan'),(129,'Inuktitut');
/*!40000 ALTER TABLE `languages` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-02 11:45:32
