-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 16 Jul 2018 pada 01.32
-- Versi server: 10.1.25-MariaDB
-- Versi PHP: 7.2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `catur`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `gelar_pelatih`
--

CREATE TABLE `gelar_pelatih` (
  `id_pelatih` varchar(8) NOT NULL,
  `pnp` tinyint(1) NOT NULL,
  `pnm` tinyint(1) NOT NULL,
  `pn` tinyint(1) NOT NULL,
  `ins` tinyint(1) NOT NULL,
  `fst` tinyint(1) NOT NULL,
  `ft` tinyint(1) NOT NULL,
  `fi` tinyint(1) NOT NULL,
  `ni` tinyint(1) NOT NULL,
  `di` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `gelar_pelatih`
--

INSERT INTO `gelar_pelatih` (`id_pelatih`, `pnp`, `pnm`, `pn`, `ins`, `fst`, `ft`, `fi`, `ni`, `di`) VALUES
('13/96003', 1, 1, 1, 1, 1, 1, 1, 0, 0);

-- --------------------------------------------------------

--
-- Struktur dari tabel `gelar_pemain`
--

CREATE TABLE `gelar_pemain` (
  `id_pemain` varchar(12) NOT NULL,
  `gm` tinyint(1) NOT NULL,
  `im` tinyint(1) NOT NULL,
  `fm` tinyint(1) NOT NULL,
  `cm` tinyint(1) NOT NULL,
  `wgm` tinyint(1) NOT NULL,
  `wim` tinyint(1) NOT NULL,
  `wfm` tinyint(1) NOT NULL,
  `wcm` tinyint(1) NOT NULL,
  `mn` tinyint(1) NOT NULL,
  `mp` tinyint(1) NOT NULL,
  `mnw` tinyint(1) NOT NULL,
  `mpw` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `gelar_pemain`
--

INSERT INTO `gelar_pemain` (`id_pemain`, `gm`, `im`, `fm`, `cm`, `wgm`, `wim`, `wfm`, `wcm`, `mn`, `mp`, `mnw`, `mpw`) VALUES
('32/97001', 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Struktur dari tabel `gelar_wasit`
--

CREATE TABLE `gelar_wasit` (
  `id_wasit` varchar(8) NOT NULL,
  `wnp` tinyint(1) NOT NULL,
  `wnm` tinyint(1) NOT NULL,
  `wn` tinyint(1) NOT NULL,
  `fa` tinyint(1) NOT NULL,
  `ia` tinyint(1) NOT NULL,
  `io` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `mutasi_pelatih`
--

CREATE TABLE `mutasi_pelatih` (
  `id_pelatih` varchar(8) NOT NULL,
  `nama` varchar(35) NOT NULL,
  `awal` varchar(30) NOT NULL,
  `akhir` varchar(30) NOT NULL,
  `tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `mutasi_pemain`
--

CREATE TABLE `mutasi_pemain` (
  `id_pemain` varchar(8) NOT NULL,
  `nama` varchar(35) NOT NULL,
  `awal` varchar(30) NOT NULL,
  `akhir` varchar(30) NOT NULL,
  `tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `mutasi_pemain`
--

INSERT INTO `mutasi_pemain` (`id_pemain`, `nama`, `awal`, `akhir`, `tanggal`) VALUES
('32/97001', 'Jibril Hartri Putra', 'Jakarta', 'Bandung', '2018-07-02'),
('32/97001', 'Jibril Hartri Putra', 'Jakarta', 'Surabaya', '2018-07-02'),
('32/97001', 'Jibril Hartri Putra', 'JAWA BARAT', '11', '2018-07-13'),
('32/97001', 'Jibril Hartri Putra', 'JAWA BARAT', '11', '2018-07-13'),
('32/97001', 'Jibril Hartri Putra', 'ACEH', '11', '2018-07-13'),
('32/97001', 'Jibril Hartri Putra', 'ACEH', '17', '2018-07-13'),
('32/97001', 'Jibril Hartri Putra', 'BENGKULU', '52', '2018-07-13');

-- --------------------------------------------------------

--
-- Struktur dari tabel `mutasi_wasit`
--

CREATE TABLE `mutasi_wasit` (
  `id_wasit` varchar(8) NOT NULL,
  `nama` varchar(35) NOT NULL,
  `awal` varchar(30) NOT NULL,
  `akhir` varchar(30) NOT NULL,
  `tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `pelatih`
--

CREATE TABLE `pelatih` (
  `no` int(11) NOT NULL,
  `fide_id` varchar(7) NOT NULL,
  `id_pelatih` varchar(8) NOT NULL,
  `nama_pelatih` varchar(35) NOT NULL,
  `jenis_kelamin` varchar(1) NOT NULL,
  `tempat_lahir` varchar(30) NOT NULL,
  `tanggal_lahir` date NOT NULL,
  `alamat` text NOT NULL,
  `telepon` varchar(13) NOT NULL,
  `kode_pos` varchar(5) NOT NULL,
  `email` varchar(50) NOT NULL,
  `rating_fide` int(4) NOT NULL,
  `rating_national` int(4) NOT NULL,
  `klasifikasi` varchar(1) NOT NULL,
  `pemprov` varchar(30) NOT NULL,
  `data_prestasi` text NOT NULL,
  `foto` varchar(50) NOT NULL,
  `status` varchar(11) NOT NULL,
  `tanggal` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `pelatih`
--

INSERT INTO `pelatih` (`no`, `fide_id`, `id_pelatih`, `nama_pelatih`, `jenis_kelamin`, `tempat_lahir`, `tanggal_lahir`, `alamat`, `telepon`, `kode_pos`, `email`, `rating_fide`, `rating_national`, `klasifikasi`, `pemprov`, `data_prestasi`, `foto`, `status`, `tanggal`) VALUES
(4, '1', '13/96003', 'Hmm', 'L', 'Depok', '1996-01-01', 'Juanda', '0821', '12532', 'jibrilhp@student.gunadarma.ac.id', 1, 1, 'A', '13', 'ya baguslah', 'd8c81cc43ba1bc34e9357f14637c2698.jpg', 'Aktif', '2018-07-15 22:25:38');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pemain`
--

CREATE TABLE `pemain` (
  `no` int(11) NOT NULL,
  `fide_id` varchar(7) NOT NULL,
  `id_pemain` varchar(8) NOT NULL,
  `nama_pemain` varchar(35) NOT NULL,
  `jenis_kelamin` varchar(1) NOT NULL,
  `tempat_lahir` varchar(30) NOT NULL,
  `tanggal_lahir` date NOT NULL,
  `alamat` text NOT NULL,
  `telepon` varchar(13) NOT NULL,
  `kode_pos` varchar(5) NOT NULL,
  `email` varchar(50) NOT NULL,
  `rating_fide` int(4) NOT NULL,
  `rating_national` int(4) NOT NULL,
  `pemprov` varchar(30) NOT NULL,
  `data_prestasi` text NOT NULL,
  `foto` varchar(50) NOT NULL,
  `status` varchar(11) NOT NULL,
  `tanggal` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `pemain`
--

INSERT INTO `pemain` (`no`, `fide_id`, `id_pemain`, `nama_pemain`, `jenis_kelamin`, `tempat_lahir`, `tanggal_lahir`, `alamat`, `telepon`, `kode_pos`, `email`, `rating_fide`, `rating_national`, `pemprov`, `data_prestasi`, `foto`, `status`, `tanggal`) VALUES
(2, '1', '32/97001', 'Jibril Hartri Putra', 'L', 'Jakarta', '1997-01-22', 'Jalan Kencana 3 No. 44', '085781601196', '12430', 'jibrilhp@outlook.com', 1, 1, '52', 'Manggarai  ', '2012-03-13-191329.jpg', 'Aktif', '2018-07-13 02:32:54');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengguna`
--

CREATE TABLE `pengguna` (
  `id` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `sebagai` int(11) NOT NULL,
  `approve` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `pengguna`
--

INSERT INTO `pengguna` (`id`, `username`, `password`, `sebagai`, `approve`) VALUES
(1, 'admin', 'admin', 0, 0),
(2, 'bunawan', 'pionsakti', 0, 0),
(3, 'pungbear', 'pungkamp', 0, 0),
(4, 'beruang', 'beruang', 1, 0);

-- --------------------------------------------------------

--
-- Struktur dari tabel `provinsi`
--

CREATE TABLE `provinsi` (
  `kd_provinsi` varchar(2) NOT NULL,
  `nm_provinsi` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `provinsi`
--

INSERT INTO `provinsi` (`kd_provinsi`, `nm_provinsi`) VALUES
('11', 'ACEH'),
('12', 'SUMATERA UTARA'),
('13', 'SUMATERA BARAT'),
('14', 'RIAU'),
('15', 'JAMBI'),
('16', 'SUMATERA SELATAN'),
('17', 'BENGKULU'),
('18', 'LAMPUNG'),
('19', 'KEPULAUAN BANGKA BELITUNG'),
('21', 'KEPULAUAN RIAU'),
('31', 'DKI JAKARTA'),
('32', 'JAWA BARAT'),
('33', 'JAWA TENGAH'),
('34', 'DI YOGYAKARTA'),
('35', 'JAWA TIMUR'),
('36', 'BANTEN'),
('51', 'BALI'),
('52', 'NUSA TENGGARA BARAT'),
('53', 'NUSA TENGGARA TIMUR'),
('61', 'KALIMANTAN BARAT'),
('62', 'KALIMANTAN TENGAH'),
('63', 'KALIMANTAN SELATAN'),
('64', 'KALIMANTAN TIMUR'),
('65', 'KALIMANTAN UTARA'),
('71', 'SULAWESI UTARA'),
('72', 'SULAWESI TENGAH'),
('73', 'SULAWESI SELATAN'),
('74', 'SULAWESI TENGGARA'),
('75', 'GORONTALO'),
('76', 'SULAWESI BARAT'),
('81', 'MALUKU'),
('82', 'MALUKU UTARA'),
('91', 'PAPUA'),
('92', 'PAPUA BARAT');

-- --------------------------------------------------------

--
-- Struktur dari tabel `wasit`
--

CREATE TABLE `wasit` (
  `no` int(11) NOT NULL,
  `fide_id` varchar(7) NOT NULL,
  `id_wasit` varchar(8) NOT NULL,
  `nama_wasit` varchar(35) NOT NULL,
  `jenis_kelamin` varchar(1) NOT NULL,
  `tempat_lahir` varchar(30) NOT NULL,
  `tanggal_lahir` date NOT NULL,
  `alamat` text NOT NULL,
  `telepon` varchar(13) NOT NULL,
  `kode_pos` varchar(5) NOT NULL,
  `email` varchar(50) NOT NULL,
  `rating_fide` int(4) NOT NULL,
  `rating_national` int(4) NOT NULL,
  `klasifikasi` varchar(1) NOT NULL,
  `pemprov` varchar(30) NOT NULL,
  `data_prestasi` text NOT NULL,
  `foto` varchar(50) NOT NULL,
  `status` varchar(11) NOT NULL,
  `tanggal` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `gelar_pelatih`
--
ALTER TABLE `gelar_pelatih`
  ADD KEY `id_pelatih` (`id_pelatih`);

--
-- Indeks untuk tabel `gelar_pemain`
--
ALTER TABLE `gelar_pemain`
  ADD PRIMARY KEY (`id_pemain`);

--
-- Indeks untuk tabel `gelar_wasit`
--
ALTER TABLE `gelar_wasit`
  ADD KEY `id_wasit` (`id_wasit`);

--
-- Indeks untuk tabel `mutasi_pelatih`
--
ALTER TABLE `mutasi_pelatih`
  ADD KEY `id_pelatih` (`id_pelatih`);

--
-- Indeks untuk tabel `mutasi_pemain`
--
ALTER TABLE `mutasi_pemain`
  ADD KEY `id_pemain` (`id_pemain`);

--
-- Indeks untuk tabel `mutasi_wasit`
--
ALTER TABLE `mutasi_wasit`
  ADD KEY `id_wasit` (`id_wasit`);

--
-- Indeks untuk tabel `pelatih`
--
ALTER TABLE `pelatih`
  ADD PRIMARY KEY (`no`),
  ADD UNIQUE KEY `id_pelatih` (`id_pelatih`) USING BTREE;

--
-- Indeks untuk tabel `pemain`
--
ALTER TABLE `pemain`
  ADD PRIMARY KEY (`no`),
  ADD UNIQUE KEY `id_pemain` (`id_pemain`) USING BTREE;

--
-- Indeks untuk tabel `pengguna`
--
ALTER TABLE `pengguna`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indeks untuk tabel `provinsi`
--
ALTER TABLE `provinsi`
  ADD UNIQUE KEY `kd_propinsi` (`kd_provinsi`);

--
-- Indeks untuk tabel `wasit`
--
ALTER TABLE `wasit`
  ADD PRIMARY KEY (`no`),
  ADD UNIQUE KEY `id_wasit` (`id_wasit`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `pelatih`
--
ALTER TABLE `pelatih`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `pemain`
--
ALTER TABLE `pemain`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `pengguna`
--
ALTER TABLE `pengguna`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `wasit`
--
ALTER TABLE `wasit`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `gelar_pelatih`
--
ALTER TABLE `gelar_pelatih`
  ADD CONSTRAINT `gelar_pelatih_ibfk_1` FOREIGN KEY (`id_pelatih`) REFERENCES `pelatih` (`id_pelatih`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `gelar_pemain`
--
ALTER TABLE `gelar_pemain`
  ADD CONSTRAINT `gelar_pemain_ibfk_1` FOREIGN KEY (`id_pemain`) REFERENCES `pemain` (`id_pemain`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `gelar_wasit`
--
ALTER TABLE `gelar_wasit`
  ADD CONSTRAINT `gelar_wasit_ibfk_1` FOREIGN KEY (`id_wasit`) REFERENCES `wasit` (`id_wasit`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `mutasi_pelatih`
--
ALTER TABLE `mutasi_pelatih`
  ADD CONSTRAINT `mutasi_pelatih_ibfk_1` FOREIGN KEY (`id_pelatih`) REFERENCES `pelatih` (`id_pelatih`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `mutasi_pemain`
--
ALTER TABLE `mutasi_pemain`
  ADD CONSTRAINT `mutasi_pemain_ibfk_1` FOREIGN KEY (`id_pemain`) REFERENCES `pemain` (`id_pemain`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `mutasi_wasit`
--
ALTER TABLE `mutasi_wasit`
  ADD CONSTRAINT `mutasi_wasit_ibfk_1` FOREIGN KEY (`id_wasit`) REFERENCES `wasit` (`id_wasit`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
