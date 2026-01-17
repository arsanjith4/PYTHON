d = {}
n = int(input("Enter the number of key-value pairs: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value
print("Dictionary created:", d)
keycheck = input("Enter the key to check: ")
if keycheck in d:
    print("The key exists in the dictionary.")
else:
    print("The key does not exist in the dictionary.")
valuecheck = input("Enter the value to check: ")
if valuecheck in d.values():
    print("The value exists in the dictionary.")
else:
    print("The value does not exist in the dictionary.")
