def twopower(n):
    ans=1
    cd=0
    while cd<n:
        ans*=2
        cd+=1
    return(ans)

def digitsum(n):
    st=str(n)
    ans=0
    for x in st:
        ans+=int(x)
    print(ans)


def main(n):
    digitsum(twopower(n))

main(1000)