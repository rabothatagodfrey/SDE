
def isPalindrome(num):
    """get parameter number and determine if is palindrome """
    
    str_num = str(num)
    if not len(str_num) > 1:
        return True
    
    R = len(str_num) - 1
    L = 0
    print(f"L:{L}. R:{R}")

    while L < R:
        if str_num[L] == str_num[R]:
            L += 1
            R -= 1
        else:
            return False
    return True

if __name__ == "__main__":
    num = 1000021
    print(isPalindrome(num))