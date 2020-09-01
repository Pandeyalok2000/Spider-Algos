# values in the given range by a value
# for multiple queries
# 1<=n<=100000
n = int(input())
my_list = [i for i in range(n+1) if (n >= 1) and (n <= 100000)]
# 1<=q>=100000
q = int(input())
if (n >= 1) and (n <= 100000):
    for i in range(q):
        L, R, value = list(map(int, input().split()))
        if (L >= 1) and (L <= R) and (R <= n):
            for j in range(L, R + 1):
                # to increment values in the given range
                my_list[j] += value
    print(max(my_list))
