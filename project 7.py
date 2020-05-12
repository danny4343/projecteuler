mlist=[2,3,5,7,11]
def main(num):
    x=13
    count=5
    while count<num:
        for y in mlist:
            if x % y == 0:
                break
            if y == mlist[len(mlist)-1] and x % y != 0:
                mlist.append(x)
                count+=1
        x+=2
    else:
        print(x-2)

main(10001)