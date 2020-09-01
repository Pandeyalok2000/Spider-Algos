# Decomposing binary strings as average of two others
n = int(input())
# only strings of length <10^5
binary_value = int(input(), 2)
# All elements will taken one from last and one from beginning to get all numbers
for i, j in zip(range(1, 2*binary_value), range(1, 2*binary_value)[::-1]):
    value_1 = bin(i)[2:]
    value_2 = bin(j)[2:]
    if len(value_1) == n and len(value_2) == n:
        print(value_1, value_2)
