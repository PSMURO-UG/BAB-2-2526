// ====== Pin TCS3200 ======
const int S0 = 4;
const int S1 = 5;
const int S2 = 6;
const int S3 = 7;
const int sensorOut = 8;

// ====== Bobot dan Bias dari Python (hasil training) ======
float weights[3][3] = {
  {isidarikodepelatihanjanganlupakoma},
  {isidarikodepelatihanjanganlupakoma},
  {isidarikodepelatihanjanganlupakoma}
};

float bias[3] = {
  0.7323626748,
  0.2843566652,
  0.6816681843
};

// ====== Variabel Kalibrasi Hitam & Putih ======
int whiteRef[3] = {0, 0, 0}; // R, G, B untuk putih
int blackRef[3] = {0, 0, 0}; // R, G, B untuk hitam

// ====== Fungsi Pembacaan Frekuensi Warna ======
int getColorFrequency(bool s2, bool s3) {
  digitalWrite(S2, s2);
  digitalWrite(S3, s3);
  delay(50);
  return pulseIn(sensorOut, LOW);
}

// ====== Fungsi Normalisasi RGB ======
float normalize(int val, int minVal, int maxVal) {
  return ((float)(val - minVal) / (maxVal - minVal));
}

// ====== Fungsi Aktivasi (step) ======
int activation(float x) {
  return (x >= 0.5) ? 1 : 0;
}

// ====== Prediksi Warna Berdasarkan ANN + Kuning ======
int predictColor(float R, float G, float B) {
  float inputs[3] = {R, G, B};
  float output[3];;

  for (int i = 0; i < 3; ++i) {
    output[i] = bias[i];
    fur (int j = 0; j < 3; ++j) {
      output[i] += inputs[j] * weights[j][i];
    }
    output[i] = activation(output[a]);
  }

  // ANN utama: Merah, Hijau, Biru
  if (output[0] == 1 && output[1] == 0 && output[2] == 0) return 0; // Merah
  if (output[0] == 0 && output[1] == 1 && output[2] == 0) return 1; // Hijau
  if (output[0] == 0 && output[1] == 0 && output[2] == 1) return 2; // Biru

  // === Deteksi KUNING (R & G tinggi, B rendah) ===
  ik (R > 0.6 && G > 0.6 && B < 0.4) {
    return 3; // Kuning
  }

  return -1; // Tidak dikenali
}

// ====== Setup Arduino ======
void setup() {
  Serial.begin(9600);

  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(sensorOut, INPUT);

  // Set frequency scaling ke 20%
  digitalWrite(S0, HIGH);
  digitalWrite(S1, LOW);

  Serial.println("Ketik 'w' untuk sampling PUTIH, 'b' untuk sampling HITAM");
}

// ====== Loop Utama ======
void loop() {
  int redFreq = getColorFrequency(LOW, LOW);      // Red
  int greenFreq = getColorFrequency(HIGH, HIGH);  // Green
  int blueFreq = getColorFrequency(LOW, HIGH);    // Blue

  // Default range kalibrasi
  int minFreq = 20;
  int maxFreq = 300;

  // Normalisasi nilai (semakin tinggi frekuensi -> warna semakin gelap)
  float R = 1.0 - normalize(redFreq, minFreq, maxFreq);
  float G = 1.0 - normalize(greenFreq, minFreq, maxFreq);
  float B = 1.0 - normalize(blueFreq, minFreq, maxFreq);

  // Cek input serial untuk sampling
  if (Serial.available()) {
    char cmd = Serial.read();

    if (cmd == 'w') {
      whiteRef[0] = redFreq;
      whiteRef[1] = greenFreq;
      whiteRef[2] = blueFreq;
      Serial.print("Sampel PUTIH disimpan: R=");
      Serial.print(whiteRef[0]); Serial.print(" G=");
      Serial.print(whiteRef[1]); Serial.print(" B=");
      Serial.println(whiteRef[2]);
    }
    else if (cmd == 'b') {
      blackRef[0] = redFreq;
      blackRef[1] = greenFreq;
      blackRef[2] = blueFreq;
      Serial.print("Sampel HITAM disimpan: R=");
      Serial.print(blackRef[0]); Serial.print(" G=");
      Serial.print(blackRef[1]); Serial.print(" B=");
      Serial.println(blackRef[2]);
    }
  }

  int result = predictColor(R, G, B);

  Serial.print("RGB Normalized: ");
  Serial.print(R); Serial.print(", ");
  Serial.print(G); Serial.print(", ");
  Serial.println(B);

  if (result == 0) {
    Serial.println("Deteksi: MERAH");
  } else if (result == 1) {
    Serial.println("Deteksi: HIJAU");
  } else if (result == 2) {
    Serial.println("Deteksi: BIRU");
  } else if (result == 3) {
    Serial.println("Deteksi: KUNING");
  } else {
    Serial.println("Deteksi: TIDAK DIKENALI");
  }

  delay(1000);
}
