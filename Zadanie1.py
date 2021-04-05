def isPalindrome(word):
    return word == word[::-1]


if __name__ == '__main__':
    line = input("Put your word: ")
    print (str(isPalindrome(line)))