import string

alphabet=string.ascii_lowercase
lower_right=[]
lower_left=[]
upper_right=[]
upper_left=[]
lower_list=[]
upper_list=[]
final_list=[]

n=int(input())

for i in range(n):
    lower_right.append('-'.join(alphabet[i:n]))
    lower_left.append(lower_right[i][1:][::-1])
    lower_list.append(lower_left[i])
    lower_list.append(lower_right[i])
upper_right=lower_right[::-1]
upper_right.pop()

upper_left=lower_left[::-1]
upper_left.pop()

for i in range(n-1):
    upper_list.append(upper_left[i])
    upper_list.append(upper_right[i])

final_list=upper_list+lower_list

for i in range(0,len(final_list),2):
    print('{}{}'.format(final_list[i].rjust((2*n)-2,'-'), final_list[i+1].ljust((2*n)-1,'-')))