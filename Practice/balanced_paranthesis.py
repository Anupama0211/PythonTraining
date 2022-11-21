# Check if brackets are balanced in expression: "(a=2,b={)" -> Not balanced , "(a=2,b={})" ->balance

def balanced_paranthesis(brackets):
    stack = []
    dictionary_of_brackets = {"(": ")", "{": "}", "[": "]"}
    left_brackets = ["(", "{", "["]
    for bracket in brackets:
        if (bracket in left_brackets):
            stack.append(bracket)
        elif (bracket in dictionary_of_brackets.values() and len(stack) != 0):
            left_bracket = stack.pop()
            if (dictionary_of_brackets[left_bracket] != bracket):
                return -1
    if len(stack) != 0:
        return -1
    return 0


print(balanced_paranthesis("(a=2,b={)"))
print(balanced_paranthesis("(a=2,b={})"))
