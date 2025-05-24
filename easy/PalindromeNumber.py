def isPalindrome(x):
    number = str(x)
    reversed_number = number[::-1]
    if reversed_number == number:
        return True
    else:
        return False


n = 1221
print(isPalindrome(n))


