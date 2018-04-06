l = [4, 3, 0, 2, 1]

i = 0

while l[i] != 0:
    i = l[i]
    print(i)

lst = []
for i in range(1, 20, 2):
    lst.append(i)
print(lst)

l = [x*2+1 for x in range(0,10)]