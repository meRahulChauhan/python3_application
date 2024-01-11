import mysql.connector 
from mysql.connector import Error
import re
from random import random

class makeConnection():

	def __init__(self):
		try:
			self.cnx=mysql.connector.connect(host="localhost",database="USER_MANAGEMENT",user="root",password="")
			self.cursor=self.cnx.cursor()
			if self.cnx.is_connected():
				self.dbInfo=self.cnx.get_server_info()
				print("connected to ",self.dbInfo)

		except Error as e:
			print("error occured")
			print("Possible cause: error in username,password,hostname,database ,connection down")	

	def printDb(self):
		self.cursor.execute("select database();")
		dbInUse=self.cursor.fetchone()
		print("database in use ",dbInUse)

	def listDb(self):
		self.cursor.execute("show databases;")
		db=cursor.fetchall()
		print("database list ",db)

	def listTb(self):
		self.cursor.execute("show tables;")
		tb=self.cursor.fetchall()
		print("tables list ",tb)

	def createDb(self):
		query1=input("new database:")
		query="CREATE DATABASE "+query1
		print("command to be execute",query)
		try:
			self.cursor.execute(query)
			print(query1 ,"created successfuly")
		except Error as e:
			print("error occured" ,e)	

	def createTb(self):
		query=input("table:")
		#query="CREATE TABLE "+query1
		print("command to be execute",query)
		try:
			self.cursor.execute(query)
			print(query ,"created successfuly")
		except Error as e:
			print("error occured" ,e)			

	def dropDb(self):
		query1=input("database to delete: ")
		query="DROP DATABASE "+query1
		try:

			self.cursor.execute(query)
			print(query1," successfulyremoved")
		except Error as e:
			print("error occured ",e)	
	def dropTb(self):
		query1=input("Table to delete: ")
		query="DROP TABLE "+query1
		try:
			self.cursor.execute(query)
			print(query1," successfulyremoved")
		except Error as e:
			print("error occured ",e)			

	def listDb(self):
		self.cursor.execute("show databases;")
		db=self.cursor.fetchall()
		print("database list ",db)

	def insertData(self,text):
		sql_query="INSERT INTO `myTable` (`custumID`,`passcode`,`name`,`phone`,`email`,`postalCode`,`city`,`country`,`age`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s');" %(text['email'],text['password'],text['name'],text['phone'],text['email'],text['postalCode'],text['city'],text['country'],text['age'])
		print(sql_query)
		try:
			self.cursor.execute(sql_query)
			self.cnx.commit()
			#print("inserted Data")
		except Error as e:
			print("failed", e)		
			
class userRegistration(makeConnection):
	def createUser(self):
		self.verificationStatus="pending"
		while(True) :
			self.name=input("name: ")
			while(self.validateAlpha(self.name)):
				self.email=input("email: ")
				query=" select * from  "+"myTable"+" where email="+'"'+self.email+'";'
				while(self.validateEmail(self.email) and self.checkAvailability(self.email,query)):
					self.phone=input("phone: ")
					while(self.validateNumeric(self.phone,10)):
						self.age=input("age: ")
						while(self.validateAge(self.age)):
							self.city=input("city: ")
							while(self.validateAlpha(self.city)):
								self.postalCode=input("postal Code: ")
								while(self.validateNumeric(self.postalCode,6)):
									self.country=input("Country: ")
									while(self.validateAlpha(self.country)):
										self.password=input("password: ")
										while(self.setCustomPassCode(self.password)):
											self.userData=dict(name=self.name,email=self.email,password=self.password,
											phone=self.phone,age=self.age,city=self.city,postalCode=self.postalCode,
											country=self.country)
											print(self.userData)
											self.insertData(self.userData)
											print("Account Created,log in with following credentials")
											print("\tEmail:",self.email)
											print("\tpassword:",self.password)
											return False
	def logIn(self):
		self.email=input("email: ")
		while(self.validateEmail(self.email)):
			if self.checkUserIdAvailibility(self.email):
				self.password=input("password: ")
				if self.password==self.result:
					print|("login success")
				else: 
					print("password doesn't match ")	
					return False


	def validateAlpha(self,text,minLength=2,maxLength=32):
		if len(text)>=maxLength or len(text)<=minLength :
			print("expected length between 2-32 but ",len(text)," given")
			#self.createUser()
			return False
		if not text.isalpha():
			print("only alphabets allowed")
			#self.createUser()
			return False
		else :
			return True	

	def validateNumeric(self,text,maxLength):
		if not text.isnumeric():
			print("Only numeric value are allowed")
			return False
		if not len(text)==maxLength:
			print(maxLength," digit expected but",len(text)," given")
			return False
		else :
			return True	

	def validateAlphaNum(self,text,minLength=8,maxLength=32):
			if len(text)>maxLength or len(text)<minLength:
				print("expected length between 8-32 but : ",len(text)," given")
				return False
			#self.createUser()
			if not text.isalphanum():
				print("only alphanumeric allowed")
				return False
			else :
				return True	

	def validateAge(self,text):
		if len(text)==0:
			print("expected at least 1 digit but",len(text)," given")
			return False
		if not text.isnumeric():
			print("expected numeric value but",type(text)," given")
			return False
		elif int(text)>120 or int(text)	<0:
			print("age must be between 0-120 years")
			return False
		else :
			return True	

	def validateEmail(self,text):
		regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z0-9]{2,7}\b'
		if(re.fullmatch(regex,text)):
			return True
		else:
			print("expected format 'userId@email.com' but ",'"',text,'"'," given")
			return False	

	def checkAvailability(self,email,query):
		#print(query)
		self.cursor.execute(query)
		self.result=self.cursor.fetchone()
		#print(self.cursor.rowcount)
		if self.cursor.rowcount>0:
			print(email,"not available")
			return False
		elif self.cursor.rowcount==-1:
			print(email,"available")
			return True

	def checkUserIdAvailibility(self,email):
		query="select passcode from myTable where email='"+email+"';"
		#print(query)
		self.cursor.execute(query)
		self.result=self.cursor.fetchone()
		print(type(self.result))	
		#print(self.cursor.rowcount)
		if self.cursor.rowcount>0:
			print(email,"available")
			return True
		elif self.cursor.rowcount==-1:
			print(email," not exists")
			return False

	def generateOtp(text,minLength=6):
		letters="QWE1RTY2UI3OP4AS5DF6GH7JKL8ZXC9VBNM0"
		OTP=""
		for i in range(0,minLength):
			OTP+=random.choice(letters)
		return(self.OTP)	
	
	def setCustomPassCode(self,password,minLength=6,maxLength=32):
		if len(password)>maxLength or len(password)<minLength:
			print("expected password length between 6-32 but",len(password)," given")
			return False
		else :
			return True

	def sendPasscode(self,email,data):
		print("service not available")


#class fetchData(makeConnection):


#obj=makeConnection()
#obj.printDb()
#obj.listDb()
#obj.listTb()
#obj.createDb()
#obj.dropDb()
#obj.createTb()
#obj2=userRegistration()
#obj2.printDb()
#obj2.insertData()

#newObj=fetchData()
#newObj.checkAvailability("myTable","rc5565931@gmail.com")

newObj=userRegistration()
def menu():
	while(True):		
		print("1.LogIn \n2.Create Account\n3.Reset Password")
		opt=int(input("choice: "))
		if opt==1:
			newObj.logIn()
		if opt==2:
			newObj.createUser()
		else:
			print("invalid choice")	
menu()	