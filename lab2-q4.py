str = input("enter a string")
char = {}
for i in str:
    if i  in char:
        char[i] = char[i]+1
    else:
        char[i] = 1

for key in char:
    if char[key] > 1:
        print(key,char[key])