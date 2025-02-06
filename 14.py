def c(n):
    k = 0
    while n != 0:
        if n % 25 == 0:
            k += 1
        n //= 25
    return k

n = 25 ** 150 + 25 ** 100
mn_x = 2501
mx = -1
for x in range(1, 2501):
    k = c(n - x)
    if k > mx:
        mn_x = x
        mx = k
print(mn_x)
