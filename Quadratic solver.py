from decimal import Decimal, getcontext

getcontext().prec = 10000000  # Set decimal precision

import time
start_time = time.time()
timeout=30
equation = "ax^2+bx+c"
print("this is the standard equation: ",equation)
a= Decimal(input("please enter the 'a' in your equation: "))
b= Decimal(input("please enter the 'b' in your equation: "))
c= Decimal(input("please enter the 'c' in your equation: "))
#using factor method
count=0


newc= a*c #simplifies process later on
if newc>0: #made a finishing point to make the code have a smaller range of no. to go through
    limit=newc+1
elif newc==0 and a>0:
    limit = a + 1
elif newc==0 and a<0:
    limit = a*-1 + 1
else:
    limit=newc*-1 +1 # forcing the limit variable to always be a pos number
if newc>0:
    basfac1=newc*-1 -1  #made a starting point for the 1st factor to default to b4 iterating
else:
    basfac1=newc-1  


stop=((limit*2)+1)*basfac1                  #making a stopping point if no factors possible


fac1=basfac1
if limit>0:             #defining starting position for 2nd factor
    fac2=limit*-1
else:
    fac2=(limit -1)*-1 -1
while True:
    if a==0:
        print("the factor is", (-c)/b)
        break
    #if time.time()-start_time > timeout:              #temporary fix to make a stopping point
        print("there is no possible solution with whole numbers in 30s. Please try again.")
        break
    count=count+1
    if a==1 and c==0 and b<0:
        b=b*-1
        newb=b
    
    fac1=fac1+Decimal('0.0000001')  #set decimal precision 
    #iterate fac1 always unless further statements are fulfilled
    #print(limit,basfac1,fac1,fac2)
    if fac1>limit and fac1+fac2!=b: #stops the code from going needlessly infinitely
        fac2=fac2+Decimal('0.0000001')   #set decimal precison
        fac1=basfac1
    if count==stop and fac1*fac2!=newc and fac1+fac2!=b:
        print("there is no possible solution with whole numbers. Please try again.")
        #print(count)
        break
    
    if fac1==limit:
        print("There are no possible values for this equation")
        break       
    
    
    
    if fac1*fac2==newc and fac1+fac2==b:
        if a==1:
            fac1=fac1*-1
            fac2=fac2*-1
        if a>1 and c!=0:
            fac1= (fac1/a)*-1
            fac2= (fac2/a)*-1
        if a>1 and c==0:
            fac1= (fac1/a)*-1
            fac2= (fac2/a)*-1
        if a<1 and c!=0:
            fac1= (fac1*a)*-1
            fac2= (fac2*a)*-1
        if a<1 and c==0:
            fac1= (fac1/a)*-1
            fac2= (fac2/a)*-1
        if a==1 and c==0:
            fac1= fac1
            fac2=fac2





        print("the roots of the equation is x=",fac1,"x=",fac2)
        break
    ## make the a term be other values than 1 and -1 COMPLETE
    ##need to make a count that goes up to max combo of fac1 and fac 2. stopping point  COMPLETE
    ##need to make a decimal thing working COMPLETE