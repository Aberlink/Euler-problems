import itertools

arguments = range(10, 0, -1)
a = list(itertools.permutations(arguments))

for i in range(0, len(a)):
    if a[i][0] > 7:
        continue
    x1 = a[i][0] + a[i][1] + a[i][2]
    x2 = a[i][3] + a[i][2] + a[i][4]
    x3 = a[i][5] + a[i][4] + a[i][6]
    x4 = a[i][7] + a[i][6] + a[i][8]
    x5 = a[i][9] + a[i][8] + a[i][1]

    if x1 == x2 == x3 == x4 == x5:
        if a[i][0] < a[i][3] and a[i][0] < a[i][5] and a[i][0] < a[i][7] and a[i][0] < a[i][9]:
            print(a[i])
            t1 = str(a[i][0]) + str(a[i][1]) + str(a[i][2]) + str(a[i][3]) + str(a[i][2]) + str(a[i][4]) + str(a[i][5])
            t2 = str(a[i][4]) + str(a[i][6]) + str(a[i][7]) + str(a[i][6])
            t3 = str(a[i][8]) + str(a[i][9]) + str(a[i][8]) + str(a[i][1])
            result = t1 + t2 + t3
            print(result)
            break
