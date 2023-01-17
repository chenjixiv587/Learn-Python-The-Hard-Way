i = 0
numbers = []


def getNumbers(i, step):

    while i < 20:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += step
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")
    print("The numbers: ")


getNumbers(i, 2)
for num in numbers:
    print(num)
