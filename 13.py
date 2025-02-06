from ipaddress import *
ip = '111.194.0.0'
mask = '255.254.0.0'
net = ip_network(ip + '/' + mask, 0)
c = 0
for i in net.hosts():
    x = ('0' * (32 - len(bin(int(i))[2:]))) + bin(int(i))[2:]
    print(x)
    if (x.count('1') - x.count('0')) % 2 == 0:
        c += 1
print(c)
