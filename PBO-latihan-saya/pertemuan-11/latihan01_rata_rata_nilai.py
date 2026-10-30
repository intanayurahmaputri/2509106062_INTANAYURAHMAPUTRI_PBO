"""
a. Latihan 1: Rata-Rata Nilai dari Teks (Dasar)
b. Tujuan: menangkap exception bawaan (ValueError) dan membiarkan exception lain (ZeroDivisionError) merambat ke pemanggil yang tepat.

"""


def rata_rata_nilai(daftar_teks):
    """
    - Hitung rata-rata (bilangan bulat, dibulatkan ke bawah) nilai valid.
    - Teks yang bukan angka dilewati. ZeroDivisionError SENGAJA tidak ditangkap di sini: fungsi ini tidak tahu cara menanganinya dengan ramah, jadi dibiarkan merambat ke proses_kelas().
    
    """
    total = 0
    jumlah_valid = 0
    for teks in daftar_teks:
        try:
            nilai = int(teks)
        except ValueError:
            print(f"  '{teks}' bukan angka, dilewati")
        else:
            total += nilai
            jumlah_valid += 1
    return total // jumlah_valid


def proses_kelas(nama_kelas, daftar_teks):
    print(f"=== {nama_kelas} ===")
    try:
        rata_rata = rata_rata_nilai(daftar_teks)
        print(f"Rata-rata: {rata_rata}")
    except ZeroDivisionError:
        print("Tidak ada nilai yang valid, rata-rata tidak bisa dihitung")


def main():
    proses_kelas("KELAS A", ["80", "75", "sembilan puluh", "92", ""])
    print()
    proses_kelas("\nKELAS B", ["-", "tidak hadir"])


if __name__ == "__main__":
    main()