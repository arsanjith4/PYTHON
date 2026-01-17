import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

a = []

for i in range(rows):
    r = []
    for j in range(cols):
        value = int(input(f"Enter value for element ({i+1},{j+1}): "))
        r.append(value)
    a.append(r)

a = np.array(a)

print("\nOriginal Array:\n")
print(a)

print("\nSum of each row:\n")
print(np.sum(a, axis=1))

print("\nSum of each column:\n")
print(np.sum(a, axis=0))

print("\nMinimum of each row:\n")
print(np.min(a, axis=1))

print("\nMinimum of each column:\n")
print(np.min(a, axis=0))

print("\nMaximum of each row:\n")
print(np.max(a, axis=1))

print("\nMaximum of each column:\n")
print(np.max(a, axis=0))
