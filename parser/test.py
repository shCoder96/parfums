(a, b, c, d) = int(input())

if (a % 2 == 0 and c % 2 == 0) or (b % 2 == 0 and d % 2 == 0):
    print('Yes')
elif (a % 2 != 0 and c % 2 != 0) or (b % 2 != 0 and d % 2 != 0):
    print("Yes")
else:
    print('No')
