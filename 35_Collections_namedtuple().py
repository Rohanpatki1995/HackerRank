import collections

n = int(input())

fields = input().split()

Students = collections.namedtuple('Students', fields)
total = 0
for _ in range(n):
    student=Students(*input().split())
    total +=int(student.MARKS)

print(total/n)