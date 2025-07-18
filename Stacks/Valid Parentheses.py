#code:
def is_valid(s):
    stack=[]
    mapping={')':'(','}':'{',']':'['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1]!=mapping[char]:
                return False
            stack.pop()
        else:
            continue
    return not stack
print(is_valid("{[]}"))
