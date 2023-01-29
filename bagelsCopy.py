import random
# 猜数字的最大位数 比如现在是3位数 注意数字是字符串
NUMBER_GUESS_LENGTH = 3
# 猜测的最大次数
GUESS_MAX = 3


def main():
    # 打印基本信息
    print(f"""
Welcome to my game, you guess {NUMBER_GUESS_LENGTH}, you have {GUESS_MAX} chances
    """)
    # 主循环开始
    while True:
        # 随机给出数字
        secretNum = getSecretNum()
        guessCount = 1
        # 猜测次数小于给定的次数 都可以一直玩下去
        while guessCount <= GUESS_MAX:
            # 循环判断用户输入是否标准
            guess = ""
            while len(guess) != NUMBER_GUESS_LENGTH or not guess.isdecimal():
                print(f"猜的次数:{guessCount}")
                guess = input("> ")
            # 获取匹配的结果
            clues = getClues(guess, secretNum)
            print(clues)
            guessCount += 1
            # 如果给出的数字和设定的数字一样 就直接退出循环
            if guess == secretNum:
                break
            # 如果次数超标 则给出提示
            if guessCount > GUESS_MAX:
                print(f"你已经猜{guessCount-1}次了，结束了")
                print(f"设定的数字是:{secretNum}")
        # 询问是否继续玩
        print("Do you want to play again [y means yes n means no]")
        if not input("> ").lower().startswith('y'):
            break


def getClues(guess, secretNum):
    if guess == secretNum:
        return "U got it"
    clues = []
    for i in range(0, len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return "".join(clues)

# 获得随机数字（字符串格式）


def getSecretNum():
    numStr = '0123456789'
    numList = list(numStr)
    random.shuffle(numList)
    secretNum = ""
    for i in range(0, NUMBER_GUESS_LENGTH):
        secretNum += str(numList[i])
    return secretNum


if __name__ == "__main__":
    main()
