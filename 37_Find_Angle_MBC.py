if __name__ == '__main__':
    import math
    ab = int(input())
    bc = int(input())

    ac = math.hypot(ab,bc)

    mbc = round(math.degrees(math.atan(ab/bc)))
    deg = '°'

    print(mbc,deg, sep='')
