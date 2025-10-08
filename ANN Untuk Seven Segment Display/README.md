# color-detection-arduino-uno

## Pin Out

| Pin Arduino | Fungsi              |
|-------------|---------------------|
| 4           | S0 (TCS3200)        |
| 5           | S1 (TCS3200)        |
| 6           | S2 (TCS3200)        |
| 7           | S3 (TCS3200)        |
| 8           | sensorOut (TCS3200) |
| 9           | LED Merah           |
| 10          | LED Hijau           |
| 11          | LED Biru            |

## Output Program

- Serial monitor menampilkan hasil normalisasi RGB dan deteksi warna:
  - "Deteksi: MERAH"
  - "Deteksi: HIJAU"
  - "Deteksi: BIRU"
  - "Deteksi: TIDAK DIKENALI"
- LED indikator menyala sesuai hasil deteksi warna:
  - LED Merah untuk warna merah
  - LED Hijau untuk warna hijau
  - LED Biru untuk warna biru

- Untuk kalibrasi warna dasar, gunakan perintah serial:
  - Ketik 'w' untuk sampling PUTIH
  - Ketik 'b' untuk sampling HITAM

## Bobot dan Bias (Hasil Training Python di Spyder 6.0)

Berikut bobot dan bias yang digunakan pada jaringan syaraf tiruan sederhana, hasil training di Python (Spyder 6.0):

**Weights (Bobot):**
```
float weights[3][3] = {
  {5.905637288, -1.7600959720, -2.0883289398},
  {-2.4917673708, 5.9018896783, -2.4899542626},
  {-2.3446083106, -1.9130676520, 5.7831227323}
};
```

**Bias:**
```
float bias[3] = {
  0.7323626748,
  0.2843566652,
  0.6816681843
};
```

Bobot dan bias tersebut diambil dari hasil training dan diterapkan langsung pada kode Arduino untuk proses prediksi warna menggunakan model ANN.

<img width="487" height="314" alt="image" src="https://github.com/user-attachments/assets/0c282e78-88b8-4631-8561-333f1907ae6a" />
