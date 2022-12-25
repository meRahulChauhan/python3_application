import os
from sys import argv
fsz=0
if len(argv)==1:
    print("No file selected to be merge")
    print("python3 script.py textfile1 textfile2 outputfilename")
else:
    name=input("Name the output file: ")
    filename=open(name,"w")
    a=range(1,len(argv))
    for x in a:
        file =open(argv[x],'r',encoding='ISO-8859-1')
        f=os.path.getsize(argv[x])
        fs=f/1048576
        fsz=fsz+fs
        print("%s %f MB merged to %s %f %i of %i done" %(argv[x],fs,name,fsz,x,len(argv)-1))
        for y in file:
            filename.write(y)
    print("%f MB Occupied %i file written to %s" %(fsz,len(argv)-1,name))
         
            # print(argv[x]+ " written successfuly to "+name,x,"of",len(argv)-1,"done ")
            #print("%s %f MB merged to %s %f %i of %i done" %(argv[x],fs,name,fsz,x,len(argv)-1))
            #print(len(argv)-1,"file merged to",name)
            #print("%f MB Occupied %i file written to %s" %(fsz,len(argv)-1,name))
''' version 0.1 rom sys import argv
name=input("Name the output file: ")
filename=open(name,"w")
a=range(1,len(argv))
for x in a:
    file =open(argv[x])
    for y in file:
        filename.write(y)
for x in a:
    print(argv[x]+ " written successfuly to "+name,x,"of",len(argv)-1,"done ")
print(len(argv)-1,"file successfully merged to",name)'''
