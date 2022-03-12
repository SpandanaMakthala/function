def fun():
    list1 = [2, -7, 5, -64, -14]
    i=0
    count=0
    count1=0
    while i<len(list1):
        if list1[i]>0:
            count+=1
        else:
            count1+=1
        i+=1
		    
    print('positive',count)
    print('negative',count1)
fun()
