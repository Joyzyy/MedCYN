--
-- Bază de date: `spital`
--

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `asistente`
--

CREATE TABLE `asistente` (
  `ID` INTEGER PRIMARY KEY,
  `Nume` TEXT NOT NULL,
  `Sectie` TEXT NOT NULL,
  `Disponibil` TEXT NOT NULL,
  `Program lucru` TEXT NOT NULL,
  `Concediu` TEXT NOT NULL,
  `Motiv` TEXT NOT NULL
);

--
-- Eliminarea datelor din tabel `asistente`
--

INSERT INTO `asistente` (`ID`, `Nume`, `Sectie`, `Disponibil`, `Program lucru`, `Concediu`, `Motiv`) VALUES
(1, 'Vasilica Macoveita', 'Cardiologie', 'Nu', '00:00:00 - 15:00:00', 'Nu', 'Inafara programului'),
(2, 'Marius Anghel', 'Cardiologie', 'Nu', '12:00:00 - 15:00:00', 'Da', 'Inafara programului'),
(3, 'Maria Andreea', 'Cardiologie', 'Nu', '20:00:00 - 05:00:00', 'Da', 'Inafara programului'),
(4, 'Zaharia Ionela', 'BoliInfectioase', 'Nu', '08:00:00 - 13:00:00', 'Da', 'Inafara programului'),
(5, 'Teodora Alexandra', 'Pediatrie', 'Da', '15:00:00 - 00:00:00', 'Da', '-'),
(6, 'Victoria Roxana', 'Psihiatrie', 'Nu', '12:00:00 - 21:00:00', 'Da', 'Concediu'),
(7, 'Buturuga Oana', 'Psihiatrie', 'Nu', '12:00:00 - 21:00:00', 'Da', 'Concediu'),
(8, 'Ilinca Ana', 'BoliInfectioase', 'Nu', '08:00:00 - 15:00:00', 'Da', 'Inafara programului'),
(9, 'Valeria Grigore', 'Cardiologie', 'Da', '16:00:00 - 01:00:00', 'Da', '-'),
(10, 'Rodica Nicoleta', 'BoliInfectioase', 'Nu', '14:00:00 - 22:00:00', 'Da', 'Concediu'),
(11, 'Victoria Bianca', 'Psihiatrie', 'Nu', '12:00:00 - 22:00:00', 'Da', 'Concediu'),
(12, 'Tatiana Cristina', 'Psihiatrie', 'Da', '00:00:00 - 07:00:00', 'Nu', '-'),
(13, 'Radu Mioara', 'Chirurgie', 'Da', '15:00:00 - 23:00:00', 'Nu', '-');

--
-- Structură tabel pentru tabel `medicamente`
--

CREATE TABLE `medicamente` (
  `ID` INTEGER PRIMARY KEY,
  `Sectie` TEXT NOT NULL,
  `Nume` TEXT NOT NULL,
  `Cantitate` INTEGER NOT NULL
);

--
-- Eliminarea datelor din tabel `medicamente`
--

INSERT INTO `medicamente` (`ID`, `Sectie`, `Nume`, `Cantitate`) VALUES
(1, 'Cardiologie', 'Tenzin', 2),
(2, 'Cardiologie', 'Kit Cardio', 0),
(3, 'Cardiologie', 'Leticina', 4),
(4, 'Chirurgie', 'Cikaflogo', 2),
(5, 'Chirurgie', 'Hernia Kit', 50),
(6, 'Chirurgie', 'Mezym', 7),
(7, 'Psihiatrie', 'Cebra Optim', 10),
(8, 'Psihiatrie', 'Pegilat', 7),
(9, 'Pediatrie', 'Tussinon', 2),
(10, 'Pediatrie', 'Fasconal', 5),
(11, 'BoliInfectioase', 'Dexametanoza', 6),
(12, 'BoliInfectioase', 'Septilin', 8),
(13, 'BoliInfectioase', 'Twinvir', 1),
(22, 'Pediatrie', 'Detrical', 3);

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `medici`
--

CREATE TABLE `medici` (
  `ID` INTEGER PRIMARY KEY,
  `Nume` TEXT NOT NULL,
  `Sectie` TEXT NOT NULL,
  `Disponibil` TEXT NOT NULL,
  `Program lucru` TEXT NOT NULL,
  `Concediu` TEXT NOT NULL,
  `Motiv` TEXT NOT NULL
);

--
-- Eliminarea datelor din tabel `medici`
--

INSERT INTO `medici` (`ID`, `Nume`, `Sectie`, `Disponibil`, `Program lucru`, `Concediu`, `Motiv`) VALUES
(2, 'Zaharia Daniel', 'Cardiologie', 'Da', '12:00:00 - 00:00:00', 'Da', '-'),
(4, 'Staret Cristian', 'Chirurgie', 'Da', '16:00:00 - 00:00:00', 'Nu', '-'),
(13, 'Rotaru Laura', 'Psihiatrie', 'Da', '00:00:00 - 09:50:00', 'Nu', '-'),
(113, 'Zavoianu Irina', 'BoliInfectioase', 'Da', '16:00:00 - 00:00:00', 'Da', '-'),
(114, 'Alexandru Ionut', 'Pediatrie', 'Nu', '17:00:00 - 03:00:00', 'Nu', 'Inafara programului'),
(115, 'Genina Mioara', 'BoliInfectioase', 'Da', '15:00:00 - 07:00:00', 'Nu', '-'),
(116, 'Alexia Crestez', 'Pediatrie', 'Nu', '18:00:00 - 00:00:00', 'Nu', 'Inafara programului'),
(117, 'Fanel Andrei', 'Cardiologie', 'Nu', '17:00:00 - 00:00:00', 'Nu', 'Inafara programului'),
(118, 'Alexandru Babuci', 'Cardiologie', 'Nu', '18:19:00 - 05:00:00', 'Nu', 'Inafara programului'),
(119, 'Paraschiv Alexandru', 'Pediatrie', 'Nu', '09:48:00 - 11:00:00', 'Nu', 'Inafara programului'),
(120, 'Gabi Tcaciu', 'BoliInfectioase', 'Da', '11:00:00 - 21:00:00', 'Nu', '-'),
(121, 'Tudor Iordache', 'Chirurgie', 'Nu', '08:00:00 - 16:00:00', 'Da', 'Inafara programului'),
(122, 'Bobe Razvan', 'Cardiologie', 'Da', '01:00:00 - 09:00:00', 'Da', '-'),
(123, 'Costea Valentin', 'Cardiologie', 'Da', '15:00:00 - 23:00:00', 'Nu', '-'),
(124, 'Iordache Mihaela', 'Pediatrie', 'Nu', '08:00:00 - 16:00:00', 'Nu', 'Inafara programului'),
(125, 'Oprea Andreea', 'BoliInfectioase', 'Nu', '12:00:00 - 20:00:00', 'Da', 'Concediu'),
(126, 'Pisica Alexandra', 'Psihiatrie', 'Nu', '03:00:00 -  12:00:00', 'Da', 'Inafara programului'),
(127, 'Ion Gabriel', 'Cardiologie', 'Da', '13:00:00 - 00:00:00', 'Da', '-'),
(128, 'Adiana Maria', 'Psihiatrie', 'Nu', '06:00:00 - 15:00:00', 'Da', 'Inafara programului'),
(129, 'Rotaru Mihai', 'Cardiologie', 'Nu', '14:00:00 - 23:00:00', 'Da', 'Concediu'),
(131, 'Jitianu Alexandru', 'Pediatrie', 'Nu', '01:00:00 - 10:00:00', 'Nu', 'Inafara programului');

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `pacienti`
--

CREATE TABLE `pacienti` (
  `ID` INTEGER PRIMARY KEY,
  `Nume` TEXT NOT NULL,
  `Varsta` INTEGER NOT NULL,
  `Sectie` TEXT NOT NULL,
  `Bloc` TEXT NOT NULL,
  `Etaj` TEXT NOT NULL,
  `Camera` INTEGER NOT NULL,
  `Afectiune` TEXT NOT NULL,
  `Medicament administrat` TEXT NOT NULL,
  `Perioada internare (zile)` INTEGER NOT NULL,
  `Evolutie` TEXT NOT NULL,
  `Data adaugarii` TEXT NOT NULL
);

--
-- Eliminarea datelor din tabel `pacienti`
--

INSERT INTO `pacienti` (`ID`, `Nume`, `Varsta`, `Sectie`, `Bloc`, `Etaj`, `Camera`, `Afectiune`, `Medicament administrat`, `Perioada internare (zile)`, `Evolutie`, `Data adaugarii`) VALUES
(1, 'Gabriel Zavoianu', 15, 'Cardiologie', 'A', '1', 5, 'Boala valvulara', 'Leticina', 14, 'Neutra', '2020-06-01'),
(2, 'Alexandru Anton', 41, 'Cardiologie', 'A', '2', 20, 'Insuficienta cardiaca', 'Leticina', 28, 'Negativa', '2020-06-30'),
(11, 'Andrei Valentin', 25, 'Cardiologie', 'A', '3', 10, 'Malformatii cardiace', 'Leticina', 24, 'Pozitiva', '2020-06-23'),
(12, 'Cosmina Necula', 84, 'Cardiologie', 'A', '3', 4, 'Hipertensiune arteriala', 'Kit Cardiac', 30, 'Pozitiva', '2020-05-21'),
(13, 'Daniel David', 55, 'Chirurgie', 'A', '5', 4, 'Hernie', 'Hernia Kit', 11, 'Neutra', '2020-03-05'),
(14, 'Dragos Eduard', 14, 'Chirurgie', 'A', '6', 6, 'Apendicita', 'Mezym', 7, 'Pozitiva', '2020-05-21'),
(15, 'Alexandra Miron', 44, 'BoliInfectioase', 'A', '3', 7, 'Pneumonie', 'Septilin', 14, 'Pozitiva', '2020-06-05'),
(16, 'Emilian Florin', 65, 'BoliInfectioase', 'A', '4', 15, 'Encefalita', 'Dexametanoza', 28, 'Negativa', '2020-02-05'),
(17, 'Madalin Alexandru', 41, 'BoliInfectioase', 'A', '3', 10, 'Micoza', 'Dexametanoza', 28, 'Negativa', '2019-12-14'),
(18, 'Gabriel Laurentiu', 34, 'Psihiatrie', 'B', '1', 20, 'Dementa', 'Cebra Optim', 144, 'Negativa', '2020-02-11'),
(19, 'Iulian Ivan', 44, 'Psihiatrie', 'B', '2', 4, 'Alzheimer', 'Cebra Optim', 249, 'Neutra', '2020-02-23'),
(20, 'Madalin Marius', 55, 'Psihiatrie', 'C', '1', 6, 'Psihoza', 'Pegilat', 105, 'Negativa', '2020-03-03'),
(21, 'Albert Barbu', 30, 'Pediatrie', 'B', '1', 15, 'Bronsita', 'Tussinon', 25, 'Pozitiva', '2020-04-01'),
(22, 'Dumitru Dimitrie', 45, 'Pediatrie', 'B', '2', 14, 'Convulsie febrila', 'Fasconal', 66, 'Neutra', '2020-02-01'),
(23, 'Iustin Iacob', 29, 'Pediatrie', 'B', '2', 15, 'Rahitism', 'Detrical', 42, 'Neutra', '2020-01-03'),
(34, 'Adrian Cuban', 15, 'Cardiologie', 'A', '1', 5, 'Boala valvulara', 'Leticina', 0, 'Pozitiva', '0000-00-00'),
(35, 'Ioana Cardiana', 55, 'Psihiatrie', 'B', '1', 1, 'Alzheimer', 'Cebra Optim', 0, 'Pozitiva', '0000-00-00');
