# Billiard-Coppeliasim
<img width="1385" height="669" alt="Screenshot 2025-09-15 235325" src="https://github.com/user-attachments/assets/fa55f822-eeb1-4b45-9663-c1d3b0946cb4" />
Proyek ini mengimplementasikan permainan billiard virtual sederhana menggunakan CoppeliaSim dan Python (ZMQ Remote API).  Pengguna dapat memasukkan sudut dan kekuatan pukulan (seperti memukul bola dengan stik), lalu program akan menerjemahkannya menjadi gaya yang diberikan ke bola putih.  

---

## 🎯 Fitur
- Menghubungkan Python dengan CoppeliaSim melalui ZMQ Remote API.
- Input dari pengguna berupa **sudut pukulan (derajat)** dan **power (skalar)**.
- Input dikonversi menjadi vektor gaya global yang diberikan ke bola putih.
- Menampilkan posisi terbaru dari bola setelah setiap pukulan.
- Ditujukan untuk tujuan edukasi: memahami cara mengambil data dan mengirim perintah di CoppeliaSim.

## 📦 Kebutuhan
- **CoppeliaSim** terpasang di komputer.
- **Python 3.8+**
- Library Python yang diperlukan:
  ```bash
  pip install coppeliasim-zmqremoteapi-client numpy

## 🛠️ Tantangan
-Perbedaan versi API (misalnya fungsi addForceAndTorque tidak selalu sama).
-Konversi input sederhana (sudut + power) menjadi vektor gaya global.
-Sinkronisasi antara Python dan simulasi di CoppeliaSim.

## ✨ Skill yang Dipelajari
-Integrasi Python–CoppeliaSim menggunakan ZMQ Remote API.
-Simulasi gaya impulsif dan torsi.
-Membuat program interaktif sederhana via terminal.

---

<img width="500" height="206" alt="image" src="https://github.com/user-attachments/assets/61b7ee59-2dc5-4ffb-85f1-05710c14791c" /> 
