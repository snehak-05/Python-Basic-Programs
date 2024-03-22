f=open("file.txt","w")
f.write("hello")
f.close()
f=open("file.txt","r")
s=f.read()
vcount=0
for i in s:
    if i in['a','e','i','o','u','A','E','I','O','U']:
        vcount=vcount+1
print("total no.of vowels in",s,vcount)
f.close()
