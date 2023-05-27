for x in range(20,-15,-5):
    print(x, end = " ")
print("/n")

for x in range(20,-15,-5):
    if (x < 0):
        break
    print(x, end = " ")
print("/n")

for x in range(20,-15,-5):
    if(x % 2 != 0):
        continue
    print(x, end = " ")
print("/n")