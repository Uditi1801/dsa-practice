class MyStack:
    def __init__(self):
        # We start with an empty list to store items
        self.stack = []

    def push(self, x):
        # Just add the item to the end (top) of the list
        self.stack.append(x)

    def pop(self):
        # Remove and return the top item
        if not self.isEmpty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        # Look at the top item, but don’t remove it
        if not self.isEmpty():
            return self.stack[-1]
        return "Stack is empty"

    def isEmpty(self):
        # Check if the list is empty
        return len(self.stack) == 0
