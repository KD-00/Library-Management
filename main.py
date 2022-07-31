# MODULE : LIBRARY
 
import MenuLib
import Book
import issue
import dbcreate

while True:
	print("\n Library Management\n")
	print("0. If using first time, to Create Database")
	print("1. Book Management ")
	print("2. Members Management ")
	print("3. Issue/Return Book ")
	print("4. Exit ")
	choice=int(input("Enter Choice between 0 to 4 : "))
	if choice==0:
		dbcreate.create()
	elif choice==1:
		MenuLib.MenuBook()
	elif choice==2:
		MenuLib.MenuMember()
	elif choice==3:
		MenuLib.MenuIssueReturn()
	elif choice==4:
		break
	else:
		print("\nWrong Choice......Enter Your Choice again")
		x=input("Enter any key to continue : ")

