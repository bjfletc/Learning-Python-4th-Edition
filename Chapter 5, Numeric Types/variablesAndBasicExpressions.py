'''
First of all, let’s exercise some basic math. In the following interaction, we first assign
two variables (a and b) to integers so we can use them later in a larger expression.
Variables are simply names—created by you or Python—that are used to keep track of
information in your program. We’ll say more about this in the next chapter, but in
Python:
• Variables are created when they are first assigned values.
• Variables are replaced with their values when used in expressions.
• Variables must be assigned before they can be used in expressions.
• Variables refer to objects and are never declared ahead of time.
In other words, these assignments cause the variables a and b to spring into existence
automatically:
'''

a = 3                   # Name created
b = 4

print(str(a) + " & " + str(b) + "\n")   # a = 3 & b = 4

a + 1, a - 1            # Addition (3 + 1), subtraction (3 - 1)

print("\n" + str(a) + "\n")

b * 3, b / 2            # Multiplication (4 * 3), division (4 / 2)

print("\n" + str(b))

a % 2, b ** 2           # Modulus (remainder), power (4 ** 2)

print("\n a: " + str(a) + " b: " + str(b) + "\n")
