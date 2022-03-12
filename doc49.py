def fun():
	list=[7,1,4,23,95,1203,403,84]
	i=0
	while i<len(list):
		if list[i]%2==0:
			print("even")
		else:
			print("odd")
		i+=1
fun()