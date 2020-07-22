'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''
if __name__=='__main__':
    command=[]
    return_list=[]
    for i in range(int(input())):
        command=input().split()
        if command[0].lower()=='insert':
            return_list.insert(int(command[1]), int(command[2]))
        elif command[0].lower()=='print':
            print(return_list)
        elif command[0].lower()=='remove':
            return_list.remove(int(command[1]))
        elif command[0].lower()=='append':
            return_list.append(int(command[1]))
        elif command[0].lower()=='sort':
            return_list.sort()
        elif command[0].lower()=='pop':
            return_list.pop()
        elif command[0].lower()=='reverse':
            return_list.reverse()
        else:
            print('Invalid Command')