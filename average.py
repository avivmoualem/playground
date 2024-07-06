print ('The average')
runloop = True
sum = 0
counter =0
while(runloop):
    inp = input()
    if inp == 'q':
        runloop = False
    else:
        num = int(inp)
        counter= counter+1
        sum = sum + num
print('Average: ' , (sum/counter))
