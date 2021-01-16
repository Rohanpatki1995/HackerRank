import re

for _ in range(int(input())):
    try:
        pattern = re.compile(input())
        valid = True
    except re.error:
        valid = False
    print(valid)