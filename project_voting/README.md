# Proyek Akhir Backend: Sistem Voting Online

## 1. Deskripsi Singkat
Aplikasi backend ini dikembangkan untuk mengelola sistem pemungutan suara (voting) secara transparan dan efisien.

## 2. Anggota Tim
- I Made Anom Wibawa - 240030465 - Username GitHub : AnomWibawa - Peran: Backend Developer

## 3. Lingkungan Pengembangan
- **Bahasa**: Python 3.12
- **Framework**: FastAPI
- **Database**: SQLite
- **Alat**: Uvicorn, SQLAlchemy

## 4. Proses Bisnis
1. User melakukan registrasi akun.
2. User yang telah login dapat membuat polling baru dengan deskripsi dan pilihan.
3. Setiap user hanya diperbolehkan memberikan 1 suara per polling.
4. Hasil voting dapat dilihat secara real-time.

## 5. Struktur Folder
```text
project_voting/
├── app/
│   ├── schemas/       # Definisi format data (Pydantic)
│   ├── repository/    # Logika akses database
│   ├── routers/       # Pengaturan endpoint URL
│   ├── models.py      # Definisi tabel database
│   └── database.py    # Konfigurasi koneksi SQLite
├── main.py            # Entry point aplikasi
└── README.md          # Dokumentasi proyek


