import collections
sale=0
quantity=int(input())   # Number of Shoes available
shoes_available=collections.Counter(map(int,input().split()))
no_of_customers=int(input())    #No of customers

for i in range(no_of_customers):
    shoe_size, cost=map(int,input().split())    # Save the shoe_size_pf_customer and his price as int
    if shoes_available[shoe_size]:
        sale+=cost
        shoes_available[shoe_size]-=1
print(sale)


