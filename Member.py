# MODULE: MEMBER

import mysql.connector
from datetime import date, datetime
import pandas as pd


def display():
	cnx = mysql.connector.connect(host='localhost',user='root',password='mysql',database='library')
	Cursor = cnx.cursor()
	query = ("SELECT * FROM Member")
	Cursor.execute(query)
	result=Cursor.fetchall()
	df=pd.DataFrame(result)
	df.columns=["Member Code", "Memeber Name","  Mobile Number","  Date of Memebership","  Address"]
	print(df)
	Cursor.close()
	cnx.close()
	a=input("Enter any key to continue...")
	

def insertMember():
	cnx = mysql.connector.connect(host='localhost',user='root',password='mysql',database='library')
	Cursor = cnx.cursor()
	mno=input("Enter Member Code : ")
	mname=input("Enter Member Name : ")
	mob=input("Enter Member Mobile No. : ")
	print("Enter Date of Membership (Date/MOnth and Year seperately: ")
	DD=int(input("Enter Date : "))
	MM=int(input("Enter Month : "))
	YY=int(input("Enter Year : "))
	adr=input("Enter Member Adress : ")
	Qry = ("INSERT INTO Member "\
	"VALUES (%s, %s, %s, %s, %s)")
	data = (mno,mname,mob,date(YY,MM,DD),adr)
	Cursor.execute(Qry,data)
	cnx.commit()
	Cursor.close()
	cnx.close()
	print("Record Inserted.")
	a=input("Enter any key to continue...")


def deleteMember():
	cnx = mysql.connector.connect(host='localhost',user='root',password='mysql',database='library')
	Cursor = cnx.cursor()
	mno=input("Enter Member Code to be deleted from the Library : ")
	Qry =("""DELETE FROM Member WHERE mno = %s""")
	del_rec=(mno,)
	Cursor.execute(Qry,del_rec)
	cnx.commit()
	Cursor.close()
	cnx.close()
	print("Record Deleted Successfully.")
	a=input("Enter any key to continue...")
	

def SearchMember():
	cnx = mysql.connector.connect(host='localhost',user='root',password='mysql',database='library')
	Cursor = cnx.cursor()
	mname=input("Enter Member Name to be Searched from the Library : ")
	query = ("SELECT * FROM Member where mname = %s ")
	rec_srch=(mname,)
	Cursor.execute(query,rec_srch)
	Rec_count=0
	for (mno,mname,mob,dop,adr) in Cursor:
		Rec_count=1
		print("Member Code : ",mno)
		print("Member Name : ",mname)
		print("Mobile No.of Member : ",mob)
		print("Date of Membership : ",dop)
		print("Address : ",adr)
	if Rec_count==1:
		print("Record Found")
	else:
		print("Record Not Found")
	cnx.commit()
	Cursor.close()
	cnx.close()
	a=input("Enter any key to continue...")	