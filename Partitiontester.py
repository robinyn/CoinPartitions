n=200 
coefArr=[1 for i in range(0, n+1)] #
tempArr=[0 for i in range(0, n+1)]
conditionArr=[1,2,5,10,20,50,100,200]
x = 0
m = 2

while m <= n:
    if m in conditionArr:
#        print("m:"+str(m))
        x=0
        while x <= n:
#            print("x:"+str(x))
            y=0
            while x+(m*y) <= n:
#                print("y:"+str(y))
                tempArr[x+(m*y)]+=coefArr[x]
                y+=1
            x+=1
        for i in range(n+1):
            coefArr[i] = tempArr[i]
            tempArr[i] = 0
    m+=1

print(coefArr[n])
