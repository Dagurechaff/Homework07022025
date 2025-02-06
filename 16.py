from sys import setrecursionlimit
setrecursionlimit(10000000)
def F(n):
    if n == 0:
        return 0
    return 3 * n + F(n - 1)

n = 0
while F(n) <= 17505321:
    n += 1
print(n)
