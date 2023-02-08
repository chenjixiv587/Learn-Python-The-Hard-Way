print("Let's practice everything.")
print('You\'d need to know \' about escapes with \\ that do.')
print('\n newlines and \t tabs')
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""

print('-' * 14)
print(poem)
print('-' * 14)

five = 10 - 2 + 3 - 6
print(f'This should be five: {five}')


def secretFormula(started):
    jellyBeans = started * 500
    jars = jellyBeans / 1000
    crates = jars / 100
    return jellyBeans, jars, crates
    # 函数返回的是元组


startPoint = 10000
beans, jars, crates = secretFormula(startPoint)
print("With a starting point of {}".format(startPoint))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates")

startPoint = startPoint / 10
print("We can also do this way")
formula = secretFormula(startPoint)
print(type(formula))  # 函数返回的是元组
# this is an easy way to apply a list to a format string.
print("We'd have {} beans {} jars {} crates.".format(*formula))
