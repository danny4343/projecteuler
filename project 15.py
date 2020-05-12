"""

def binary(n):
    if n==2:
        return("10")
    if n==1:
        return("1")
    if n==0:
        return("0")
    big=1
    num=n
    while num/(2**big)>=1:
        big+=1
    big-=1
    snum=""
    snum+=str(1)
    bg=0
    for x in range(2, n-1):
        if (2**x==n):
            bg=x
    if bg!=0:
        for x in range(bg):
            snum+=str(0)
        return(snum)
    num-=2**big
    counter=1
    while num>0:
            if num/(2**(big-counter))>=1:
                snum+=str(1)
                num-=2**(big-counter)
                counter+=1
            else:
                snum+=str(0)
                counter+=1
    while big+1!=counter:
        snum+=str(0)
        counter+=1
    return(snum)

#print(bin(4000000))


def decimal(n):
    length=len(str(n))
    op=0
    for y in range(length):
        op+=(2**(length-y-1))*int(str(n)[y])
    return(op)
#print(decimal(1011))


n=21


y=0
mlist=[]
for x in range(((n-1)*2)):
    y+=10**x
for q in range(decimal(y)+1):
    mlist.append((str(bin(q)))[2:])

for z in range(len(mlist)-1):
    mlist[z]=("00000000000000000000"+mlist[z])
for z in range(len(mlist)-1):
    while len(mlist[z])!=((n-1)*2):
        mlist[z]=mlist[z][1:]


mc=0
destination=n**2
def checker(num):
    global mc
    position=1
    for x in num:
        if int(x)==1:
            position+=1
        else:
            position+=n
    if position==destination:
        mc+=1

for x in mlist:
    checker(x)
print(mc)
"""


va = 0

size = 4

def down(vert,horiz):
    global va
    if (vert != size) & (horiz != size):
        va += 1
        down(vert + 1, horiz)
        down(vert, horiz + 1)


down(0,0)

print(va+1)

"""

size = 2

va = 1

for n in range(size+1):
    va += 2



print(va)


"""



