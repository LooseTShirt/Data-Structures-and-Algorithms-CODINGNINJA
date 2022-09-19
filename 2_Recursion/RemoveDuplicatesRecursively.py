"""
Remove Duplicates Recursively
Send Feedback
Given a string S, remove consecutive duplicates from it recursively.
Input Format :
String S
Output Format :
Output string
Constraints :
1 <= |S| <= 10^3
where |S| represents the length of string
Sample Input 1 :
aabccba
Sample Output 1 :
abcba
Sample Input 2 :
xxxyyyzwwzzz
Sample Output 2 :
xyzwz
"""

# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    # Please add your code here
    if len(string) == 1:
        return string
    elif string[0] == string[1]:
        return removeConsecutiveDuplicates(string[1:])
    else:
        return string[0] + removeConsecutiveDuplicates(string[1:])

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))