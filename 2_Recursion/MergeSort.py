"""
Merge Sort Code
Send Feedback
Sort an array A using Merge Sort.
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
2 1 5 2 3
Sample Output 2 :
1 2 2 3 5 
"""

def merge(left, right): # Here I am assuming that the array which we
    pass 				# will receive will be sorted, so two finger algorithm
    pass				# is most likely used
    
    n1, n2 = len(left), len(right)
    
    if n1 == 0:
        return right
    elif n2 == 0:
        return left
    
    i, j, mergearr = 0, 0, []
    
    while i < n1 and j < n2:
        #print("n1 and n2 is", n1, n2, "i and j is", i, j)
        if left[i] <= right[j]:
            mergearr.append(left[i])
            i += 1
        else:
            mergearr.append(right[j])
            j += 1
        #print("mergea")
    
    if i == n1:
        while j < n2:
            mergearr.append(right[j])
            j += 1
    else:
        while i < n1:
            mergearr.append(left[i])
            i += 1
            
    return mergearr 

def mergeSort(arr, start, end):
    # Please add your code here
    # BASE CASE
    if start - end == 0:
        return [arr[start]]
    
    mid = (start + end)//2
    left = mergeSort(arr, start, mid)
    #print("left is", left)
    right = mergeSort(arr, mid + 1, end)
    #print("right is", right)
	
    mergearr = merge(left, right)
    #print("mergearr is", mergearr)
    return mergearr

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
arr = mergeSort(arr, 0, n-1)
print(*arr)
#print(merge([3, 8, 9], [2, 5, 6]))
#print(mergeSort([2, 5, 8, 5, 4, 3, 1, 7], 0, 7))
