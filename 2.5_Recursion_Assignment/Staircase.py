"""
Staircase
Send Feedback
A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.
Input format :
Integer N
Output Format :
Integer W
Constraints :
1 <= N <= 30
Sample Input 1 :
4
Sample Output 1 :
7
Sample Input 2 :
5
Sample Output 2 :
13
"""

def staircase(n):
    if n == 0:
        return 1
    #print("n is", n)
    
    x = staircase(n-1)
    if n-2 >= 0:
    	y = staircase(n-2)
    else: y = 0
    if n-3 >= 0:
    	z = staircase(n-3)
    else: z = 0
    #print("x , y , z, is", x, y, z)
    
    return x + y + z


n = int(input())
print(staircase(n))