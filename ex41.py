import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef__init__(self, ***)":
    "class %%% has-a __init__ that takes self and *** paras",
    "class %%%(object):\n\t\def ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'"

}

# do they want to drill phrase first

if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

# load up the words from the website
# 将文件里面的文字 写入到 WORDS 列表中
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    """

    """
    classNames = [w.capitalize()
                  for w in random.sample(WORDS, snippet.count("%%%"))]
    otherNames = random.sample(WORDS, snippet.count("***"))
    results = []
    paramNames = []

    for i in range(0, snippet.count("@@@")):
        paramCount = random.randint(1, 3)
        paramNames.append(', '.join(random.sample(WORDS, paramCount)))

    for sentence in snippet, phrase:
        result = sentence[:]
        # fake class names
        for word in classNames:
            result = result.replace("%%%", word, 1)
        # fake other names
        for word in otherNames:
            result = result.replace("***", word, 1)
        # fake parameter lists
        for word in paramNames:
            result = result.replace("@@@", word, 1)

        results.append(result)
    return results

# keep going untill they hit CTRL-D


try:
    while True:
        # snippets 是由 PHRASES 的 键组成的列表
        snippets = list(PHRASES.keys())
        # 随机打乱
        random.shuffle(snippets)
        # snippet 是每一个对应的键
        for snippet in snippets:
            # phrase 就是对应的值
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question, answer = answer, question
            print(question)
            input("< ")
            print(f"ANSWER: {answer}\n\n")

except EOFError:
    print("\nBye!")
