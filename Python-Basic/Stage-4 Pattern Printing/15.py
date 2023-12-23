#     1
#    121
#   12321
#  1234321
# 123454321
#  1234321
#   12321
#    121
#     1

rows = 5  # We can change the number of rows as needed
# Print the first half
for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print increasing numbers
    for k in range(1, i + 1):
        print(k, end="")
    # Print decreasing numbers
    for l in range(i - 1, 0, -1):
        print(l, end="")
    print()

# Print the second half
for i in range(rows - 1, 0, -1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print increasing numbers
    for k in range(1, i + 1):
        print(k, end="")
    # Print decreasing numbers
    for l in range(i - 1, 0, -1):
        print(l, end="")
    print()
