# var variable is assigned to the input value
# input function allows the user to input any value in the console
# print function will return the value of var
var = input("Please enter a value :")
print("Value is ", var)

# 3a) var in all caps
# upper method used to change the var into all caps characters
print("Value as uppercase is:", var.upper())

# 3b) Count number  of characters in var
# print function to return length of characters of var using len function
print("length of characters in var is", len(var))

# 3C) Use isdecimal to confirm if there is a numerical character in var
# Q: How to return true/false if value is a combination of number and letters?

# var_isdecimal variable checks if there are decimals using isdecimal and boolean response
var_isdecimal = var.isdecimal()
print("Does value contain numerical characters?", var_isdecimal)

# Alternative method of confirming numerical characters in var is using conditional formatting:
if not var_isdecimal:
    print("Does NOT contain numerical characters")
else:
    print("DOES contain numerical characters")

# Alternative method using isdigit and boolean response
var_isdigit = var.isdigit()
print("Does value contain numerical characters?", var_isdigit)

# Part 3: Practice with complex maths
