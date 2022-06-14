list = list(map(int, input().split()))
a = int(0)
sum = int(0)
big = 0

for i in range(len(list)):
    for j in range(len(list)):
        if list[i] == list[j]:
            a = a + 1
    if sum < a:
        sum = a
        same = list[i]
    
    if big < list[i]:
        big = list[i]
    a = 0

if sum == 3:
    print(10000 + same*1000)
elif sum == 2:
    print(1000 + same*100)
elif sum == 1:
    print(big*100)