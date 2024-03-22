l=[12,13,34,56,21,79,98,22,35,38]
def alam(l):
    stack=[]
    for i in l[::-1]:
        if i%2==0:
            stack.append(i)
            print(stack.pop(),end=' ')
alam(l)
