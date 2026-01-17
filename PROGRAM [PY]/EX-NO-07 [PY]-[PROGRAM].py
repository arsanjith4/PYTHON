import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

a = []
for i in range(rows):
    r = []
    for j in range(cols):
        r.append(int(input("Enter value: ")))
    a.append(r)

a = np.array(a)
print("Original Array:")
print(a)

search = int(input("Enter element to search: "))
result = np.where(a == search)

if result[0].size > 0:
    print("Element found at:")
    for r, c in zip(result[0], result[1]):
        print("Row:", r + 1, "Column:", c + 1)
else:
    print("Element not found")
