num_list = input('please enter list of numbers comma seperate\n ') 
divider = int(input('please enter divider\n '))
arr = num_list.split(',')

arr2 = []
for i in arr:
   if not int(i) % divider == 0:
      arr2.append(i)
      
print(arr2)
