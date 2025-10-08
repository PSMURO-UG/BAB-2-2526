import numpy as np
import matplotlib.pyplot as plt
import csv

# ======================================================
# 1. Dataset 7-segment (0–9)
# ======================================================
inputVector = np.array([
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 1, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1]   # 9
])

# ======================================================
# 2. One-hot target (pilih angka yang ingin dilatih)
# Contoh: angka 5
# ======================================================
desiredOut = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0])

numInputTypes = 10
bias = -1
learningRate = 0.1
iterations = 5000

# ======================================================
# 3. Inisialisasi bobot (7 input + 1 bias = 8 bobot)
# ======================================================
weights = 0.1 * np.random.rand(8, 1)
error = np.ones((1, iterations))

# ======================================================
# 4. Fungsi aktivasi
# ======================================================
def binaryStep(x):
    return np.where(x >= 0, 1, 0)

def elu(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))

def relu(x):
    return np.maximum(0, x)

def leakyRelu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def gelu(x):
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * x**3)))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def maxout(x):
    return np.max(x, axis=0)

def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / np.sum(exp_x, axis=0)

def softplus(x):
    return np.log(1 + np.exp(x))

def tanh(x):
    return np.tanh(x)

def swish(x):
    return x / (1 + np.exp(-x))

def threshold(x):
    return 1 if x > 0 else 0

# ======================================================
# 5. Training loop
# ======================================================
for i in range(iterations):
    out = np.zeros((10, 1))

    for j in range(numInputTypes):
        y = (bias * weights[0] +
             inputVector[j][0] * weights[1] +
             inputVector[j][1] * weights[2] +
             inputVector[j][2] * weights[3] +
             inputVector[j][3] * weights[4] +
             inputVector[j][4] * weights[5] +
             inputVector[j][5] * weights[6] +
             inputVector[j][6] * weights[7])

        # Pilih aktivasi yang ingin dipakai:
        # out[j] = binaryStep(y)
        # out[j] = relu(y)
        out[j] = softplus(y)   # ← contoh pakai softplus

        delta = desiredOut[j] - out[j, 0]

        # Update bobot (Perceptron learning)
        weights[0] = weights[0] + learningRate * bias * delta
        weights[1] = weights[1] + learningRate * inputVector[j][0] * delta
        weights[2] = weights[2] + learningRate * inputVector[j][1] * delta
        weights[3] = weights[3] + learningRate * inputVector[j][2] * delta
        weights[4] = weights[4] + learningRate * inputVector[j][3] * delta
        weights[5] = weights[5] + learningRate * inputVector[j][4] * delta
        weights[6] = weights[6] + learningRate * inputVector[j][5] * delta
        weights[7] = weights[7] + learningRate * inputVector[j][6] * delta

        error[0][i] = delta

# ======================================================
# 6. Plot error selama training
# ======================================================
plt.plot(np.arange(0, iterations, 1), error[0])
plt.ylabel('Error')
plt.xlabel('Iteration')
plt.title('Training Error')
plt.grid(True)
plt.show()

# ======================================================
# 7. Tampilkan bobot akhir
# ======================================================
print("\nFinal weights : ")
for idx in range(8):
    print(f"w{idx} : {weights[idx][0]}")

# ======================================================
# 8. Simpan bobot ke file CSV
# ======================================================
with open('weights_7segment_5.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(('W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7'))
    writer.writerow([weights[0][0],
                     weights[1][0],
                     weights[2][0],
                     weights[3][0],
                     weights[4][0],
                     weights[5][0],
                     weights[6][0],
                     weights[7][0]])

print("Values file exported: weights_7segment_5.csv")
