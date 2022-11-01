-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 31-10-2022 a las 03:59:21
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `usuarios`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos`
--

CREATE TABLE `datos` (
  `id` int(25) NOT NULL,
  `fec_alta` date DEFAULT current_timestamp(),
  `user_name` varchar(50) NOT NULL,
  `codigo_zip` varchar(20) DEFAULT NULL,
  `credit_car_num` varchar(250) NOT NULL,
  `cuenta_numero` int(20) NOT NULL,
  `direccion` varchar(20) DEFAULT NULL,
  `geo_latitud` varchar(20) NOT NULL,
  `geo_longitud` varchar(20) NOT NULL,
  `color_favorito` varchar(20) DEFAULT NULL,
  `foto_dni` varchar(20) NOT NULL,
  `ip` varchar(20) NOT NULL,
  `auto` varchar(20) DEFAULT NULL,
  `auto_modelo` varchar(20) DEFAULT NULL,
  `auto_tipo` varchar(20) DEFAULT NULL,
  `auto_color` varchar(20) DEFAULT NULL,
  `cant_compras` int(20) NOT NULL,
  `avatar` varchar(20) NOT NULL,
  `fec_nacimiento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `datos`
--

INSERT INTO `datos` (`id`, `fec_alta`, `user_name`, `codigo_zip`, `credit_car_num`, `cuenta_numero`, `direccion`, `geo_latitud`, `geo_longitud`, `color_favorito`, `foto_dni`, `ip`, `auto`, `auto_modelo`, `auto_tipo`, `auto_color`, `cant_compras`, `avatar`, `fec_nacimiento`) VALUES
(1, '2022-10-25', 'JOHN FREDY', '76001', '1236547821', 12345678, 'Casrrera 66B#2C-44', '45,654789', '32,547879', '#F000', '///////', '192.168.1.1', 'Mazda', 'Sedan', 'Carro', 'Rojo', 12, '////', '2022-10-04'),
(2, '2022-10-07', 'JOHN ALEXANDER', '76001', '12345678', 15426874, 'Carrera 66b#2C-44', '45,69832', '27,6589234', '#FF00', '//////', '127.168.3.5', 'Mazda', 'Sedan', 'Carro', 'Green', 2, '/////', '2022-10-06');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `datos`
--
ALTER TABLE `datos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `datos`
--
ALTER TABLE `datos`
  MODIFY `id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
