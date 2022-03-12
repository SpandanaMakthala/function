def fizz_buzz():
    a=int(input('enter the num'))
    if a % 3 == 0 and a % 5 == 0:
        print('FizzBuzz')
    if a % 3 == 0:
        print('Fizz')
    if a % 5 == 0:
        print('Buzz')
    else:
    	print('nothing')
fizz_buzz( )
