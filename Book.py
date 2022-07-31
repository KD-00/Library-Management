# MODULE : BOOK

import mysql.connector
from datetime import date, datetime
import pandas as pd

def display():
	cnx = mysql.connector.connect(host='localhost', user='root',password='mysql',database='library')
	Cursor = cnx.cursor()
	query = ("SELECT * FROM bookrecord")
	Cursor.execute(query)
	result=Cursor.fetchall()
	df=pd.DataFrame(result)
	df.columns=[" Book No.","  Book Name","  Author","  Price","  Publisher","  Quantity","  Date of Purchase"]
	print(df)
	Cursor.close()
	cnx.close()
	a=input("Enter any key to continue...")


def insertData():
	cnx = mysql.connector.connect(host='localhost', user='root',password='mysql',database='library')
	Cursor = cnx.cursor()
	bno=input("Enter Book Number : ")
	bname=input("Enter Book Name : ")
	Auth=input("Enter Book Author's Name : ")
	price=int(input("Enter Book Price : "))
	publ=input("Enter Publisher of Book : ")
	qty=int(input("Enter Quantity purchased : "))
	print("Enter Date of Purchase (Date/MOnth and Year seperately: ")
	DD=int(input("Enter Date : "))
	MM=int(input("Enter Month : "))
	YY=int(input("Enter Year : "))
	Qry = ("INSERT INTO BookRecord "\
		"VALUES (%s, %s, %s, %s, %s, %s, %s)")
	data = (bno,bname,Auth,price,publ,qty,date(YY,MM,DD))
	Cursor.execute(Qry,data)
	cnx.commit()
	Cursor.close()
	cnx.close()
	print("Record Inserted..............")
	a=input("Enter any key to continue...")


def deleteBook():
	cnx = mysql.connector.connect(host="localhost",user="root",password="mysql",database='library')
	Cursor = cnx.cursor()
	bno=input("Enter Book Number of Book to be deleted from the Library : ")
	Qry =("DELETE FROM bookrecord WHERE bno = %s")
	del_rec=(bno,)
	Cursor.execute(Qry,del_rec)
	cnx.commit()
	Cursor.close()
	cnx.close()
	print(Cursor.rowcount,"Record Deleted Successfully")
	a=input("Enter any key to continue...")
	
	
def SearchBookRec():
	cnx = mysql.connector.connect(host='localhost', user='root',password='mysql',database='library')
	Cursor = cnx.cursor()
	bno=input("Enter Book Number to be Searched from the Library : ")
	query = ("SELECT * FROM BookRecord where bno = %s ")
	rec_srch=(bno,)
	Cursor.execute(query,rec_srch)
	Rec_count=0
	for (bno,bname,author,price,publ,qty,d_o_purchase) in Cursor:
		Rec_count=1
		print("Book Number : ",bno)
		print("Book Name : ",bname)
		print("Author of Book : ",author)
		print("Price of Book : ",price)
		print("Publisher : ",publ)
		print("Total Quantity in Hand : ",qty)
		print("Purchased On : ",d_o_purchase)
	if Rec_count==1:
		print(Rec_count, "Record found")
	else:
		print("Record not found")
	cnx.commit()
	Cursor.close()
	cnx.close()
	a=input("Enter any key to continue...")


def UpdateBook():
	cnx = mysql.connector.connect(host='localhost', user='root',password='mysql',database='library')
	Cursor = cnx.cursor()
	bno=input("Enter Book Number of Book to be Updated from the Library : ")
	query = ("SELECT * FROM BookRecord where BNo = %s ")
	rec_srch=(bno,)
	print("Enter new data ")
	bname=input("Enter Book Name : ")
	author=input("Enter Book Author's Name : ")
	price=int(input("Enter Book Price : "))
	publ=input("Enter Publisher of Book : ")
	qty=int(input("Enter Quantity purchased : "))
	print("Enter Date of Purchase (Date,Month and Year seperately: ")
	DD=int(input("Enter Date : "))
	MM=int(input("Enter Month : "))
	YY=int(input("Enter Year : "))

	Qry = ("UPDATE bookrecord SET bname=%s,author=%s,"\
	"price=%s,publ=%s,qty=%s,d_o_purchase=%s "\
	"WHERE bno=%s")

	data = (bname,author,price,publ,qty,date(YY,MM,DD),bno)
	Cursor.execute(Qry,data)
	cnx.commit()
	Cursor.close()
	cnx.close()
	print(Cursor.rowcount,"Record Updated Successfully")
	a=input("Enter any key to continue...")