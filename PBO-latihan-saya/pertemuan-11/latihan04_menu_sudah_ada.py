"""
a. Latihan 4 (KedaiKita): Menolak Kode Menu Ganda (Menengah)
b. Cara B: satu file berisi salinan ringkas kelas studi kasus KedaiKita yang dibutuhkan, ditambah exception baru MenuSudahAdaError.

"""


def rupiah(nilai):
    """Format 18000 -> 'Rp18.000'."""
    return "Rp" + f"{nilai:,}".replace(",", ".")


#Hierarki exception
class KedaiError(Exception):
    """Induk semua error KedaiKita."""


class MenuSudahAdaError(KedaiError):
    """Kode menu sudah dipakai menu lain."""

    def __init__(self, kode, nama_lama):
        super().__init__(f"Kode {kode} sudah dipakai oleh {nama_lama}")
        self.kode = kode
        self.nama_lama = nama_lama


#Kelas domain
class Menu:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"[{self.kode}] {self.nama} - {rupiah(self.harga)}"


class Kedai:
    def __init__(self):
        self.daftar_menu = []

    def tambah_menu(self, menu):
        """Tambah menu. Lempar MenuSudahAdaError SEBELUM menu dimasukkan."""
        for ada in self.daftar_menu:
            if ada.kode == menu.kode:
                raise MenuSudahAdaError(menu.kode, ada.nama)
        self.daftar_menu.append(menu)


def main():
    kedai = Kedai()
    daftar_uji = [
        Menu("M01", "Kopi Susu Gula Aren", 18000),
        Menu("M02", "Es Teh Manis", 8000),
        Menu("M03", "Nasi Goreng Kampung", 25000),
        Menu("M04", "Mie Goreng Jawa", 23000),
        Menu("M05", "Pisang Goreng Keju", 15000),
        Menu("M02", "Es Jeruk", 10000),
        Menu("M06", "Teh Tarik", 12000),
        Menu("M06", "Kopi Tubruk", 12000),
    ]

    print("=== MENAMBAH MENU ===")
    for menu in daftar_uji:
        try:
            kedai.tambah_menu(menu)
            print(f"[OK] {menu}")
        except MenuSudahAdaError as e:
            print(f"[GAGAL] {e}")
            print(f"        {menu.nama} tidak ditambahkan, pilih kode selain {e.kode}")
    print(f"Jumlah menu terdaftar: {len(kedai.daftar_menu)}")


if __name__ == "__main__":
    main()