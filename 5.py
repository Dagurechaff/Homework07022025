for n in range(1,1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '1' + s + '00'
    else:
        c = bin(s.count('1'))[2:]
        s = s + c
    rez = int(s,2)
    if rez > 205:
        print(n)
        break