def fun():
    list=[23,42,41,1]
    i=0
    while i<len(list):
        a=int(input("num"))
        if a%2==0:
            print('even',list[i]*100)
        else:
            print('odd',list[i]*-1)
        i+=1
fun()
