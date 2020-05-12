def main():
    a=1
    b=1
    while a+b+(((a**2)+(b**2))**(1/2))!=1000:
        if a<999:
            a+=1
        else:
            a=1
            b+=1
    else:
        print(a*b*(((a**2)+(b**2))**(1/2)))

main()