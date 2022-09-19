"""
Check Palindrome (recursive)
Send Feedback
Check whether a given String S is a palindrome using recursion. Return true or false.
Input Format :
String S
Output Format :
'true' or 'false'
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
racecar
Sample Output 1:
true
Sample Input 2 :
ninja
Sample Output 2:
false
"""

def checkPalindrome(inputstr):
    t = False
    #print(inputstr)
    #print(len(inputstr))
    if len(inputstr) == 1 or len(inputstr) == 0:
        return True
    #print("(1) t is", t)
    #print("OK, inside")
    if inputstr[0] == inputstr[len(inputstr)-1]:
        #print("Insidey, insidey")
        t = checkPalindrome(inputstr[1:-1])
        #print(len(inputstr))
        #print(inputstr)
    #print("(2) t is", t)
    #print("AAAAAHHHHH")
    if not t:
        #print("WTF?")
        t = False
    else:
        return True


inputstr = input()
#t = False
#checkPalindrome(inputstr)
if checkPalindrome(inputstr):
    print("true")
else:
    print("false")