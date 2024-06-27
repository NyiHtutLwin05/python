f = open("demotest.txt",'r')

for x in f:
    print(x)

# f = open("demotest.txt",'r')
# print(f.read())


g = open("demotest.txt",'r')
print(g.readline())

h = open("demotest.txt",'r')
print(h.read(5))