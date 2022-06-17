a = int(input())
b = int(input())
c = int(input())

x = a * b * c

list = list(str(x))
z = []
for i in range(10):
    z.append(0)

for i in range(len(list)):
    for j in range(10):
        if int(list[i]) == j:
            z[j] = z[j] + 1

for i in range(10):
    print(z[i])

# for i in range(len(list)):
#     for j in range(10):
#         print(j)