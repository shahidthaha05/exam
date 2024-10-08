# def fact(a):
#     s=1
#     for i in range(1,a+1):
#         s*=i
#     print(s)
# a=int(input("enter a number : "))
# fact(a)


def fun(value):
    fact=1
    for i in range(1,value+1):
        fact=fact*i
    return fact


print(fun(5))
print(fun(6))