def linearsolver(A,b):
    n = len(A)
    M = A
    i = 0
    for x in M:
        x.append(b[i])
        i+=1
    for j in range(n-1):
        for i in range (n-1) : 
           a=i+j+1
           if a < n:
               q = float(M[a][j]) / M[j][j]       
               for k in range(n+ 1):
                   M[a][k] -=  q * M[j][k]
    print(M)
    x=[0]
    x=x*n
    for i in range(n-1,-1,-1):
        sum=0
        for k in range(n-1,i,-1):
            f=x[k]*M[i][k]
            sum+=f
        v=(M[i][n]-sum)/M[i][i]
        x[i]=v
    print(x)
    return 
q=int(input("how many rows"))
z=[]
for i in range(q):
    b=[]
    a=input("Enter data item in each row separated with space bar")
    a=a.split()
    for i in range (len(a)):
        a[i]=int(a[i])
    z.append(a)   
print(z)
b=input("enter Answers to the equations")
b=b.split()
for i in range(len(b)):
    b[i]=int(b[i]) 
linearsolver(z,b)
print(" This is a simple code by @iPhelther ")
a=int(input("any key to exit"))
print(a)
