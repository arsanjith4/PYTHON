s = input("Enter the elements of the tuple, separated by commas: ")
t = tuple(map(int, s.split(",")))

print("The tuple is:", t)

li = list(t)
print("The list is:", li)

li.sort()
print("Sorted list is:", li)
