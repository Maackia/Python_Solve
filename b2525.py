x, y = input().split()
z = input()

x = int(x)
y = int(y)
z = int(z)

if y + z >= 60:
    x = int(x + ((y + z) / 60))
    y = (y + z) % 60
else:
    y = y + z
    
if x >= 24:
    x = x - 24

print(x, y)