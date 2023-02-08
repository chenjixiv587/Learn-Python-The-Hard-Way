def breakWords(stuff):
    """This function will break up words for us.
    make the stuff to list"""
    words = stuff.split(' ')
    return words


# print(breakwords("he llow orl d"))


def sortWords(words):
    """Sorts the words."""
    return sorted(words)


def printFirstWord(words):
    """Print the first word after poppig it off."""
    firstWord = words.pop(0)
    print(firstWord)


def printLastWord(words):
    """Print the last words after popping it off."""
    lastWord = words.pop(-1)
    print(lastWord)


def sortSentence(sentence):
    """Takes in a full sentence and return the sorted words."""
    words = breakWords(sentence)
    return sortWords(words)


def printFirstAndLast(sentence):
    """Prints the first and last words of the sentence"""
    words = breakWords(sentence)
    printFirstWord(words)
    printLastWord(words)


def printFirstAndLastSorted(sentence):
    """Sorts the words then print the first and last one."""
    words = sortSentence(sentence)
    printFirstWord(words)
    printLastWord(words)
