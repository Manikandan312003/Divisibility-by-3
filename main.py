def divisibleBy3(arr):
    s=0
    for i in arr:
        s=(s%3+i%3)%3
    return int(s==0)

print(divisibleBy3(list(map(int,input().split()))))