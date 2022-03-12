def fun(a,b):
    i=0
    while i<20:
        if i%3==0 or i%5==0:
            print(i,",",end="")
        i+=3
fun(3,5)