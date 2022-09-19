"""
Does s contain t ?
Send Feedback
Given two string s and t, write a function to check if s contains all characters of t (in the same order as they are in string t).
Return true or false.
Do it recursively.
E.g. : s = “abchjsgsuohhdhyrikkknddg” contains all characters of t=”coding” in the same order. So function will return true.
Input Format :
Line 1 : String s
Line 2 : String t
Output Format :
true or false
Sample Input 1 :
abchjsgsuohhdhyrikkknddg
coding
Sample Output 1 :
true
Sample Input 2 :
abcde
aeb
Sample Output 2 :
false
"""

def contains(s,t):
    if len(t) == 1:
        for i in range(len(s)):
            if t == s[i]:
                return True
        return False
    
    for i in range(0, len(s), 1):
        if t[0] == s[i]:
            return contains(s[i+1:], t[1:])
    return False
    #Implement This Function Here
    pass
    
s = input()
t = input()

ans = contains(s,t)
if ans is True:
    print('true')
else:
    print('false')