if __name__ == '__main__':
    n, m = map(int, input().split())
    array = input().split()
    like = set(input().split())
    dislike = set(input().split())
    print(sum((i in like) - (i in dislike) for i in array))

