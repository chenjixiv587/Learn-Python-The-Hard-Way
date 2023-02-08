import random
# 设定猜测的数字的位数
MAX_LENGTH = 3
# 设定猜测的次数
MAX_GUESS = 10

# 游戏开始:


def main():
    gameStart = True
    while gameStart:
        # 猜测次数从1 开始
        guessCount = 1
        # 给定设定的数字
        secretNum = getSecretNum()
        # 猜测的次数小于等于设定的次数都可以继续玩
        while guessCount <= MAX_GUESS:
            # 判断用户的输入是否符合标准
            userGuess = ""
            while len(userGuess) != MAX_LENGTH or not userGuess.isdecimal():
                print(f"你第{guessCount}次猜")
                userGuess = input("> ")
            # 展示结果
            result = getResult(userGuess, secretNum)
            print(result)
            # 如果用户输入的和给定的一致 那么结束循环
            if userGuess == secretNum:
                break
            guessCount += 1

        print(f"你一共猜了{guessCount}次")
        print(f"秘密数字是{secretNum}")
        # 询问用户是否还要继续玩
        print("还想继续玩吗？y 表示还想玩， n 表示不玩了")
        if not input("> ").lower().startswith("y"):
            gameStart = False


# 比较结果

def getResult(userGuess, secretNumber):
    if userGuess == secretNumber:
        return "U WIN"
    # 得到随机的数字
    result = []
    for i in range(len(userGuess)):
        if userGuess[i] == secretNumber[i]:
            result.append("一致")
        elif userGuess[i] in secretNumber:
            result.append("其中")
    if len(result) == 0:
        return "不对"
    else:
        result.sort()
        return "".join(result)


def getSecretNum():
    secretNum = ""
    secretList = list('0123456789')
    random.shuffle(secretList)
    for i in range(MAX_LENGTH):
        secretNum += str(secretList[i])
    return secretNum


if __name__ == "__main__":
    main()
