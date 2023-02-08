theCount = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list.
for number in theCount:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit pf type:{fruit}")

for i in change:
    print(f"I got {i}")
# We can also build lists, first start with an empty one.
elements = []

# range(left, right)
# left is included anf right is not included.
for j in range(0, 5):
    print(f"Adding {j} to the list")
    elements.append(j)
for e in elements:
    print(f"Element was: {e}")

numbers = [i ** 2 for i in range(0, 3)]
print(numbers)

