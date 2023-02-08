import random
# 猜测的数字个数
NUM_DIGITS = 3  # Try setting this to 1 or 10
# 猜测的最大次数
MAX_GUESSES = 10  # Try setting this to 1 or 100


def main():
    print(f"""Bagles, a deductive logic game.
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
 Try to guess what it is. Here are some clues:
 When I say:    That means:
 Pico         One digit is correct but in the wrong position.
 Fermi        One digit is correct and in the right position.
 Bagels       No digit is correct.
 
 For example, if the secret number was 248 and your guess was 843, the
 clues would be Fermi Pico.""")
# 主循环
    while True:
        # need generate a secretNum
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print(f"You have {MAX_GUESSES} guesses to get it.")
        # 猜的次数从 1 开始
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            # 判断输入 当输入的不符合要求的时候 就循环询问
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}")
                guess = input("> ")
            # 获取匹配的结果
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            # 当两个结果一样时  就退出循环
            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secretNum}")
        print("Do you want to play again?(yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing.")


def getClues(guess, secretNum):
    if guess == secretNum:
        return "you got it!"
        # 互相匹配  将结果保存在 列表中 并最终以字符串的形式展示出来
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return " ".join(clues)


def getSecretNum():
    """Return a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789")
    # 打乱顺序
    random.shuffle(numbers)
    secretNum = ""
    # 随机生成三个
    for i in range(0, NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


if __name__ == "__main__":
    main()
