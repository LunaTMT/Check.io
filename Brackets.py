

stack = []
brackets = {'(': ')', '[': ']', '{': '}'}

for char in s:
    if char in brackets.keys():
        stack.append(char)
    elif char in brackets.values():
        if not stack or brackets[stack.pop()] != char:
            return False

return not stack