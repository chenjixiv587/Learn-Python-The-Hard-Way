class Parent():
    def override(self):
        print("PARENT override()")


class Child(Parent):
    def override(self):
        super().override()
        print("CHILD override()")


p = Parent()
c = Child()
p.override()
c.override()
