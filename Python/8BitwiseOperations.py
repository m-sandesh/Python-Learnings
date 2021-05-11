# # Bitwise operations
# # All calculations are performed in BIT so output varies drastically.

# Complement
#     Applies 1's and 2's Compliment for the output. Uses '~' symbol.
print(~12)
#     Output is -13 due to compliments calculation in bit format

# AND:
#     Applies AND truth table for output. Uses '&' for bit operations.
print(12 & 13)
#     Output is 12 due to truth table calculation in bit format.

# OR:
#     Applies OR truth table for output. Uses '|' for bit operations.
print(12 | 13)
#     Output is 13 due to truth table calculation in bit format

# XOR:
#     Applies XOR truth table for output. Uses '^' symbol.
print(12 ^ 13)

# Left Shift:
#     Shifts bits after decimal(.) to the left of decimal. Uses symbol <<.
print(12 << 2)
#     Example:    00001100.00
#                 0000110000.00 (after left shift)

# Right Shift:
#     Shifts bits before decimal(.) to the right of decimal. Uses symbol >>.
print(12 >> 2)
#     Similar example to left shift.