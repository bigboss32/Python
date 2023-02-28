-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: proyecto
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `registro`
--

DROP TABLE IF EXISTS `registro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registro` (
  `idRegistro` int NOT NULL AUTO_INCREMENT,
  `numero_entrega` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `cedula` varchar(45) NOT NULL,
  `edad_de_ingreso` int NOT NULL,
  `Actualmente_trabaja` int NOT NULL,
  `Tipo_de_población_a_la_que_pertenece` int NOT NULL,
  `ESTADO_CIVIL` int NOT NULL,
  `Cómo_financia_sus_estudios` int NOT NULL,
  `CIRCUNSCRIPCION` int NOT NULL,
  `Dispone_de_un_computador_permanentemente` int NOT NULL,
  `Posee_conexión_permanente_a_internet` int NOT NULL,
  `sexo` int NOT NULL,
  `estrato` int NOT NULL,
  `FKresultado` int NOT NULL,
  PRIMARY KEY (`idRegistro`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro`
--

LOCK TABLES `registro` WRITE;
/*!40000 ALTER TABLE `registro` DISABLE KEYS */;
INSERT INTO `registro` VALUES (26,1,'miguel','1212324',1,1,1,1,1,1,1,1,1,1,0),(27,1,'tilin','1213324',1,1,1,1,1,1,1,1,1,1,0),(28,1,'monis','1213324',2,1,1,1,1,1,1,1,1,1,0),(29,1,'miguel','1212324',1,1,1,1,1,1,1,1,1,1,0),(30,1,'tilin','1213324',1,1,1,1,1,1,1,1,1,1,0),(31,1,'monis','1213324',2,1,1,1,1,1,1,1,1,1,0),(32,1,'miguel','1212324',1,1,1,1,1,1,1,1,1,1,0),(33,1,'tilin','1213324',1,1,1,1,1,1,1,1,1,1,0),(34,1,'monis','1213324',2,1,1,1,1,1,1,1,1,1,0),(35,1,'miguel','1212324',1,1,1,1,1,1,1,1,1,1,0),(36,1,'tilin','1213324',1,1,1,1,1,1,1,1,1,1,0),(37,1,'monis','1213324',2,1,1,1,1,1,1,1,1,1,0),(38,1,'miguel','1212324',1,1,1,1,1,1,1,1,1,1,0),(39,1,'tilin','1213324',1,1,1,1,1,1,1,1,1,1,0),(40,1,'monis','1213324',2,1,1,1,1,1,1,1,1,1,0),(41,1,'miguel','1212324',1,1,1,1,1,1,1,1,1,1,0),(42,1,'tilin','1213324',1,1,1,1,1,1,1,1,1,1,0),(43,1,'monis','1213324',2,1,1,1,1,1,1,1,1,1,0),(44,1,'miguel','1212324',1,1,1,1,1,1,1,1,1,1,0),(45,1,'tilin','1213324',1,1,1,1,1,1,1,1,1,1,0),(46,1,'monis','1213324',2,1,1,1,1,1,1,1,1,1,0),(47,1,'miguel','1212324',1,1,1,1,1,1,1,1,1,1,0),(48,1,'tilin','1213324',1,1,1,1,1,1,1,1,1,1,0),(49,1,'monis','1213324',2,1,1,1,1,1,1,1,1,1,0);
/*!40000 ALTER TABLE `registro` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-28 13:15:51
