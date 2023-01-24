import os
import shutil
import subprocess
from PIL import Image, ImageOps
import PIL
import time 
def rgb_to_gray():
   dir="img_black"
   img_set=set()
   if os.path.isfile("img_list.txt")==False:
      print("Notice: since no file selected, select at least one file")
      print('.'*60)
      validate_img()
   img_file=open("img_list.txt","r")
   for y in img_file:
      if y not in img_set:
         img_set.add(y)
         y=y[0:len(y)-1]
         print(y)

         img_rgb = Image.open(y)
         #img_rgb.show() #show image in true color
         img_gray=ImageOps.grayscale(img_rgb)
         #img_gray.show() #show grayscale image
         dir_path=dir+'/'+y
         #print(dir_path)
         #bw=img_gray.save("Music/ls.jpg")
         if os.path.isdir(dir)==False:
            if os.mkdir(dir):
               pass
         if os.path.isdir(dir)==True:
               #print(dir,"Directory created") #since not working  script not refresh
             bw=img_gray.save(dir_path)
             #print("dir created and saved")
         else:
            bw=img_gray.save(dir_path)
            print("File saved '"+dir_path+"'")
         fs=open("img_set.txt","a")
         fs.write(dir_path+"\n")
         fs.close()

def validate_img():
   path=input("Enter filename: ")
   img_list=set()
   if os.path.exists(path)==False:
       if len(path)>0:
          print("Notice: '"+path+"'"+" not exists! probably deleted?")
          menu()
       else:
           print("Null entry")
           menu()
   elif os.path.isdir(path):
       print("Notice: '"+path+"'"+"is a directory,Can't be used.")
       menu()
   else:
      if path.endswith(".jpg",-4,len(path)):
         img_list.add(path)
      elif path.endswith(".jpeg",-5,len(path)):
         img_list.add(path)
      elif path.endswith(".png",-4,len(path)):
         img_list.add(path)
      else :
         print("Notice: '"+path+"'"+" probably not a image file")
         validate_img()
      fs=open("img_list.txt","a")
      for x in img_list:
         fs.write(x+"\n")
        
def diskfile():
   img_list=set()
   path=os.getcwd()
   if os.path.exists(path)==False:
      print("path not exists")
      menu()
   if os.path.isfile(path):
      print("Enter directory not file")
      menu() 
   if os.path.isdir(path):
      for fs in os.listdir(path):
         childpath=os.path.join(fs)
         if childpath.endswith(".jpg",-4,len(childpath)):
            img_list.add(childpath)
         elif childpath.endswith(".jpeg",-5,len(childpath)):
            img_list.add(childpath)
         elif childpath.endswith(".png",-4,len(childpath)):
            img_list.add(childpath)
         else :
            print("Notice: '"+childpath+"'"+" probably not a image file")
         
      fs=open("img_list.txt","a")
      for x in img_list:
         fs.write(x+"\n") 
                     

    
def img_to_txt():
   if os.path.isfile("img_set.txt")==False:
      rgb_to_gray()
   fs=open("img_set.txt","r")
   for x in fs:
      x=x[0:len(x)-1] #-1 to fix ,word shift to last in down
      #print(x)
      cmd="tesseract "+x+" wordlist"
      subprocess.run([cmd, "-l"],shell=True)
      if os.path.isfile("wordlist.txt"):
         with open("wordlist.txt","r") as wl, open("paragraph.txt","a") as pr:
            for line in wl:
               if line.strip():
                  pr.write(line)
      else:
         print("Couldn't extracted data from image")
      '''base='wordlist.txt'
      copy_to="paragraph.txt"
      shutil.copyfile(base,copy_to)'''

def sanitize_words():
   if os.path.isfile("paragraph.txt")==False:
      img_to_txt()
   fs=open("paragraph.txt","r")
   filename=input("Enter filename to store words: ")
   if len(filename)<=0:
      print("Filename couldn't be null")
      sanitize_words()
   fs1=open(filename,"w")
   sanitize_wordset=set()
   with open("paragraph.txt","r") as datafile:
      for word in datafile:
         data=set(word.split(" "))
         #print(data)
         for ws in data:
            ws=''.join(char for char in ws if char.isalpha())
            if len(ws)>3:
               if ws not in sanitize_wordset:
                  sanitize_wordset.add(ws)
                  fs1.write(ws.title()+"\n")
   remover()               
def remover():
   if os.path.exists("wordlist.txt"):
      os.remove("wordlist.txt") 
   if os.path.exists("img_list.txt"):
      os.remove("img_list.txt")
   if os.path.exists("img_set.txt"):
      os.remove("img_set.txt")   
   #if os.path.exists("img_black/*.*"):
   #   os.remove("img_black/*.*")
   if os.path.exists("paragraph.txt"):
      while True:
         print("Save Extract text 'y/n' -")
         opt=input().lower().strip()
         if opt=='y':
            new_file=input("Enter filename: ")
            source_file="paragraph.txt"
            if len(new_file)>0:
               shutil.copyfile(source_file ,new_file)
               print("extracted data saved")
               os.remove("paragraph.txt")
               break
            else:
               print("filename couldn't be null")
               continue
         elif opt=='n':
            os.remove("paragraph.txt")
            print("extracted file removed")
            break
         else :
            print("Invalid Entry")

def read_text():
   print("Enter filename to read ")     
   filename=input("Filename: ") 
   cmd="cat "+filename
   subprocess.run([cmd,"-l"],shell=True)
   
def menu():
   while True:
      print("."*60)
      print("1. Enter file \n2. Convert Image RGB to Grayscale\n3. Extract text from images\n4. Save exracted word to file\n5. Read from textfile\n6. Bulk file\nx. Exit Application  ")
      opt=input("\tYour choice: ").lower().strip()
      print("."*60)
      if opt=='1':
         validate_img()
      elif opt =='2':
         rgb_to_gray()
      elif opt=='3':
         img_to_txt() 
      elif opt=='4':
         sanitize_words()
      elif opt=='5':
         read_text()   
      elif opt=='6':
         print("place this script in dir , where you want to extract data ")
         diskfile()
      elif opt=='x':
         print("Exiting application")   
         time.sleep(.5)
         break        
      else :
         print("Invalid Entry: ") 
menu()
