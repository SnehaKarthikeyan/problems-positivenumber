Coding:

n=int(input())
list1 =list(map(int,input().split()))
num = 0
while(num < len(list1)):
    if list1[num] >= 0:
        print(list1[num], end = " ")
    num += 1
