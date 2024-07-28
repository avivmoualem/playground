num = int(input('please enter a number  '))
print(num)

sum = 0

for i in range(num + 1):
    print('current sum: ', sum)
    sum = sum + i

print('the sum is',sum)
