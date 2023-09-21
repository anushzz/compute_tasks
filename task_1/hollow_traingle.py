n=6
for i in range(1,n+1):
    for j in range(1,2*n):
        if (i+j==n+1) or (j-i==n-1) or (i==n and j%2!=0) :
            print('*',end='')
        else:
            print(' ',end='')
    print()
