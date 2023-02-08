"""
When to Use Inheritance or Composition
1. Avoid multiple inheritance at all costs, as it’s too complex to be reliable. If you’re stuck with it, then be prepared to know the class hierarchy and spend time finding where everything is coming from.

2. Use composition to package code into modules that are used in many different unrelated places and situations.

3. Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept or if you have to because of something you’re using.
"""

# 在另一个类 里面使用 一个类的构造出来的实列


class Other():
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child():
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        self.other.override()

    def altered(self):
        print("CHILD BEFORE ")
        self.other.altered()
        print("CHILD AFTER")


son = Child()
son.implicit()
son.altered()
son.override()
