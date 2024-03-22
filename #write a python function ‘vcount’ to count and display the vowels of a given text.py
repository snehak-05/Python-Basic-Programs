def vcount():
    n=input('Enter a String:')
    c=0
    print("The Vowels are:")
    for i in n:
        if i in "AEIOUaeiou":
            print(i)
            c=c+1
    print("And There are",c,"Vowels")
vcount()
