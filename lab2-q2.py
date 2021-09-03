str = input("enter a string")
char = {}
for i in str:
    if i  in char:
        char[i] = char[i]+1
    else:
        char[i] = 1
print(char)