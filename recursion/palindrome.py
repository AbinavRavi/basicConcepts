# Task: check if a given string is palindrom or not by recursion

def ispalindrome(word):
    return word == word[::-1]

if __name__ == "__main__":
    print(ispalindrome("abinav"))