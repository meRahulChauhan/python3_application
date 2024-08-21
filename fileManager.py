import os
import time
class fileManager:
    path=os.getcwd()
    def __init__(self):
        pass
    def makedir(self,dirname):
        self.dirname=dirname
        if not os.path.isdir(dirname):
            os.mkdir(dirname)
            print("\tDirectory '%s' create sucessfully"%self.dirname)
        else:
            print("\tDirectory '%s' already exist..."%(self.dirname))

    def deldirectory(self,deldir):

         self.deldir=deldir
         if not os.path.isdir(self.deldir):
             print("\tdirectory '%s' doesn't exist"%self.deldir)
         elif os.path.isdir(self.deldir):
             datasize=os.path.getsize(self.deldir)
             if datasize <4097:
                 print("\t'%s' is an empty directory"%self.deldir)
                 os.rmdir(self.deldir)
                 print("\tdirectory '%s' successfully deleted..."%self.deldir)
             elif  os.path.isdir(self.deldir)>4096:
                 print("\tNot a empty directory,can't delete, you may loose data  ")
                 print("\tcontains '%s Bytes' Data"%datasize)
    def createfile(self,filename):
        self.filename=filename
        if not os.path.isfile(self.filename):
            fileObj=open(self.filename,"w")
            print("\tfile '%s' created successfully "%self.filename)
        else :
            print("\tfile '%s' Already exist"%self.filename)
    def delfile(self,filename):
        self.filename=filename
        if not os.path.isfile(self.filename):
           print("\tfile '%s' not exist "%self.filename)
        else :
            os.remove(self.filename)
            print("\tfile '%s' deleted successfully"%self.filename)

    def readfile(self,filename):
        self.filename=filename
        if not os.path.isfile(self.filename):
           print("\tfile '%s' not exist "%self.filename)
        else:
            fileObj=open(self.filename,"r")
            dataread=fileObj.read()
            word=dataread.split()
            if len(word)>0:
                print(dataread)
            else :
                print("***emptyfile***")

    def updatefile(self,filename):
        self.filename=filename
        if not os.path.isfile(self.filename):
           print("\tfile '%s' not exist "%self.filename)
        else :
            fileObj=open(self.filename,"a")
            insert=input("Append file: ")
            insert="\n"+insert
            fileObj.write(insert)
            fileObj.close
            print("\t%s \nwritten successfully "%insert)
    def getsizeOf(self,name):

        self.name=name
        if os.path.isdir(self.name):
            filesize=os.path.getsize(self.name)
            print("\tType 'dir' & '%s' contains '%s' Bytes"%(self.name,filesize))
        elif os.path.isfile(self.name):
            filesize=os.path.getsize(self.name)
            print("\tType 'file' & '%s' contains '%s' Bytes"%(self.name,filesize))
        else:
            print("\tNo file/directory exist with '%s' name" %self.name)

def disk_usage(path):
    total=os.path.getsize(path)
    if os.path.isdir(path):
        for filesys in os.listdir(path):
            childpath=os.path.join(path,filesys)
            total+=disk_usage(childpath)
    print('{0:7}'.format(total),path)
    return total
OBJ=fileManager()
while True:
    print("______________________________________________________________")
    print("select option without hyphen \n md --make directory \n dd --delete directory \n cf --create file \n rf --read file \n uf --update file \n df --delete file \n size --getsizeOf \n ls --list all \n q --quit application")
    opt=input("Your selection:  ").lower().strip()

    if opt=="md":
        filename=input("Enter dir name to create: ")
        OBJ.makedir(filename)

    elif opt=="dd":
        filename=input("Enter dir name to delete: ")
        OBJ.deldirectory(filename)

    elif opt=="cf":
        filename=input("Enter filename to create: ")
        OBJ.createfile(filename)

    elif opt=="rf":
        filename=input("Enter filename to read data: ")
        OBJ.readfile(filename)

    elif opt=="uf":
        filename=input("Enter filename to update: ")
        OBJ.updatefile(filename)

    elif opt=="df":
        filename=input("Enter filename to delete: ")
        OBJ.delfile(filename)

    elif opt=="size":
        filename=input("Enter file/fir name to get size: ")
        OBJ.getsizeOf(filename)

    elif opt=="ls":
        filename=os.getcwd()
        print(filename)
        disk_usage(filename)
    elif opt=="q":
        print("Exiting...")
        time.sleep(0.5)
        print("Thanks for using...")
        break
    else:
        print("choose a valid option: ")
"""
NAME :"RAHUL CHAUHAN";
EMAIL :"RC5565931@GMAIL.COM";
"""
