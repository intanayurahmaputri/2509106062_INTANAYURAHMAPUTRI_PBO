"""
Latihan 5: Impor Data Pendaftar Lomba (Tantangan)
Tujuan: exception buatan sendiri, validasi bertingkat, dan exception chaining.

"""


class BarisDataError(Exception):
    """Error pada satu baris data pendaftar."""

    def __init__(self, nomor_baris, alasan):
        super().__init__(f"Baris {nomor_baris}: {alasan}")
        self.nomor_baris = nomor_baris
        self.alasan = alasan


class Pendaftar:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def __str__(self):
        return f"{self.nama} ({self.umur} tahun)"


def baca_pendaftar(nomor_baris, teks):
    """
    - Ubah satu baris 'nama;umur' menjadi Pendaftar.
    - Pemeriksaan berurutan dari yang paling mendasar sehingga pemanggil
    - cukup menangkap satu jenis exception: BarisDataError.
    
    """
    kolom = teks.split(";")
    if len(kolom) != 2:
        raise BarisDataError(nomor_baris, "format harus nama;umur")

    nama = kolom[0].strip()
    teks_umur = kolom[1].strip()

    if nama == "":
        raise BarisDataError(nomor_baris, "nama tidak boleh kosong")

    try:
        umur = int(teks_umur)
    except ValueError as e:
        # Exception chaining: ValueError asli menjadi __cause__
        raise BarisDataError(
            nomor_baris, f"umur '{teks_umur}' bukan angka"
        ) from e

    if not 17 <= umur <= 25:
        raise BarisDataError(
            nomor_baris, f"umur {umur} di luar syarat 17-25 tahun"
        )

    return Pendaftar(nama, umur)


def main():
    data = [
        "Ayu Lestari;20",
        "Bima Saputra",
        "Citra Dewi;dua puluh",
        ";19",
        "Dimas Pratama;30",
        "Eka Putri;18",
        "Fajar Nugraha;21;Samarinda",
    ]

    diterima = []
    jumlah_ditolak = 0

    print("=== IMPOR DATA PENDAFTAR LOMBA DEBAT ===")
    for nomor, teks in enumerate(data, start=1):
        try:
            pendaftar = baca_pendaftar(nomor, teks)
        except BarisDataError as e:
            jumlah_ditolak += 1
            print(f"[DITOLAK] {e}")
            if e.__cause__ is not None:
                print("          (penyebab asli: kesalahan konversi angka)")
        else:
            diterima.append(pendaftar)
            print(f"[OK] Baris {nomor}: {pendaftar}")

    print()
    print(f"Diterima: {len(diterima)}, ditolak: {jumlah_ditolak}")
    print("Daftar peserta:")
    for p in diterima:
        print(f"- {p}")


if __name__ == "__main__":
    main()