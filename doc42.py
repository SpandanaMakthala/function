def fun():
    list=[15,81,11,234]
    i=0
    a=[]
    while i<len(list):
        j=list[i]
        sum=0
        while j>0:
            c=j%10
            sum=sum+c
            j=j//10
        a.append(sum)
        i+=1
    print(a)
fun()