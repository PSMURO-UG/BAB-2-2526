import numpy as np

# ===== Dataset RGB (0–255) =====
# Format: [R, G, B]
X = np.array([
    # Merah
    [255, 0, 0],
    [200, 50, 50],
    [180, 30, 30],
    [220, 80, 70],
    # Hijau
    [0, 255, 0],
    [50, 200, 50],
    [30, 180, 40],
    [80, 220, 90],
    # Biru
    [0, 0, 255],
    [50, 50, 200],
    [40, 30, 180],
    [70, 80, 220],
])

# ===== Label target (one-hot) =====
# [Merah, Hijau, Biru]
y = np.array([
    [1, 0, 0],  # Merah
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [0, 1, 0],  # Hijau
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 1],  # Biru
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1],
])

# ===== Normalisasi ke 0–1 =====
X = X / 255.0

# ===== Parameter model =====
np.random.seed(42)
w = np.random.rand(3, 3)  # 3 input → 3 output neuron
b = np.random.rand(3)
lr = 0.1
epochs = 1000

# ===== Fungsi Softmax =====
def softmax(z):
    e_z = np.exp(z - np.max(z))
    return e_z / e_z.sum()

# ===== Training loop =====
for epoch in range(epochs):
    for i in range(len(X)):
        z = np.dot(X[i], w) + b
        y_pred = softmax(z)
        error = y[i] - y_pred
        w += lr * np.outer(X[i], error)
        b += lr * error

# ===== Simpan bobot dan bias =====
np.savetxt("weights.txt", w)
np.savetxt("bias.txt", b)
print("✅ Training selesai. Bobot dan bias disimpan ke file.")
