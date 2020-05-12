counter=1
bigst=0
def main(n):
    global counter
    global bigst
    lc=0
    x=n
    while int(x) > 1:
        if int(x%2)==0:
            lc+=1
            x=x/2
        else:
            lc+=1
            x=(x*3)+1
    else:
        if lc>=counter:
            counter=lc
            bigst=n

for x in range(1000000):
    if x%2 != 0:
        main(x)

print(bigst)


