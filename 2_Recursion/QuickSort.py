"""
Quick Sort Code
Send Feedback
Sort an array A using Quick Sort.
Change in the input array itself. So no need to return or print anything.


Input format :
Line 1 : Integer n i.e. Array size
Line 2 : Array elements (separated by space)
Output format :
Array elements in increasing order (separated by space)
Constraints :
1 <= n <= 10^3
Sample Input 1 :
6 
2 6 8 5 4 3
Sample Output 1 :
2 3 4 5 6 8
Sample Input 2 :
5
1 5 2 7 3
Sample Output 2 :
1 2 3 5 7 
"""

import math as math 

def quickSort(arr, start, end):
    # Please add your code here
    # BASE CASE 
    if start >= end:
        return
    pivotindex = int((start+end)//2)
    #print("start is", start, "end is", end, "pivotindex is", pivotindex)
    #print("arr is", arr)
    fixedindex = partition(arr, start, end, pivotindex)
    #print("arr is", arr)
    #print("fixedindex is", fixedindex)
    quickSort(arr, start, fixedindex-1)
    quickSort(arr, fixedindex+1, end)
    
    #return
    

def partition(arr, start, end, pivotindex):
    si = 0
    ei = end - 1
    lv, hv = -1000000, -1000000
    #print("Before swapping with pivot", arr)
    arr[pivotindex], arr[end] = arr[end], arr[pivotindex]
    
    pivot = arr[end]
    #print(arr)
    #print("pivot is", pivot)
    #print("After swapping", arr)
    
    while si <= ei:
        #print("lv is", lv, "hv is", hv)
        if arr[si] < pivot: 
            lv = -1000000
            si += 1
        else:
            lv = arr[si]
                
        if arr[ei] > pivot: 
            hv = -1000000
            ei -= 1
        else:
            hv = arr[ei]
        #print("lv is", lv, "hv is", hv)
        
        # SWAP
        if lv != -1000000 and hv != -1000000:
            #print("SWAPPING", arr[si], arr[ei])
            arr[si], arr[ei] = hv, lv
            si += 1
            ei -= 1
        
    #print("INSIDE ARRAY IS", arr)
    arr[si], arr[end] = arr[end], arr[si]
    #print("INSIDE ARRAY IS", arr)
    #print(arr)
                
    return si

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)

#n = 6
#arr = [2, 6, 8, 5, 4, 3]

#l = random.randint(0, n-1)
#print(partition(arr, 0, n-1, 2))