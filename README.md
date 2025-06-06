# b2b_scraper_projects


---

## 📑 report.pdf (isi naskah)

Berikut adalah naskah isi `report.pdf` dalam format Markdown atau Word yang bisa kamu convert ke PDF:

---

### 📘 Laporan Akhir: B2B Scraper Project

**Nama:** Ahmad Zulal Zaqi  
**Tanggal:** Juni 2025  
**Judul:** Otomatisasi Pengambilan Kontak B2B dari Daftar Domain

---

#### 1. **Latar Belakang**

Di era digital saat ini, kebutuhan untuk menjangkau perusahaan lain (B2B) semakin tinggi. Namun, proses pencarian email atau kontak dari website satu per satu sangat memakan waktu. Oleh karena itu, diperlukan sistem otomatis yang mampu mengumpulkan data dari banyak domain secara efisien.

---

#### 2. **Tujuan**

Membangun scraper modular untuk mengekstrak:
- Email,
- Nomor telepon,
- Tautan kontak,
serta menyajikan dashboard analitik dan file hasil.

---

#### 3. **Metodologi**

- **Input:** Daftar domain (CSV)
- **Proses:**
  - Buka halaman HTML,
  - Parse konten menggunakan BeautifulSoup,
  - Ekstrak dengan Regex untuk email, phone, dan contact link,
- **Output:** Preview + Analytics + Export CSV

---

#### 4. **Hasil**

- Total domain: 7
- Total email ditemukan: 380
- Total nomor telepon: 1349
- Total link kontak: 8

**Contoh domain:**  
`https://qiscus.com` — 4 email ditemukan

---

#### 5. **Kelebihan Sistem**

- Modular dan scalable
- Bisa dikembangkan menjadi aplikasi web
- Output rapi dan bisa di-export

---

#### 6. **Rencana Pengembangan**

- Integrasi visual (Streamlit)
- Tambah grafik & summary insight
- Validasi hasil (cek format email/telepon)
- Handling blocked request (retry / proxy)

---

#### 7. **Kesimpulan**

Sistem telah bekerja dengan baik sesuai target. Tinggal menambahkan UI/UX untuk menyempurnakan user experience dan meningkatkan nilai tambah proyek ini ke level produksi.

---

Kalau kamu mau Putri bantu export ke **PDF** juga, tinggal bilang aja ya — bisa langsung tak buatkan. Mau langsung PDF-nya sekarang?
