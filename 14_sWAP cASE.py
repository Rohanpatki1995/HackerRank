'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format

A single line containing a string S.

Constraints

0<=len(S) <=1000
Output Format

Print the modified string S.
'''

#METHOD 1

def swap_case(s):
    swap_case=''
    for letter in s:
        if letter.isupper():
            swap_case+=letter.lower()
        elif letter.islower():
            swap_case+=letter.upper()
        else:
            swap_case+=letter
    return swap_case


if name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

'''
#METHOD 2

def swap_case(s):
	return s.swapcase()
'''

