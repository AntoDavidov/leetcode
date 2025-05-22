def isValid(string):
    stack = []
    hashmapBrackets = {"}": "{", "]": "[", ")": "("}

    for parenthesses in string:
        if parenthesses in hashmapBrackets:
            if stack and stack[-1] == hashmapBrackets[parenthesses]:
                stack.pop()
            else:
                return False
        else:
            stack.append(parenthesses)
    return not stack

s = "([)"

result = isValid(s)
print(result)


######### EXAMPLE TRACE
#Let’s walk through "([])" step by step:

# Initial:
#stack = []

#Loop through each character.

#1. char = '('
#It’s not in hash, so it’s an opening bracket → push to stack.

#stack = ['(']

#2. char = '['
#Not in hash → push to stack.

#stack = ['(', '[']

#3. char = ']'
#It is in hash → it's a closing bracket.

#hash[char] = '['

#stack[-1] = '['

#✅ Condition is True → pop from stack.

#stack = ['(']

#4. char = ')'
#It is in hash → it's a closing bracket.

#hash[char] = '('

#stack[-1] = '('

#✅ Match → pop from stack.

#stack = []

