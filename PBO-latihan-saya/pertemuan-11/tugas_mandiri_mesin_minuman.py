"""
Tugas Mandiri: Mesin Penjual Minuman di Gedung Kuliah

Program ini mensimulasikan mesin penjual minuman dengan penanganan error
menggunakan exception handling.

Catatan checked dan unchecked:
Di Python, semua exception termasuk unchecked karena tidak wajib
menggunakan try-except atau menuliskan deklarasi throws seperti di Java.

Namun, dalam program ini beberapa error seperti produk tidak ditemukan,
stok habis, dan uang tidak cukup sengaja ditangani satu per satu.
Alasannya, kondisi tersebut bisa saja terjadi saat transaksi dan masih
bisa ditangani oleh program tanpa harus menghentikan seluruh aplikasi.

Kalau menggunakan Java, exception seperti ini lebih cocok dibuat
sebagai checked exception (extends Exception), supaya bagian yang
memanggilnya wajib menangani kemungkinan error tersebut.

"""


def rupiah(nilai):
    return "Rp" + f"{nilai:,}".replace(",", ".")


#Hierarki exception
class MesinError(Exception):
    """Induk semua error mesin minuman."""


class ProdukTidakAdaError(MesinError):
    """Kode produk tidak terdaftar di mesin."""

    def __init__(self, kode):
        super().__init__(f"Produk dengan kode '{kode}' tidak ada")
        self.kode = kode


class StokHabisError(MesinError):
    """Stok produk habis."""

    def __init__(self, nama_produk):
        super().__init__(f"Stok {nama_produk} habis")
        self.nama_produk = nama_produk


class UangKurangError(MesinError):
    """Uang yang dimasukkan kurang dari harga produk."""

    def __init__(self, kekurangan):
        super().__init__(f"Uang kurang {rupiah(kekurangan)}")
        self.kekurangan = kekurangan


#Kelas domain
class Produk:
    def __init__(self, kode, nama, harga, stok):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok


class MesinMinuman:
    def __init__(self, daftar_produk):
        self.produk = {p.kode: p for p in daftar_produk}
        self.pendapatan = 0

    def beli(self, kode, uang):
        """
        Proses pembelian produk dan menghitung kembalian:
        - Periksa semua syarat pembelian terlebih dahulu.
        - Stok dan pendapatan hanya diubah jika transaksi berhasil.
        
        """
        if kode not in self.produk:
            raise ProdukTidakAdaError(kode)
        produk = self.produk[kode]
        if produk.stok <= 0:
            raise StokHabisError(produk.nama)
        if uang < produk.harga:
            raise UangKurangError(produk.harga - uang)

        produk.stok -= 1
        self.pendapatan += produk.harga
        return uang - produk.harga


def main():
    mesin = MesinMinuman([
        Produk("A1", "Air Mineral", 3000, 5),
        Produk("A2", "Teh Botol", 5000, 3),
        Produk("B1", "Kopi Kaleng", 8000, 1),
        Produk("B2", "Jus Jeruk", 10000, 0),
    ])

    transaksi = [
        ("A1", 5000),
        ("B1", 10000),
        ("B1", 10000),
        ("A2", 3000),
        ("C9", 5000),
        ("B2", 10000),
        ("A2", 5000),
    ]

    print("=== SIMULASI MESIN PENJUAL MINUMAN ===")
    for nomor, (kode, uang) in enumerate(transaksi, start=1):
        print(f"Transaksi {nomor}: kode {kode}, uang {rupiah(uang)}")
        try:
            kembalian = mesin.beli(kode, uang)
            nama = mesin.produk[kode].nama
            print(f"  Berhasil membeli {nama}. Kembalian: {rupiah(kembalian)}")
        except ProdukTidakAdaError as e:
            print(f"  Maaf, kode '{e.kode}' tidak ditemukan. Periksa kembali kode produk.")
        except StokHabisError as e:
            print(f"  Maaf, {e.nama_produk} sedang habis. Silakan pilih minuman lain.")
        except UangKurangError as e:
            print(f"  Uang kurang {rupiah(e.kekurangan)}. Silakan tambah uang Anda.")
        except MesinError as e:
            print(f"  Terjadi kesalahan pada mesin: {e}")
        finally:
            print("  Mesin siap melayani pembeli berikutnya")

    print(f"\nTotal pendapatan: {rupiah(mesin.pendapatan)}")
    print("Sisa stok:")
    for p in mesin.produk.values():
        print(f"- {p.nama}: {p.stok}")


if __name__ == "__main__":
    main()