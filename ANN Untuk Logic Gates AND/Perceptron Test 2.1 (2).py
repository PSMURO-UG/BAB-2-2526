import numpy as np
# Import numpy untuk operasi array.

# ======================================================
# 1. Load bobot dan bias hasil training
# ======================================================
w = np.load('weights.npy')
b = np.load('bias.npy')
# Memuat bobot dan bias hasil training.

# ======================================================
# 2. Fungsi aktivasi step
# ======================================================
def step(x):
    return 1 if x >= 0 else 0

# ======================================================
# 3. Data uji (fungsi logika AND)
# ======================================================
X_test = np.array([[0, 0],
                   [0, 1],
                   [1, 0],
                   [1, 1]])

# ======================================================
# 4. Uji model
# ======================================================
print("Testing Perceptron Logic AND")
for x in X_test:
    z = np.dot(x, w) + b
    y_pred = step(z)
    print(f"Input: {x} -> Output Prediksi: {y_pred}")
