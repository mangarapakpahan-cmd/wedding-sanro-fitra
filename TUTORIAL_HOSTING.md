# 🔥 Panduan Lengkap Hosting Undangan Pernikahan (Google Firebase + Vercel)

Panduan langkah demi langkah untuk meng-online-kan website undangan **Sanro & Fitra** menggunakan **Google Firebase Realtime Database** (database doa restu gratis & tanpa batas proyek seperti Supabase) dan **Vercel** (hosting web gratis 24 jam dengan HTTPS).

---

## 📋 Ikhtisar Arsitektur

- **Google Firebase (Realtime Database)**:
  - Layanan database cloud resmi dari Google (*Spark Plan* 100% Gratis).
  - Menyimpan seluruh ucapan dan doa restu secara permanen dan otomatis sinkron *real-time* ke semua perangkat.
  - **Biaya**: **100% Gratis** tanpa batas ketat proyek.
- **Vercel (Frontend Hosting)**:
  - Meng-online-kan file website (HTML, CSS, JS, Foto, Musik).
  - Domain gratis HTTPS (contoh: `https://wedding-sanro-fitra.vercel.app`).
  - **Biaya**: **100% Gratis**.

---

## 🗄️ TAHAP 1: Menyiapkan Google Firebase Realtime Database (5 Menit)

### Langkah 1: Buat Proyek Firebase Baru
1. Buka [https://console.firebase.google.com](https://console.firebase.google.com) dan login menggunakan akun Google / Gmail Anda.
2. Klik tombol **Tambahkan Proyek** (*Add project*).
3. Masukkan nama proyek: `wedding-sanro-fitra`.
4. Klik **Lanjutkan** (*Continue*).
5. Pada pilihan *Google Analytics*, matikan (*toggle off*) saja agar lebih cepat, lalu klik **Buat proyek** (*Create project*).
6. Tunggu beberapa detik hingga proyek selesai disiapkan, lalu klik **Lanjutkan**.

---

### Langkah 2: Buat Realtime Database
1. Di bilah menu sebelah kiri, klik **Build** -> pilih **Realtime Database**.
2. Klik tombol **Buat Database** (*Create Database*).
3. Pada lokasi database, pilih **Singapore (asia-southeast1)** atau **United States (us-central1)** (keduanya sama-sama cepat). Klik **Berikutnya**.
4. Pada pilihan aturan keamanan, pilih **Mulai dalam mode pengujian** (*Start in test mode*) atau **Mode terkunci**, lalu klik **Aktifkan** (*Enable*).

---

### Langkah 3: Atur Aturan Keamanan (*Security Rules*)
Agar para tamu undangan bisa membaca dan mengirim doa tanpa perlu login akun Google:
1. Pada halaman Realtime Database yang baru dibuat, klik tab **Rules** (*Aturan*) di bagian atas.
2. Ubah isi kodenya menjadi seperti ini:
   ```json
   {
     "rules": {
       "wedding_wishes": {
         ".read": true,
         ".write": true
       }
     }
   }
   ```
3. Klik tombol **Publikasikan** (*Publish*).

---

### Langkah 4: Ambil Konfigurasi Firebase & Tempel ke `script.js`
1. Di menu kiri paling atas, klik ikon **Roda Gigi** (di samping *Project Overview*) -> pilih **Setelan proyek** (*Project settings*).
2. Gulir ke bawah ke bagian **Aplikasi Anda** (*Your apps*).
3. Klik ikon web: **`</>`**.
4. Masukkan nama panggilan aplikasi: `web-undangan` (tidak perlu centang Firebase Hosting), lalu klik **Daftarkan aplikasi** (*Register app*).
5. Firebase akan menampilkan objek konfigurasi seperti ini:
   ```javascript
   const firebaseConfig = {
     apiKey: "AIzaSyD-...",
     authDomain: "wedding-sanro-fitra.firebaseapp.com",
     databaseURL: "https://wedding-sanro-fitra-default-rtdb.asia-southeast1.firebasedatabase.app",
     projectId: "wedding-sanro-fitra",
     storageBucket: "wedding-sanro-fitra.appspot.com",
     messagingSenderId: "123456789",
     appId: "1:123456789:web:abcdef"
   };
   ```
6. Salin bagian dalam kurung kurawal `{ ... }` tersebut.
7. Buka berkas `script.js` di baris 146, lalu ganti `firebaseConfig` dengan konfigurasi milik Anda:
   ```javascript
   const firebaseConfig = {
     apiKey: "AIzaSyD-...",
     authDomain: "wedding-sanro-fitra.firebaseapp.com",
     databaseURL: "https://wedding-sanro-fitra-default-rtdb.asia-southeast1.firebasedatabase.app",
     projectId: "wedding-sanro-fitra",
     storageBucket: "wedding-sanro-fitra.appspot.com",
     messagingSenderId: "123456789",
     appId: "1:123456789:web:abcdef"
   };
   ```
8. Simpan berkas (`Ctrl + S`). Sekarang sistem buku doa sudah terhubung ke Google Firebase secara *real-time*!

---

## ⚡ TAHAP 2: Meng-online-kan Website di Vercel

### Cara A: Melalui GitHub + Vercel Dashboard (Paling Mudah)

1. **Buat Repositori di GitHub**:
   - Buka [https://github.com](https://github.com) dan login.
   - Klik **New** (Buat repositori baru).
   - Beri nama: `wedding-sanro-fitra`, lalu klik **Create repository**.

2. **Unggah Kode dari Komputer Anda**:
   Buka terminal / PowerShell di folder proyek Anda:
   ```powershell
   cd C:\Users\manga\.gemini\antigravity\scratch\wedding-sanro-fitra
   git add .
   git commit -m "feat: connect to firebase realtime database"
   git branch -M main
   git remote add origin https://github.com/USERNAME_GITHUB_ANDA/wedding-sanro-fitra.git
   git push -u origin main
   ```
   *(Ganti `USERNAME_GITHUB_ANDA` dengan username GitHub Anda).*

3. **Deploy di Vercel**:
   - Buka [https://vercel.com](https://vercel.com) dan login dengan akun GitHub Anda.
   - Klik **Add New...** -> pilih **Project**.
   - Pilih repositori `wedding-sanro-fitra` lalu klik **Import**.
   - Pada bagian **Framework Preset**, biarkan nilai default **Other**.
   - Klik tombol **Deploy**!
   - Website Anda langsung aktif di link:
     `https://wedding-sanro-fitra.vercel.app` 🎉

---

### Cara B: Langsung dari Terminal (Tanpa GitHub)

1. Buka PowerShell di folder proyek:
   ```powershell
   cd C:\Users\manga\.gemini\antigravity\scratch\wedding-sanro-fitra
   ```
2. Jalankan perintah Vercel:
   ```powershell
   npx vercel
   ```
3. Ikuti petunjuk login browser dan tekan Enter untuk pertanyaan yang muncul.
4. Terakhir, jalankan perintah rilis utama:
   ```powershell
   npx vercel --prod
   ```

---

## 💌 Cara Mengirim Link Khusus Nama Tamu (WhatsApp)

Setelah website aktif di Vercel, bagikan link dengan parameter nama tamu:

- `https://wedding-sanro-fitra.vercel.app/?to=Bpk.+Roberto+Simanjuntak`
- `https://wedding-sanro-fitra.vercel.app/?to=Keluarga+Besar+Opung+Bona`
- `https://wedding-sanro-fitra.vercel.app/?to=Sahabat+Tercinta`

Saat tamu membuka tautan tersebut:
1. Kartu nama di halaman sampul otomatis memuat nama tamu.
2. Kolom nama pada buku doa otomatis terisi.
3. Seluruh doa yang dikirim tamu akan langsung masuk ke database Firebase dan otomatis muncul seketika di layar seluruh tamu & keluarga!
