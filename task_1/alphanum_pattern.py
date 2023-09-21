n=5
ch='A'
num=1
for i in range(n):
    for j in range(i+1):
        if i%2!=0:
            print(num,end=' ')
            num+=1
            ch = chr(ord(ch) + 1)
        else:
            print(ch, end=' ')
            ch = chr(ord(ch) + 1)
            num+=1
    print()
