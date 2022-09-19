"""
Split Array
Send Feedback
Given an integer array A of size N, check if the input array can be splitted in two parts such that -
- Sum of both parts is equal
- All elements in the input, which are divisible by 5 should be in same group.
- All elements in the input, which are divisible by 3 (but not divisible by 5) should be in other group.
- Elements which are neither divisible by 5 nor by 3, can be put in any group.
Groups can be made with any set of elements, i.e. elements need not to be continuous. And you need to consider each and every element of input array in some group.
Return true, if array can be split according to the above rules, else return false.
Note : You will get marks only if all the test cases are passed.
Input Format :
Line 1 : Integer N (size of array)
Line 2 : Array A elements (separated by space)
Output Format :
true or false
Constraints :
1 <= N <= 50
Sample Input 1 :
2
1 2
Sample Output 1 :
false
Sample Input 2 :
3
1 4 3
Sample Output 2 :
true
"""

def isSplit(arr, n, i, lsum, rsum):
    #print(lsum, rsum, i)
    if i == n:
        return lsum == rsum
    
    if (arr[i] % 5 == 0):
        lsum += arr[i]
        
    elif arr[i] % 3 == 0:
        rsum += arr[i]
        
    else:
        return (isSplit(arr, n, i+1, lsum + arr[i], rsum) or isSplit(arr, n, i+1, lsum, rsum + arr[i]))
    
    #print("OK", lsum, rsum, i)
    
    return isSplit(arr, n, i+1, lsum, rsum)

def isSplita(arr, n, i, lsum, rsum):
    #print(lsum, rsum)
    if i == n-1:
        return lsum == rsum
    
    if (arr[i] % 5 == 0):
        lsum += arr[i]
        
    elif arr[i] % 3 == 0:
        rsum += arr[i]
        
    else:
        return isSplita(arr, n, i+1, lsum + arr[i], rsum)
    
    return isSplita(arr, n, i+1, lsum, rsum)
                
def isSplitb(arr, n, i, lsum, rsum):
    #print(lsum, rsum)
    if i == n-1:
        return lsum == rsum
    
    if (arr[i] % 5 == 0):
        lsum += arr[i]
        
    elif arr[i] % 3 == 0:
        rsum += arr[i]
        
    else:
        return isSplitb(arr, n, i+1, lsum, rsum + arr[i])
    
    return isSplitb(arr, n, i+1, lsum, rsum)

def splitArray(arr, n):
    #t1 = isSplita(arr, n, 0, 0, 0)
    #t2 = isSplitb(arr, n, 0, 0, 0)
    return isSplit(arr, n, 0, 0, 0)

def split(arr,i,sum):
    #Implement Your Function here
    #arr.sort()
    arr_5div, arr_3div, arr_both = [], [], []
    
    for i in range(len(arr)):
        if arr[i] % 5 == 0:
            arr_5div.append(arr[i])
            
    for i in range(len(arr)):
        if arr[i] % 3 == 0:
            if arr[i] % 5 == 0:
                pass
            else:
            	arr_3div.append(arr[i])
                
    for i in range(len(arr)):
        if arr[i] % 5 != 0 and arr[i] % 3 != 0:
            arr_both.append(arr[i])
            
    if len(arr_both) >= 2:
        arr_both.sort()
        
    #print(arr_5div)
    #print(arr_3div)
    #print(arr_both)
    
    sum_5, sum_3 = 0, 0
    if len(arr_5div) == 0:
        sum_5 = 0
    elif len(arr_5div) == 1:
        sum_5 = arr_5div[0]
    else:
        for i in range(len(arr_5div)):
            sum_5 += arr_5div[i]
        
    #print(arr_3div)
    if len(arr_3div) == 0:
        sum_3 = 0
    elif len(arr_3div) == 1:
        sum_3 = arr_3div[0]
    else:
        for i in range(len(arr_3div)):
            sum_3 += arr_3div[i]
        
    i = 0
    """
    while i < len(arr_both):
        if sum_5 < sum_3:
            arr_5div.append(arr_both[i])
            sum_5 += arr_both[i]
        elif sum_3 < sum_5:
            arr_3div.append(arr_both[i])
            sum_3 += arr_both[i]
        else:
            arr_5div.append(arr_both[i])
            sum_5 += arr_both[i]
        i += 1
	"""
    len_val = len(arr_both)
    while i < len(arr_both):
        #print(arr_5div, arr_3div, i)
        if sum_5 < sum_3:
            arr_5div.append(arr_both[len_val - i - 1])
            sum_5 += arr_both[len_val - i - 1]
        elif sum_3 < sum_5:
            arr_3div.append(arr_both[len_val - i - 1])
            sum_3 += arr_both[len_val - i - 1]
        else:
            arr_5div.append(arr_both[len_val - i - 1])
            sum_5 += arr_both[len_val - i - 1]
        i += 1
        #print(arr_5div, arr_3div, i)

    #print(arr_5div)
    #print(arr_3div)
    #print(arr_both)
        
    if sum_5 == sum_3:
        return True
    else:
        return False
    
n = int(input())
arr = [int(ele) for ele in input().split()]
ans = splitArray(arr,n)
if ans is True:
    print('true')
else:
    print('false')