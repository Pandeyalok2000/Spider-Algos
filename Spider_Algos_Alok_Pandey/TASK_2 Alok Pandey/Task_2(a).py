# longest prefix.
T = int(input())
my_results = []
if (T >= 1) and (T <= 500):
    for j in range(T):
        string = input()
        i_sum = 0
        maximum = 0
        # Traversing the string.
        for i in range(len(string)):
            if len(string) <= 1000000:
                # If open "<" add 1 to sum.
                if string[i] == '<':
                    i_sum += 1
                # If closed  subtract 1
                # from sum
                else:
                    i_sum -= 1
                # if first symbol is closing ">"
                # then this condition would help
                if i_sum < 0:
                    break
                # If sum is 0, store the
                # index value.
                if i_sum == 0:
                    maximum = i + 1
        my_results.append(maximum)
    for result in my_results:
        print(result)
