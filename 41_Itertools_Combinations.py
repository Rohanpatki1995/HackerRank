import itertools

s,k =input().split()
results=[]
for i in range(1,int(k)+1):
    for j in itertools.combinations(sorted(s),i):
        print(''.join(j))