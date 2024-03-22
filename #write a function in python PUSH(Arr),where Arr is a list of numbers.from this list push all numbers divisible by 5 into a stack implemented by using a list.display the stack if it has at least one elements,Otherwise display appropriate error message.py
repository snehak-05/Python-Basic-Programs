Arr=[1,20,45,30,4,37,35]
def PUSH(Arr):
    stack=[]
    for i in Arr:
        if i%5==0:
            stack.append(i)
    print(stack)
    if stack==[]:
        print('ERROR...stack is empty')
PUSH(Arr)
