def sumdigit():
    S=int(input('Enter Number:'))
    sum=0
    while(S>0):
        rem=S%10
        sum=sum+rem
        S=S//10
    print('Sum of The Digits:',sum)
sumdigit()
