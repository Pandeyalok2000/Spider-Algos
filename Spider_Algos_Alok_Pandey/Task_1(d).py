# values are [ No of days , initial rating, rating increase, rating decrease
n, r, x, y = list(map(int, input().split()))
initial_value = r
# contest happens or not
c = list(str(input()))
# SCN eaten or not
s = list(str(input()))
for i, j in zip(c, s):
    if i == "1" and j == "1":
        r =  r + x
    elif i == "0" and j == "0":
        r = r - y
if initial_value > r:
    print("demoted")
elif initial_value < r:
    print("promoted")
elif initial_value == r:
    print("no change")
