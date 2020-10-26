#!/bin/sage
# Python 3 implementation of Dixon factorization algo
# https://www.geeksforgeeks.org/dixons-factorization-method-with-implementation/

from math import sqrt, gcd 
import numpy as np
import sympy 

# Function to find the factors of a number 
# using the Dixon Factorization Algorithm 
def factor(n): 

        # Factor base for the given number 
        base = [22] 

        # Starting from the ceil of the root 
        # of the given number N 
        start = int(sqrt(n)) 

        # Storing the related squares 
        pairs = [] 

        # For every number from the square root 
        # Till N 
        for i in range(start, n): 

                # Finding the related squares 
                for j in range(len(base)): 
                        lhs = i**2 % n 
                        rhs = base[j]**2 % n 
                        
                        # If the two numbers are the 
                        # related squares, then append 
                        # them to the array 
                        if(lhs == rhs):
                                pairs.append([i, base[j]])
                                print("i: " + str(i))

        new = [] 

        # For every pair in the array, compute the 
        # GCD such that 
        for i in range(len(pairs)): 
                factor = gcd(pairs[i][0] - pairs[i][1], n)
                print("f: " + str(factor))
                # If we find a factor other than 1, then 
                # appending it to the final factor array 
                if(factor != 1): 
                        new.append(factor)
                        
        x = np.array(new) 

        # Returning the unique factors in the array 
        return(np.unique(x))

# Driver Code 
if __name__ == "__main__":
        print(factor(403)) 
