def f(s,p):
    if s<=73 and p==4:
        return True
    if s <= 73 and (p == 2 or p==3):
        return False
    if s > 73 and p == 4:
        return False
    if p%2==1:
        return f(s-2, p+1) or f(s-4, p+1) or f(s//2, p+1)
    else:
        return f(s - 2, p + 1) and f(s - 4, p + 1) and f(s // 2, p + 1)
for s in range(1000,73,-1):
    if f(s,1):
        print(s)