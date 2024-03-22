def fact():
    F=int(input('Enter a Number:'))
    f=1
    for i in range(1,F+1):
        f=f*i
    print('Factorial of Given Number:',f)
fact()
