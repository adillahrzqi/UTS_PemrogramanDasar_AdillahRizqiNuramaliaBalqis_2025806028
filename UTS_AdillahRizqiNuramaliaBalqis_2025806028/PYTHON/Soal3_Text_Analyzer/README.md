├── soal3_text_analyzer/
│   │   ├── main.py
│   │   ├── analyzer.py
│   │   ├── utils.py
│   │   ├── input.txt                 ← file teks input
│   │   └── report.txt                ← output laporan

### 📌 Soal 3 — Analisis Teks Otomatis (Python)
**Konsep:** file I/O, string, dictionary, Counter, grafik ASCII

Program membaca file `input.txt` dan menghasilkan laporan statistik lengkap:
- Jumlah baris dan kata
- Jumlah huruf vokal dan konsonan
- 5 kata yang paling sering muncul
- Grafik frekuensi kata dalam format ASCII

Hasil laporan disimpan ke `report.txt`.

---

### ▶️ Soal 3 — Analisis Teks Otomatis (Python)

```bash
# 1. Masuk ke folder
cd Python/soal3_text_analyzer

# 2. Jalankan
python main.py
```

**Contoh output:**
```

REPORT ANALISIS TEKS OTOMATIS
================================

TEKS SUMBER:
Hello world
Saya belajar python
Program analisis teks

--------------------------------
HASIL ANALISIS:

Jumlah baris        : 3
Jumlah kata         : eight (8)
Jumlah karakter     : (53)

5 Kata paling sering:
- hello : 1
- world : 1
- saya : 1
- belajar : 1
- python: 1

Jumlah vokal        : (16)
Jumlah konsonan     : (30)

--------------------------------
KESIMPULAN:
Teks membahas pembelajaran Python dan analisis teks dengan beberapa pengulangan kata kunci seperti "python" dan "teks".