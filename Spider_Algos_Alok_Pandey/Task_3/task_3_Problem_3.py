# Problem 3
# The logic is we have to categorise numbers which share common factors
# So finding no of prime Numbers is sufficient to get no of categories
n = int(input())
prime = 0
if n >= 2:
    for i in range(2, n+1):
        # Numbers have factors other than number itself till its half only
        for j in range(2, (i//2)+1):
            if i % j == 0:
                break
        else:
            prime += 1
    # Summing up numbers starting from 1 corresponding to each category
    print(sum(map(int, range(1, prime+1))))
else:
    raise ValueError("Value of n is out of bound")
