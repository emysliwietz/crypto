#!/bin/sage

# Python code for Pollard p-1  
# factorization Method 
#https://www.geeksforgeeks.org/pollard-p-1-algorithm/
   
# importing "math" for  
# calculating GCD 
import math 
   
# importing "sympy" for  
# checking prime 
import sympy 
   
      
# function to generate  
# prime factors 
def pollard(n): 
    print("pollard("+str(n)+")")
    # defining base 
    a = 2
   
    # defining exponent 
    i = 27720
   
    # iterate till a prime factor is obtained 
    while(True): 
   
        # recomputing a as required 
        a = (a**i) % n 
   
        # finding gcd of a-1 and n 
        # using math function 
        d = math.gcd((a-1), n)

        print(str(a) + " " + str(d))
   
        # check if factor obtained 
        if (d > 1): 
   
            #return the factor 
            return d 
   
            break
   
        # else increase exponent by one  
        # for next round 
        i += 1
  
# Driver code 
n = 27887
   
# temporarily storing n 
num = n 
   
# list for storing prime factors 
ans = [] 
   
# iterated till all prime factors 
# are obtained 
while(True): 
   
    # function call 
    d = pollard(num) 
    print("pollard = " + str(d))
    # add obtained factor to list 
    ans.append(d) 
   
    # reduce n 
    r = int(num/d) 
   
    # check for prime using sympy 
    if(sympy.isprime(r)): 
   
        # both prime factors obtained 
        ans.append(r) 
   
        break
   
    # reduced n is not prime, so repeat 
    else: 
   
        num = r 
  
# print the result 
print("Prime factors of", n, "are", *ans) 
