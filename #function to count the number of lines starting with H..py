def  countH():
        f=open(“filename.txt”,”r”)
        lines=0
        l=f.readlines()
        for i in l:
               if i[0]==’H’:
                     lines+=1
       print(“no of lines are”,lines)
       f.close()
countH()
