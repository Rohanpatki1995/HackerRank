def average(n):
    return (sum(set(n))/len(set(n)))

if __name__=='__main__':
    n=int(input())  # No of entries
    height=list(map(int,input().split()))   # Height List
    average_result=average(height)
    print(average_result)
    