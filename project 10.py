mlist=[2,3,5,7,11]
fv=28
def main(num):
    global fv
    x=13
    while x < num:
        for y in mlist:
            if y>(x**(1/2)):
                mlist.append(x)
                fv += x
                break
            if x % y == 0:
                break
            if y == mlist[len(mlist) - 1] and x % y != 0:
                mlist.append(x)
                fv += x
        x+=2


main(2000000)

print(fv)

