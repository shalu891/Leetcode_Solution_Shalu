class Solution(object):
    def isValid(self, s):
        stack = []
        matching = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matching:
                top_element = stack.pop() if stack else '#'
                if matching[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
        