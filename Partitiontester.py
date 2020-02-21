n=200 
coefArr=[1 for i in range(0, n+1)] # This is where the coefficients of the polynomial will be stored 
tempArr=[0 for i in range(0, n+1)] # This is a buffer for the coefficients while I multiply them out, since the coef. can't change during the multiplication steps
conditionArr=[1,2,5,10,20,50,100,200]
x = 0 # This represents the xth term of the first polynomial (x^0 + x^1 + x^2 +.... + x^n)
m = 2 # This is the multiplier to move across the terms in the polynomial I am multiplying to the first polynomial (x^m0 + x^m1 + x^m2 +...+ x^mi where mi=n)

while m <= n:
    if m in conditionArr:
        x = 0
        while x <= n:
#            print("x:"+str(x))
            y=0 # This is the same thing as i in the comment above 
            while x+(m*y) <= n:
#                print("y:"+str(y))
                tempArr[x+(m*y)]+=coefArr[x] # Here is where the actual 'multiplication' of the polynomials happen
                y+=1
            x+=1
        for i in range(n+1):
            coefArr[i] = tempArr[i] # Here I just move the calculated coefficients into the actual storage array and resetting the buffer
            tempArr[i] = 0
    m+=1

print(coefArr[n]) # This prints the coefficient of the nth term, which is the answer
