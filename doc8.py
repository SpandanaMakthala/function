def fun():
    string="The quick Brow Fox"
    i=0
    e=0
    b=-3
    while i<len(string):
        if string[i]==" ":
            e=e+1
        else:
            b=b+1
            
        i+=1
    print("UPPERCASE",e)
    print("lowercase",b)
fun()
 