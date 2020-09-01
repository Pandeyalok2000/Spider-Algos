# Problem 2
# the logic is to find number in order
# Here I have used Dynamic Programming by using subset sum method


def is_sum(bricks, n, target_sum):
    # base cases
    if target_sum == 0:
        return True
    if n == 0:
        return False
    # recursion
    if bricks[n - 1] > target_sum:
        return is_sum(bricks, n - 1, target_sum)
    return is_sum(bricks, n - 1, target_sum) or (is_sum(bricks, n - 1, target_sum - bricks[n - 1]))


# Initialising variable
N = int(input())
M = int(input())
# Checking for constraint
if N in range(1, 3) and (M >= 1) and M <= 100000:
    brick_strength = list(map(int, input().split()))
    # Checking for constraint
    if len(brick_strength) == M and max(brick_strength) in range(1, 10**9):
        total_sum_average = sum(map(int, brick_strength))//N
        for i in range(total_sum_average, 0, -1):
            if is_sum(brick_strength, M, i):
                print(i)
                break
    else:
        # raising ValueError
        raise ValueError("Value is Out of Constraints")
else:
    # raising ValueError
    raise ValueError("Input Values are out of bound")
