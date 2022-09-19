"""
Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
Note : For this question, you can assume that 0 raised to the power of 0 is 1


Input format :
Two integers x and n (separated by space)
Output Format :
x^n (i.e. x raise to the power n)
Constraints:
0 <= x <= 8 
0 <= n <= 9
Sample Input 1 :
 3 4
Sample Output 1 :
81
Sample Input 2 :
 2 5
Sample Output 2 :
32
"""

val = list(map(float, input().rstrip().split()))
    
x, n = val[0], val[1]

def xPowern(p, q):
    if p == 0:
        if q == 0:
            return 1
        else:
            return 0
    else:
        if q == 0:
            return 1
        else:
            p = p * xPowern(p, q-1)
            #print(x)
            return p

print(int(xPowern(x, n)))