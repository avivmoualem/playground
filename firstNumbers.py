print ('The 10 first numbers are: ')


for x in range(10):
     print(x+1, end = " ")

for x in range(5):
    for y in range(x+1):
        print(y+1, end=" ")
    print()
