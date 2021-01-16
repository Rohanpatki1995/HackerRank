import re

s = input()
pattern = re.split(r'[.,]+', s)

for element in pattern:
    print(element)


'''
regex_pattern = r"[.,]+"
import re
print("\n".join(re.split(regex_pattern,input())))

'''