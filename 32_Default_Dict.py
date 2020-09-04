import _collections

n,m=map(int,input().split())
list_a=_collections.defaultdict(list)
list_b=[]

for i in range(n):
    list_a[input()].append(i+1)

for i in range(m):
    list_b.append(input())

for item in list_b:
    if item in list_a:
        print(' '.join(map(str,list_a[item])))
    else:
        print('-1')


