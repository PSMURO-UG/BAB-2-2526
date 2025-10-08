import numpy as np
import csv

# ======================================================
# 1. Dataset 7-segment
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

numInputTypes = 10
bias = -1
threshold = 0.0

# ======================================================
# 2. Import bobot dari file CSV
# ======================================================
dataFromFile = []
with open('weights_7segment_5.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if len(row) > 0:
            dataFromFile.append(row)

# Ambil bobot dari baris ke-2 file CSV (baris pertama = header)
weights = np.array([
    float(dataFromFile[1][0]),
    float(dataFromFile[1][1]),
    float(dataFromFile[1][2]),
    float(dataFromFile[1][3]),
    float(dataFromFile[1][4]),
    float(dataFromFile[1][5]),
    float(dataFromFile[1][6]),
    float(dataFromFile[1][7]),
])

# ======================================================
# 3. Uji semua input terhadap bobot yang dimuat
# ======================================================
for j in range(numInputTypes):
    print(f"\nInput Vectors {j}: {inputVector[j]}")

    y = (bias * weights[0] +
         inputVector[j][0] * weights[1] +
         inputVector[j][1] * weights[2] +
         inputVector[j][2] * weights[3] +
         inputVector[j][3] * weights[4] +
         inputVector[j][4] * weights[5] +
         inputVector[j][5] * weights[6] +
         inputVector[j][6] * weights[7])

    # Output biner (true jika > threshold)
    output = y > threshold
    print("Output Before Threshold :", y)
    print("Final Output :", int(output))
