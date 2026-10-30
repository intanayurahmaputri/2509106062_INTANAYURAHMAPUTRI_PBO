"""
a. Latihan 3: Peminjaman Buku Perpustakaan (Menengah)
b. Tujuan: membuat hierarki exception sendiri yang membawa data tambahan.

"""


#Hierarki exception
class PerpustakaanError(Exception):
    """Induk semua error perpustakaan."""


class BukuSedangDipinjamError(PerpustakaanError):
    """Buku yang diminta sedang dipinjam orang lain."""

    def __init__(self, judul, peminjam):
        super().__init__(f"Buku '{judul}' sedang dipinjam oleh {peminjam}")
        self.judul = judul
        self.peminjam = peminjam


class BatasPinjamError(PerpustakaanError):
    """Anggota sudah mencapai batas maksimal pinjaman."""

    def __init__(self, nama, batas):
        super().__init__(f"{nama} sudah meminjam {batas} buku (batas maksimal)")
        self.nama = nama
        self.batas = batas


#Kelas domain
class Buku:
    def __init__(self, judul):
        self.judul = judul
        self.peminjam = None


class Anggota:
    BATAS_PINJAM = 2

    def __init__(self, nama):
        self.nama = nama
        self.daftar_pinjam = []

    def pinjam(self, buku):
        if buku.peminjam is not None:
            raise BukuSedangDipinjamError(buku.judul, buku.peminjam.nama)
        if len(self.daftar_pinjam) >= self.BATAS_PINJAM:
            raise BatasPinjamError(self.nama, self.BATAS_PINJAM)
        buku.peminjam = self
        self.daftar_pinjam.append(buku)
        print(f"{self.nama} meminjam '{buku.judul}'")

    def kembalikan(self, buku):
        if buku not in self.daftar_pinjam:
            raise PerpustakaanError(
                f"{self.nama} tidak sedang meminjam '{buku.judul}'"
            )
        self.daftar_pinjam.remove(buku)
        buku.peminjam = None
        print(f"{self.nama} mengembalikan '{buku.judul}'")


def coba_pinjam(anggota, buku):
    try:
        anggota.pinjam(buku)
    except BatasPinjamError as e:
        print(f"Gagal: {e}")
        print(f"  Saran: kembalikan dulu salah satu dari {e.batas} buku")
    except BukuSedangDipinjamError as e:
        print(f"Gagal: {e}")
        print(f"  Saran: tunggu sampai {e.peminjam} mengembalikannya")


def coba_kembalikan(anggota, buku):
    try:
        anggota.kembalikan(buku)
    except PerpustakaanError as e:
        print(f"Gagal: {e}")


def main():
    laskar = Buku("Laskar Pelangi")
    bumi = Buku("Bumi Manusia")
    negeri = Buku("Negeri 5 Menara")
    ayu = Anggota("Ayu")
    bima = Anggota("Bima")

    print("=== PEMINJAMAN BUKU ===")
    coba_pinjam(ayu, laskar)
    coba_pinjam(ayu, bumi)
    coba_pinjam(ayu, negeri)
    coba_pinjam(bima, laskar)

    print()
    print("=== PENGEMBALIAN ===")
    coba_kembalikan(bima, bumi)
    coba_kembalikan(ayu, laskar)
    coba_pinjam(bima, laskar)


if __name__ == "__main__":
    main()