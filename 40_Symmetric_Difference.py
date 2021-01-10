m = int(input())

set_m = set(map(int, input().split()))

n = int(input())

set_n = set(map(int, input().split()))

diff_set = set_m.symmetric_difference(set_n)

print(*sorted(diff_set, key=int), sep='\n')
