import os
import sys
import platform
import base64
from pathlib import Path
from cryptography.fernet import Fernet

def gen_key():
   k=input("Enter password: ")
   k=k*33
   k=k[0:32]
   print(k)
   key=base64.b64encode(bytes(k,"utf-8"))
   print("In gen key method",key)
   return key

def encrypt_data():
   filename=data()
   key=gen_key()
   print("filename for encryption:",filename)
   print("key:",key)
   fernet=Fernet(key)
   with open(filename,'rb') as file:
      original=file.read()
   encrypted=fernet.encrypt(original) 
   with open(filename,"wb") as encrypted_file:
      encrypted_file.write(encrypted)
   print("successfuly encrypted [%s] with [%s]"%(filename,key))
   
def decrypt_data():
   filename=data()
   key=gen_key()
  #print("file for decryption ",filename)
   #print("key: ",key)
   fernet=Fernet(key)
   with open(filename,'rb') as file:
      original=file.read()
   encrypted=fernet.decrypt(original) 
   with open(filename,"wb") as encrypted_file:
      encrypted_file.write(encrypted)
   print("successfuly decrypted [%s] with [%s]"%(filename,key))

def data():
   filename=input("Enter filename to encryt: ")
   if os.path.isfile(filename):
      if filename==sys.argv[0]:
         print("[%s] script itself can't be encrypted "%filename)
         print("select file other than [%s]"%sys.argv[0])
         menu()
      else:
         return filename      
   else:
      print("%s not exist "%filename)
      menu()               
      """key=Fernet.generate_key()
      fernet=Fernet(key)
      print("key :[%s] "%str(key))
      #print("fernet object key[%s] "%str(fernet))
      with open(filename,'rb') as file:
         original=file.read()
      encrypted=fernet.encrypt(original) 
      with open(filename,"wb") as encrypted_file:
         encrypted_file.write(encrypted)
      print("successfuly encrypted [%s] with [%s]"%(filename,key))   """
  
   
def menu():
   while True:
      dot="."
      print(dot*40)
      print("1 -encrypt file")
      print("2 -decrypt file")
      print("0 -exit program")
      print(dot*40)
      opt=input("Your selection: ")
      if opt=='1':
         encrypt_data()
      elif opt=='2':
         decrypt_data()
      elif opt=='0':
         print("Exit...")
         break;
      else :
         print("Invalid selection")   
menu()
    
