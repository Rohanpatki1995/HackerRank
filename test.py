import itertools

#counter=itertools.cycle([2,3,4])
#print(next(counter))
#print(next(counter))
#print(next(counter))
#print(next(counter))

#squares=map(pow,range(10),itertools.repeat(2))
#print(list(squares))

numbers=[0,1,2,3]
result_combination=itertools.combinations(numbers,4)
result_permutation=itertools.permutations(numbers,4)
result_product=itertools.product(numbers,repeat=4)
result_combination_with_replacement=itertools.combinations_with_replacement(numbers,4)
for item in result_combination_with_replacement:
    print(item)
