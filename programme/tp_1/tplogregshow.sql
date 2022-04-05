-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mar. 05 avr. 2022 à 14:05
-- Version du serveur : 10.4.21-MariaDB
-- Version de PHP : 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `tplogregshow`
--

-- --------------------------------------------------------

--
-- Structure de la table `roles`
--

CREATE TABLE `roles` (
  `id_role` int(11) NOT NULL,
  `name_role` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `roles`
--

INSERT INTO `roles` (`id_role`, `name_role`) VALUES
(1, 'administrateur'),
(2, 'modérateur'),
(3, 'membre');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id_user` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `mail` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `id_role` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id_user`, `name`, `first_name`, `mail`, `password`, `image`, `id_role`) VALUES
(1, 'Joanel', 'Jonathan', 'toto@toto.com', '$2y$10$bqDsPpin/wMqMZ8DMeqTnOMUkbZ3LI6/3OESOG8x7T1xfZSNjJJp2', NULL, 2),
(2, 'aa', 'aa', 'aa@aa.com', '$2y$10$TaxsBELrivUdWb7ojT.8hO/kkZ6T03GH/bFDHAcPkrdsPFFN4Fx/e', NULL, 3),
(3, 'bb', 'bb', 'b@b.com', '$2y$10$pHhxb8/1vVldiejlkgP7Mu3JJiHUjC6FwQDcusbDNEjHAKwXQ.oNC', NULL, 1),
(4, 'dd', 'dd', 'dd@dd.com', '$2y$10$JAW8ymWY3374EPl.hyDu0eKZtpgBWb7tTfJDvKFOgURwAtBj9cwtq', NULL, 2),
(5, 'pp', 'pp', 'p@p.com', '$2y$10$ddoJ6LkpmIinGCqS0aaL4ePJTXO/hhyh0b.sfbNNq/lbcnA9QRbvy', NULL, 1),
(6, 'vv', 'vvvv', 'vv@vv.com', '$2y$10$piwJ/21gVfuwe9VChZWvyO9JES/9CL5M3Wr3f2x60npJb3WaqZhx.', NULL, 2),
(7, 'ff', 'fffff', 'f@f.com', '$2y$10$m5ZQF4wg/r2b5WkZaL4U.OQANn0sZPo.pFsP5y1GOGsBlPHv.n/NW', NULL, 3),
(8, 'kk', 'kk', 'k@k.com', '$2y$10$xKD7IhXp/gkrhRellVRKZ.ZVg6XtVRgMNO7/ehBlxhPACXDGzVL6a', NULL, 3),
(9, 'zz', 'zz', 'z@z.com', '$2y$10$z6vWesW/pJwWWdz4BNWprOesm2lLOjh9GEDbLOtGQOANrUXa0jXnm', NULL, 3),
(10, 'oo', 'oo', 'o@o.com', '$2y$10$cRvQCyZ0pvLfD/zrPeghoOu7pIJdzrcufzFq1s7IfWNUW2aXk4J5m', NULL, 2),
(11, 'nn', 'nn', 'n@n.com', '$2y$10$5D8zWpCXx6SEqr8tN4ZrheyZQ3o4ids96sUkwoQh2s/RxKrwuOFv.', NULL, 3),
(12, 'gg', 'gg', 'gf@gf.com', '$2y$10$4HweXFdY9vOxkpvvAJBkg.OCwAzSMCJHssf4vyeH/VeS78VzlULm2', NULL, 3),
(13, 'ww', 'ww', 'w@w.com', '$2y$10$pDX8vvkKecMzV7jGw4XgiOGvONO8O4v8uko1jXanvylOX0PAhy2OK', NULL, 1),
(14, 'h', 'h', 'h@h.com', '$2y$10$PFZpWiJ2WA3z5iD57qkDLOS5x83987QlI3uvTG1rrdnVI18S8HrNO', NULL, 2),
(15, 's', 's', 's@s.com', '$2y$10$DQEFJ9.0JxECxuRpU2MCzur0qgkdFk6nAf.mnHsQyR2M5AlwrS6xG', NULL, 3),
(16, 'x', 'x', 'x@x.com', '$2y$10$zQdlyT6O.O/uEyFFNhwkZ.xtl3Pqub1SJw6/oyblTQbEF6fdD/mJS', NULL, 3),
(17, 'mm', 'mm', 'ml@ml.com', '$2y$10$5KJn7YSdSma7QaL4VNnZauoYQ/A3Fh6Jr5RwvJkGM2/32k2xOWOTG', NULL, 1),
(18, 're', 're', 're@re.com', '$2y$10$qLheS7GFEGDHE3l3ySGkYOJPfKmgYWESiugoeP.PLjC/UMtNJKGiq', NULL, 3),
(51, 'corin', 'gaetan', 'email@email.fr', '$2y$10$L2B694J4g0ZaUf23HFbPc.XTWVWb9UI6C3G0QFLSJzIg3rvwii9hS', NULL, 1);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_role`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`),
  ADD KEY `id_role` (`id_role`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `roles`
--
ALTER TABLE `roles`
  MODIFY `id_role` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`id_role`) REFERENCES `roles` (`id_role`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
