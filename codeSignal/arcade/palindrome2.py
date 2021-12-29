def palindrome(inputString):
    n=len(inputString)

    for i in range(n//2):
        if inputString[i] != inputString[n-i-1]:
            return False

    return True



if __name__ == "__main__":

    print(palindrome('mym'))
    print(palindrome('hello'))
    print(palindrome('nisioisin')) 
