def reverse2():
    N=int(input('Enter Any Number:'))
    rev=0
    while(N>0):
        rem=N%10
        N=N//10
        rev=(rev*10)+rem
    print('Reverse of The Number:',rev)
reverse2()
