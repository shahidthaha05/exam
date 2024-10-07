def fact(a):
    s=1
    for i in range(1,a+1):
        s*=i
    print(s)
a=int(input("enter a number : "))
fact(a)