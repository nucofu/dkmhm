import curses
import define as df

# splash screen aplikasi ini
def main_menu():
    menu_selection = [
        "Mulai",
        "Tentang Kami"
    ]
    main_windows = [
"""\
   @@@@@@@@@@@@@@@@@@@@  \n\
 @@  @@            @@  @@ \n\
@@   @@@          @@@   @@\n\
@@   @@@          @@@   @@\n\
@@   @@@@        @@@@   @@\n\
@@   @@@@        @@@@   @@\n\
@@   @@@@@      @@@@@   @@\n\
@@   @@@@@@@@@@@@@@@@   @@\n\
 @   @@@@@@@@@@@@@@@@   @ \n\
 @@  @@@@@      @@@@@  @@ \n\
  @   @@@        @@@   @  \n\
   @@@@@@@@@@@@@@@@@@@@   \n\
\n\
\n\
Sistem Pakar Diagnosa Kerusakan Motor Honda Matic\n\
-------------------------------\n\
\n\
Aplikasi ini menggunakan metode hybrid antara Forward Chaining\n\
dan Certainty Factor untuk menganalisa gejala dan menghitung\n\
tingkat keyakinan dari setiap kemungkinan kerusakan.\n\
\n\
Gejala yang Anda pilih akan dicocokkan dengan aturan,\n\
kemudian nilai kerusakan yang sama akan dikombinasikan untuk\n\
mendapatkan bobot nilai secara pasti\n\
\n\
~ Tekan tombol Enter untuk melanjutkan...\n\
""", """\
Tentang Kami\n\
------------\n\
\n\
Kami adalah mahasiswa Sistem informasi dari UBSI kampus\n\
Tasikmalaya yang sedang mengembangkan aplikasi sistem pakar\n\
berbasis TUI sebagai bagian dari proyek studi dan ketertarikan\n\
kami pada teknologi open-source.\n\
\n\
Anggota Kelompok:\n\
- Rustu Judika Rahmat        : (NIM 19252502)\n\
- Sri Lestari Putri          : (NIM 19250202)\n\
- M. Zidan Asykarilah Rahman : (NIM 19251159)\n\
- Nurfauzy Sundara           : (NIM 19252624)\n\
\n\
Tujuan aplikasi ini dibuat adalah untuk membantu pengguna\n\
mengenali kerusakan motor Honda matic dengan metode hybrid\n\
Forward Chaining dan Certainty Factor melalui antarmuka\n\
terminal yang ringan.\n\
\n\
Harapan kami, aplikasi ini dapat menjadi bagian dari ekosistem\n\
open-source yang terus berkembang, terutama distribusi melalui\n\
repository package.\n
"""]
    return menu_selection, main_windows

# Penjelasan singkat tentang panduan menggunakan aplikasi ini
def panduanSingkat():
    PANDUAN = ["""\
1. ANGKET\n\
--------------------------------\n\
Pada layar ini ditampilkan soal-soal angket yang digunakan untuk menakar nilai CF User.\n\
Total terdapat 20 soal.\n\
\n\
Key:\n\
  [q] Back    : Kembali ke Menu Utama\n\
  [s] Submit  : Masuk ke tahap Pre-Submit\n\
  [n] Next    : Pindah ke soal berikutnya\n\
  [b] Prev    : Kembali ke soal sebelumnya\n\
\n\
\n\
2. CERTAINTY FACTOR ROLL (CF ROLL)\n\
--------------------------------\n\
Pada layar ini ditampilkan nilai keyakinan (CF User) dalam bentuk persentase.\n\
\n\
Keterangan nilai:\n\
  0%   : Tidak Terjadi\n\
  25%  : Mungkin Tidak Terjadi\n\
  50%  : Ragu-ragu\n\
  75%  : Mungkin Terjadi\n\
  100% : Terjadi\n\
\n\
Selain nilai di atas, pengguna dapat menentukan persentase secara bebas\n\
sesuai tingkat keyakinan masing-masing.\n\
""", """\
3. LAMPU INDIKATOR\n\
--------------------------------\n\
Pada layar ini ditampilkan status setiap soal menggunakan warna indikator.\n\
\n\
Keterangan warna:\n\
  Putih : 50% (Netral)\n\
  Hijau : Di atas 50% (Cenderung Terjadi)\n\
  Merah : Di bawah 50% (Cenderung Tidak Terjadi)\n\
\n\
\n\
4. PRE-SUBMIT\n\
--------------------------------\n\
Layar Pre-Submit akan muncul setelah tombol Submit ditekan.\n\
\n\
Pada tahap ini, seluruh jawaban yang telah diinput akan ditampilkan kembali\n\
untuk diperiksa sebelum dilakukan kalkulasi.\n\
\n\
Terdapat 4 halaman, di mana setiap halaman menampilkan 5 soal beserta jawaban\n\
yang telah diisi sebelumnya.\n\
\n\
Key:\n\
  [←] Geser halaman ke belakang\n\
  [→] Geser halaman ke depan\n\
\n\
Pilihan konfirmasi:\n\
  [iya]   : Melanjutkan ke proses kalkulasi\n\
  [tidak] : Kembali ke pengisian soal\n\
"""]
    
    return PANDUAN

# data Soal dan Jawaban Angket
def dataAngket():
    QUESTIONS = [
        "Motor sulit dihidupkan dengan electric starter",
        "Terdengar suara \"Cetek-cetek\" saat starter ditekan\n tapi mesin tidak berputar",
        "Lampu indikator dan speedometer redup atau mati\n saat kunci kontak ON",
        "Mesin \"brebet\" atau tersendat saat digas",
        "Akselerasi awal terasa berat atau ngeden",
        "Timbul Getaran \"gredek\" saat tarikan gas awal",
        "Terdengar Suara berdecit atau mencicit dari area\n CVT saat langsam",
        "Mesin sering mati mendadak saat langsam atau\n berhenti",
        "Konsumsi bahan bakar terasa lebih boros dari\n biasanya",
        "Terdengar Suara \"klotok-klotok\" kasar dari\n area CVT",
        "Tenaga motor terasa berkurang drastis di putaran\n atas \"ngemos\"",
        "Electric starter tidak merespon sama sekali\n \"sunyi\"",
        "Bau bensin yang kuat keluar dari knalpot",
        "Motor bisa dihidupkan dengan kick starter, tapi\n tidak dengan electric starter",
        "Tarikan motor terasa \"slip\" saat berakselerasi\n dikecepatan menengah",
        "Lampu MIL (Malfunction Indicator Lamp) di\n speedometer menyala",
        "Putaran mesin \"RPM\" tidak stabil saat langsam\n \"naik-turun\"",
        "Akselerasi terasa lambat dan tidak responsif",
        "Terdengar suara \"ngorok\" saat motor digas",
        "Kecepatan puncak \"Top speed\" motor menurun\n dari biasanya"
    ]
    
    ANSWER = {
        "K01": "V-belt Aus atau Retak",
        "K02": "Roller CVT Peyang atau Aus",
        "K03": "Busi Lemah atau Mati",
        "K04": "Aki (Baterai) Lemah atau Soak",
        "K05": "Kampas Ganda Habis",
        "K06": "Injektor Kotor atau Tersumbat"
    }

    return QUESTIONS, ANSWER

# data Menu Pilihan
def angketMenuSelection(mode):
    # di sesi Panduan Singkat
    if mode == 0:
        menu_selection = ["Lanjut", "Kembali"]
        return menu_selection
    # di sesi Pre-Submit
    if mode == 1:
        menu_selection = ["Iya", "Tidak"]
        return menu_selection
    # di sesi Hasil Perhitungan
    if mode == 2:
        menu_selection = ["Kembali"]
        return menu_selection

# konten windows untuk sesi Pre-Submit
def preSubmit(cf_values, question, current_page, screen):
    list_start = current_page * 5
    list_end = list_start + 5
    sub_question = question[list_start:list_end]
    y, x = 2, 0

    for idx, item in enumerate(sub_question):
        kode = f"G{list_start+idx+1:02d}"
        cf_val = cf_values.get(kode, 0.0)
        cf_percen = int(df.convertPercentage(cf_val, 1))

        screen.addstr(y, x+len(kode), " -> ")
        screen.addstr(y, x, f"{kode}", curses.color_pair(6))

        # menulis kode soal dan hasilnya
        if cf_percen == 50:
            screen.addstr(y, x+len(kode)+4, f"{cf_percen}")
        elif cf_percen > 50:
            screen.addstr(y, x+len(kode)+4, f"{cf_percen}", curses.color_pair(2))
        elif cf_percen < 50:
            screen.addstr(y, x+len(kode)+4, f"{cf_percen}", curses.color_pair(3))
        screen.addstr(y, x+len(kode)+4+len(str(cf_percen)), "%", curses.color_pair(5))

        # menulis soal
        screen.addstr(y+1, x, f" {item}")
        y += 4

def hasilPerhitungan(screen, results, answer):
    if not results:
        # jika tidak ada gejala
        screen.addstr(4, 2, "Tidak ada gejala yang di input!")
        screen.addstr(6, 2, "~ Tekan tombol Enter untuk kembali...")

    else:
        # cari CF terbesar
        best_k, best_cf = max(results.items(), key=lambda x: x[1])
        percent = best_cf * 100

        screen.addstr(3, 2, f"Kerusakan terbesar: {best_k}")
        screen.addstr(4, 2, f"Persentase keyakinan: {percent:.2f}%")
        screen.addstr(6, 2, f"Artinya: {answer.get(best_k, 'Tidak diketahui')}")

        # detail persentase kerusakan yang lain
        screen.addstr(8, 2, "Detail CF semua kerusakan:")

        y = 9
        for k, v in sorted(results.items(), key=lambda x: x[1], reverse=True):
            screen.addstr(y, 4, f"{k} → {v:.4f} ({v*100:.2f}%)")
            y += 1

        # Keterangan kode
        screen.addstr(y+1, 2, "Keterangan:")

        y += 2
        for idx in range(len(answer)):
            kode = f"K{idx+1:02d}"
            screen.addstr(y, 4, f"{kode} = {answer.get(kode, 'Tidak diketahui')}")
            y += 1

        screen.addstr(y+1, 2, "~ Tekan tombol Enter untuk kembali...")
