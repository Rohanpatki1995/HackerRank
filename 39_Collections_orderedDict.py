import collections

item_list = collections.OrderedDict()

n = int(input())

for _ in range(n):
    item, split_parameter, price = input().rpartition(" ")
    if item_list.get(item):
        item_list[item] = item_list.get(item, 0) + int(price)
    else:
        item_list[item] = int(price)

for k,v in item_list.items():
    print(k,v)
