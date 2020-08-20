import itertools

s,k=input().split()
result=list(itertools.permutations(sorted(s),int(k)))

for item in result:
    print(''.join(item))
