class Parent():
    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
    def implicit(self):
        print("SON")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()
