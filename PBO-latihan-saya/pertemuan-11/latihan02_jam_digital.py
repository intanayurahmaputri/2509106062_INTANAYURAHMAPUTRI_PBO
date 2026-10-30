"""
a. Latihan 2: Jam Digital yang Menolak Waktu Mustahil (Dasar)
b. Tujuan: melempar exception untuk validasi dan memakai blok finally.

"""


class JamDigital:
    #Jam digital format 24 jam, awalnya 00:00.
    def __init__(self):
        self.jam = 0
        self.menit = 0

    def atur(self, jam, menit):
        """
        - Waktu lama tidak berubah jika ditolak.
        - Validasi dilakukan SEBELUM atribut diubah, sehingga jika
        - exception dilempar, baris pengubah atribut tidak pernah tercapai.
        
        """
        if not 0 <= jam <= 23:
            raise ValueError("jam harus 0 sampai 23")
        if not 0 <= menit <= 59:
            raise ValueError("menit harus 0 sampai 59")
        self.jam = jam
        self.menit = menit

    def tampilan(self):
        return f"{self.jam:02d}:{self.menit:02d}"


def main():
    jam = JamDigital()
    print("=== JAM DIGITAL ===")
    print(f"Tampilan awal: {jam.tampilan()}")

    percobaan = [(7, 30), (25, 0), (12, 75), (23, 59), (-1, 10)]
    for j, m in percobaan:
        try:
            jam.atur(j, m)
            print(f"Atur ke jam {j} menit {m} -> berhasil")
        except ValueError as e:
            print(f"Atur ke jam {j} menit {m} -> ditolak: {e}")
        finally:
            print(f"  Tampilan jam: {jam.tampilan()}")


if __name__ == "__main__":
    main()