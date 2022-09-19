"""
Check AB
Send Feedback
Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:
a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'
If all the rules are followed by the given string, return true otherwise return false.
Input format :
String S
Output format :
'true' or 'false'
Constraints :
1 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
abb
Sample Output 1 :
true
Sample Input 2 :
abababa
Sample Output 2 :
false
Explanation for Sample Input 2
In the above example, a is not followed by either "a" or "bb", instead it's followed by "b" which results in false to be returned.
"""

# def checkAB(inputstr):
#     # BASE CASE
#     # If length is 1
#     if len(inputstr) <= 1:
#         # If it is a, return True
#         if inputstr == "a":
#             return True
#         # Else return False
#         else:
#             return False
    
#     # Check For a 
#     if inputstr[0] == "a":
#         # If a is present, check for next, is b 
#         if inputstr[1] == "b":
#             val = checkAB(inputstr[1:])
#         # Or a
#         elif inputstr[1] == "a":
#             val = checkAB(inputstr[1:])
#         # Accordingly call for ahead for recursion
    
#     # Check For b
#     elif inputstr[0] == "b":
#         # Check if length of string >= 3
#         if len(inputstr) >= 3:
#             # If another is also b, then check for consecutive b
#             if inputstr[1] == "b":
#                 # If present check if next is a or b?
#                 # If a, then all is good, continue recursion
#                 if inputstr[2] == "a":
#                 	val = checkAB(inputstr[2:])
#                 # Else, return False, no more b is allowed
#                 else:
#                     return False
#             # If only a single b is present, return false
#             else:
#                 return False
#         # Or <= 2
#         # If length is two or less
#         else:
#             # If next is b, string ends with bb, return True
#             if inputstr[1] == "b":
#                 return True
#             # Else it is, ba or b, then return False
#             else:
#                 return False
            
#     # Return value
#     return val

def checkAB(inputstr):
    if len(inputstr) == 0:
        return True
    if inputstr[0] == "a":
        if len(inputstr[1:]) > 1and inputstr[1:3] == "bb":
            return checkAB(inputstr[3:])
        else:
            return checkAB(inputstr[1:])
    else:
        return False

inputstr = input()
val = checkAB(inputstr)

if val:
    print("true")
else:
    print("false")