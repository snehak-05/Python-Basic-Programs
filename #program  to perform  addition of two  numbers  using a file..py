f=open(“num.txt”,”w”)
num1=int(input(“Enter a number:”))
num2=int(input(“Enter a number:”))
sum=num1+num2
f.write(str(num1))
f.write(str(num2))
f.write(str(sum))
f.close
