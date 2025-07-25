#check if a string is palindrome
#Method1:
def is_palindrome(s):
    return s==s[::-1]
print(is_palindrome("listen"))

#Method2:
def is_palindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        while left<right and not s[left].isalnum():
            left+=1
        while left<right and not s[right].isalnum():
            right-=1
        if s[left].lower()!=s[right].lower():
            return False
        left+=1
        right-=1
    return True
