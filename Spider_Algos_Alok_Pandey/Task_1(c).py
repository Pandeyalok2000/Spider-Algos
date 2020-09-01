# elements are 10, 7, 43, 9, 8, 16
real_list = list(map(int, input().split()))     # real ordered list
random_list = [10, 7, 43, 9, 8, 16]
guessed_list = ["?", "?", "?", "?", "?", "?"]
# queries to guess
print("Enter whatever digit written before COLON ':' these are value of x and y")
#Adit has asked x= 1, y = 3
x, y = int(input("1 : ")), int(input("3 : "))
a = real_list[x]*real_list[y]
for j in random_list:
    for k in random_list:
        if j*k == a:
            guessed_list[x] = (j, k)
            guessed_list[y] = (j, k)
print(guessed_list)
# here x =1, y =5
x, y = int(input("1 : ")), int(input("5 : "))
b = real_list[x]*real_list[y]
for j in (guessed_list[1]):
    for k in random_list:
        if j*k == b:
            guessed_list[1] = j
            guessed_list[3] = real_list[3]
            guessed_list[5] = k
            print(guessed_list)
# here x = 4, y = 5=
x, y = int(input("4 : ")), int(input("5 : "))
c = real_list[x]*real_list[y]
for i in random_list:
    if i*guessed_list[5] == c:
        guessed_list[4] = i
        print(guessed_list)
# here x = 0, y = 1
x, y = int(input("0 : ")), int(input("1 : "))
c = real_list[x]*real_list[y]
for i in random_list:
    if i*guessed_list[1] == c:
        guessed_list[0] = i
        print(guessed_list)
guessed_list[2] = real_list[2]
print("Congrats you got it!")
print(guessed_list)
