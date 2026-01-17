s = input("Enter a string: ")
start = int(input("Enter the start index for slicing: "))
end = int(input("Enter the end index for slicing: "))

part = s[start:end]
print(f"Sliced string (from index {start} to {end-1}): '{part}'")

first = input("Enter the first string to concatenate: ")
second = input("Enter the second string to concatenate: ")
concat = first + " " + second
print(f"Concatenated string: '{concat}'")

replicate = input("Enter the string to replicate: ")
count = int(input("Enter the number of times to replicate the string: "))
replicated = replicate * count
print(f"Replicated string: {replicated}")

length = len(s)
print(f"Length of the input string '{s}': {length}")
