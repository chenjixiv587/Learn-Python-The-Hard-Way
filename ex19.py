def cheeseAndCrackers(cheeseCount, boxesOfCrackers):
    print(f"You have {cheeseCount} cheeses")
    print(f"You have {boxesOfCrackers} boxes of crackers")
    print("Man that is enough for a party.")
    print("Get a blanket.\n")


print("We can just give the function nunbers directly.")
cheeseAndCrackers(30, 30)
print("OR, we can use variables from our scipt:")
amountOfChesese = 10
amountOfCrackers = 50

cheeseAndCrackers(amountOfChesese, amountOfCrackers)
print("We can even do math inside too:")
cheeseAndCrackers(10 + 20, 5 + 6)
print("And we can combine the two, variables and math:")
cheeseAndCrackers(amountOfChesese + 100, amountOfCrackers + 10000)
