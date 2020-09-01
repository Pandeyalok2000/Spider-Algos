# Problem 1
n = int(input())
count = 0
# constraint applying
if (n >= 0) and (n <= 10**100000):
    while len(str(n)) != 1:
        n = sum(map(int, str(n)))
        count += 1
    print(count)
else:
    # raising error for out of bound input
    raise ValueError("Out of Constraint")
