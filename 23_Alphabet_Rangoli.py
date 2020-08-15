'''
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5
#UL         #UR
--------    e--------
------e-    d-e------
----e-d-    c-d-e----
--e-d-c-    b-c-d-e--

#LL         #LR
e-d-c-b-    a-b-c-d-e
--e-d-c-    b-c-d-e--
----e-d-    c-d-e----
------e-    d-e------
--------    e--------
'''

import string

alphabet=string.ascii_lowercase   #alphabet='abcd......z'
lower_right=[]
lower_left=[]
upper_right=[]
upper_left=[]
lower_list=[]
upper_list=[]
final_list=[]

n=int(input())

for i in range(n):
    lower_right.append('-'.join(alphabet[i:n]))  # ['a-b-c-d-e', 'b-c-d-e', 'c-d-e', 'd-e', 'e']
    lower_left.append(lower_right[i][1:][::-1])  # ['e-d-c-b-', 'e-d-c-', 'e-d-', 'e-', '']
    lower_list.append(lower_left[i])
    lower_list.append(lower_right[i])
upper_right=lower_right[::-1]                    # ['e', 'd-e', 'c-d-e', 'b-c-d-e', 'a-b-c-d-e']
upper_right.pop()                                # ['e', 'd-e', 'c-d-e', 'b-c-d-e']

upper_left=lower_left[::-1]                      # ['', 'e-', 'e-d-', 'e-d-c-', 'e-d-c-b-']
upper_left.pop()                                 # ['', 'e-', 'e-d-', 'e-d-c']

for i in range(n-1):
    upper_list.append(upper_left[i])             # Every even element will be the element from upper_left
    upper_list.append(upper_right[i])            # Every odd element will be the element from upper_right

final_list=upper_list+lower_list

for i in range(0,len(final_list),2):
    print('{}{}'.format(final_list[i].rjust((2*n)-2,'-'), final_list[i+1].ljust((2*n)-1,'-')))