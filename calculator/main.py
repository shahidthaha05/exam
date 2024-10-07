from add import *
from sub import *
from mult import *
from div import *
from num import *
from mod import *




while True:
    print('''
    
    1.addition
    2.substraction
    3.multiplication
    4.division
    5.modules
    6.exit
    ''')
    ch=int(input("enter the choice : "))
    if ch==1:
        a,b=num()
        add(a,b)
    elif ch==2:
        a,b=num()
        sub(a,b)
    elif ch==3:
        a,b=num()
        mult(a,b)
    elif ch==4:
        a,b=num()
        div(a,b)
    elif ch==5:
        a,b=num()
        mod(a,b)
    elif ch==6:
        break
    else:
        print('invalid choice')