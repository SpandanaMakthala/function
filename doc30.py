def prime():
    num=int(input("enter the num"))
    count=0
    i=1
    while i<=num:
        if num%i==0:
            count+=1
        i+=1
    if count==2:
        print("it is prime")
    else:
        print("no it is not")
prime()

