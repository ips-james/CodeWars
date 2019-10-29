# Write a function called that takes a string of parentheses, and determines if the order of the parentheses is
# valid. The function should return true if the string is valid, and false if it's invalid.
#
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true


def valid_parentheses(string):
    left = 0
    right = 0
    for i in range(len(string)):
        if string[i] == "(":
            left += 1
        elif string[i] == ")":
            right += 1
        if right > left:
            return False
    if left == right:
        return True
    else:
        return False


# No need to have 2 variables, one for right and one for left.
# Could instead just have one variable and check to see whether it goes negative.

print(valid_parentheses("  ("))
print(valid_parentheses("hi(hi)()"))
