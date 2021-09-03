l1 = [1, 2, 3]
lists = [[]]
for i in range(len(l1) + 1):
    for j in range(i):
        lists.append(l1[j: i]) 
print(lists)
