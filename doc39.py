def fun():
    a=[4,6,2,1,9,63,-134,566]
    b=[-52, 56, 30, 29, -54, 0, -110]
    i=0
    max=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i+=1
    j=0
    min=b[j]
    while j<len(b):
        if a[j]<min:
            min=b[j]
        j+=1
    print(max)
    print(min)
fun()

