print('minmax game')
list = input('enter list of numbers \n')
num = int (input('enter one number \n')) 

arr = list.split(' ')

min = int(arr[0])
max = int(arr[0])
num_exist = int(arr[0]) == num
for k in arr:
    n = int(k)
    if n > max:
        max = n
    if n < min:
        min = n
    if num == n:
        num_exist = True


print('max is: ',max)
print('min is: ',min)
print ('num exist in arr ?', num_exist)
