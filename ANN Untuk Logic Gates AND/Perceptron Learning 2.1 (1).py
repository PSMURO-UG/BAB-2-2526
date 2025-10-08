import numpy as np
import matplotlib.pyplot as plt

# ======================================================
# 1. Dataset AND gate
# ======================================================
# X = input (2 fitur: A dan B), y = target output (AND)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([0, 0, 0, 1])

# ======================================================
# 2. Inisialisasi parameter
# ======================================================
w = np.random.rand(2)   # bobot awal random (2 input)
b = np.random.rand(1)   # bias awal random
lr = 0.1                # learning rate
epochs = 20             # jumlah iterasi training

# ======================================================
# 3. Fungsi aktivasi step
# ======================================================
def step(x):
    return 1 if x >= 0 else 0

# ======================================================
# 4. Proses Training Perceptron
# ======================================================
error_history = []

for epoch in range(epochs):
    total_error = 0
    for i in range(len(X)):
        z = np.dot(X[i], w) + b         # kalkulasi weighted sum
        y_pred = step(z)               # output prediksi (0 atau 1)
        error = y[i] - y_pred          # error = target - prediksi

        # Update bobot dan bias (Perceptron Learning Rule)
        w += lr * error * X[i]
        b += lr * error

        total_error += abs(error)

    error_history.append(total_error)
    print(f"Epoch {epoch+1} | Total Error: {total_error} | w: {w} | b: {b}")

# ======================================================
# 5. Simpan bobot & bias hasil training
# ======================================================
np.save('weights.npy', w)
np.save('bias.npy', b)

# ======================================================
# 6. Plot Grafik Error per Epoch
# ======================================================
plt.plot(error_history, marker='o')
plt.title("Grafik Total Error per Epoch")
plt.xlabel("Epoch")
plt.ylabel("Total Error")
plt.grid(True)
plt.show()
