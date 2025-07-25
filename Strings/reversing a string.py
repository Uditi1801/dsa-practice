#reversing a string
#Method1:
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))

#Method2:
def reversed_string(s):
    result=""
    for char in s:
        result=char+result#adds current char to front
    return result
print(reversed_string("hello"))
print(reversed_string("uditi"))

#Method3-Two Pointer Approach:
def reversed_string(s):
    s=list(s)
    left=0
    right=len(s)-1
    s[left],s[right]==s[right],s[left]
    left+=1
    right-=1
    return ".join(s)
