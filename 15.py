b = [i for i in range(50, 81)]
for a in range(100):
    f = True
    for x in range(1, 100):
        f = f and (((x in b) <= (x % 7 != 0)) or x + a >= 90)
    if f:
        print(a)

