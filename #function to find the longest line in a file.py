def  file_long(filename):
        longest=” “
        for  line in open(filename):
                    if len(line)>len(longest):
                                longest=line
         print(“longest line’s length “,len(longest))
         print(longest)
file_long(filename)
