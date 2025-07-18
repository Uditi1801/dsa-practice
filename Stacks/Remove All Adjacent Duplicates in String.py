def remove_adjacent_duplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove the duplicate
        else:
            stack.append(char)  # Add new character
    return ''.join(stack)

# Example usage:
print(remove_adjacent_duplicates("abbaca"))  # Output: ca
