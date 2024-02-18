class Solution(object):
    def isValid(self, s):
        stack = [] # create an empty stack to store opening brackets
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for c in s: # loop through each character in the string
            if c in pairs:
                stack.append(c) # push it onto the stack
            elif len(stack) == 0 or c != pairs[stack.pop()]:
                return False
        return len(stack) == 0
        