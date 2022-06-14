# a = []
# for i in range(9):
#     a.append(input())

# print(max(a))
# print(a.index(max(a))+1)

a = []
max = int(0)
b = 0

for i in range(9):
    a.append(int(input()))

for i in range(len(a)):
    if max <= a[i]:
        max = a[i]
        b = i+1

print(max)
print(b)