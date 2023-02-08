class Game():
    def __init__(self, x) -> None:
        self.x = x
    def check(self):
        try:
            num = int(input("> "))
        except ValueError:
            num = 0
        return self.x == num