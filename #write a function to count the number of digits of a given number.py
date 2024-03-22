def countdigit():
    C=int(input('Enter Number to Count Digit:'))
    count=0
    while(C>0):
        rem=C%10
        count=count+1
        C=C//10
    print('Number of Digits:',count)
countdigit()
