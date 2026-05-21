# 🎮 Guess Battle Game (Python)

Game tebak angka berbasis CLI menggunakan Python.

## 📌 Fitur
- Login pemain
- Multi level permainan
- Sistem skor otomatis
- Menyimpan skor ke file JSON
- Menampilkan Top 5 pemain terbaik
- Warna terminal menggunakan Colorama
- Error handling menggunakan try-except

---

# 📁 Struktur Project

project/
│
├── main.py
├── game.py
├── scoreboard.py
├── scores.json
└── README.md

### ▶️ Soal 2 — Game Guess Battle (Python)

```bash
# 1. Masuk ke folder
cd Python/soal2_game_guess

# 2. Jalankan
python main.py
```

**Alur permainan:**
```
=== WELCOME TO GUESS BATTLE ===
Masukkan nama pemain: Ahmad
=== Level 1 | Tebak 1-10 | 3 percobaan ===
Tebakan kamu: 5
Terlalu kecil! Sisa: 2
Tebakan kamu: 8
Benar! +40 poin
...
=== TOP 5 SCORE ===
1. Ahmad – 120 pts
```

---