total = 0
x = 0
y = 1
a = 0
maxval = 4000000



def funct():
    global total
    global x
    global y
    global a
    while x < maxval:
        a = y
        y = x
        x += a
        if x%2 == 0:
            total += x
    print(total)


funct()
