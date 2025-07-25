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
