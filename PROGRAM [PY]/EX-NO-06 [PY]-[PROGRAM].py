import numpy as np

n = int(input("Enter the number of elements: "))
a = []

for i in range(n):
    a.append(int(input("Enter element: ")))

a = np.array(a)

row = int(input("Enter number of rows: "))

if n % row != 0:
    print("Reshape not possible. Number of elements is not divisible by rows.")
else:
    col = n // row
    a2 = a.reshape(row, col)

    print("2D Array:")
    print(a2)

    print("First two columns:")
    print(a2[:, :2])
