j = 0

for i in list(xrange(10)):
    for n in list(xrange(10)):
        print n, i, j
        if n==i:
            print("break")
            next
        j+=1

