'''

'''


def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        sub_string=string[i:i+k]
        return_sub_string=''
        for letter in sub_string:
            if letter not in return_sub_string:
                return_sub_string+=letter
        print(return_sub_string)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)