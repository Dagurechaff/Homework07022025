print('x y w z')
for x in 0,1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                if ((not(z or (w <= y))) or (x <= z)) == 0:
                    print(x,y,w,z)