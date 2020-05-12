import math
def factorit(n):
    mlist=[]
    for x in range(1, math.ceil(n**(1/2))):
        if n%x==0:
            mlist.append(int(x))
            mlist.append(int(n/x))
    return(mlist)

def main(n):
    x=1
    counter=1
    while len(factorit(x)) < n:
        counter+=1
        x += counter
    else:
        print(x)

main(500)