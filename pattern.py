a=65
for i in range(1,5):
    for j in range(i):
        print(chr(a-j),end='')
    print('')
    a+=1