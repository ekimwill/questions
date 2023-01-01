n,m=map(int, input().split())
area = n*m
if area%2==0:
    print(int(area/2))
elif area%2==1:
    print(int((area-1)/2))

