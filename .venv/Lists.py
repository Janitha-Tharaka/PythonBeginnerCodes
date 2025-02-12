names = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth"]
print(names[0])
print(names[1])
# Negative will print from back
print(names[-1])
print(names[-2])
print()

names[0] = "FirstButChanged"
# Print from 0 to the 2nd (3rd one not showing)
print(names[0:3])

print("---------List Methods---------\n")
numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# numbers.insert(2,2.5)
# numbers.remove(2.5)
# numbers.clear()
# print(numbers)
# print(1 in numbers)
print(len(numbers))

