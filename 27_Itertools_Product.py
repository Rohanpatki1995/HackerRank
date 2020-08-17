from itertools import product

a= list(map(int,input().split()))
b= list(map(int,input().split()))

#print(a)
#print(b)

print(*product(a,b))
