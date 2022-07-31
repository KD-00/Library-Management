# MODULE : ISSUE

import mysql.connector
from datetime import date, timedelta
import pandas as pd


def ShowIssuedBooks():
	cnx = mysql.connector.connect(host='localhost', user='root',password='mysql',database='library')
	Cursor = cnx.cursor()
	query = ("SELECT B.bno,bname,M.mno,mname,d_o_issue,d_o_ret FROM bookrecord B,issue I"\
	",member M where B.bno=I.bno and I.mno=M.mno")
	Cursor.execute(query)
	result=Cursor.fetchall()
	df=pd.DataFrame(result)
	df.columns=[" Book No.","  Book Name","  Member No.","  Member Name","  Date of issue","  Date of return"]
	print(df)
	Cursor.close()
	cnx.close()
	a=input("Enter any key to continue...")



def issueBook():
	cnx = mysql.connector.connect(host='localhost', user='root',password='mysql',database='library')
	Cursor = cnx.cursor()
	bno=input("Enter Book Code to issue : ")
	mno=input("Enter Member Code : ")
	print("Enter Date of Issue (Date,Month and Year seperately: ")
	DD=int(input("Enter Date : "))
	MM=int(input("Enter Month : "))
	YY=int(input("Enter Year : "))
	d_o_issue=date(YY,MM,DD)
	d_o_ret = d_o_issue + timedelta(days=14)
	Qry = ("INSERT INTO issue (bno,mno,d_o_issue,d_o_ret)"\
	"VALUES (%s, %s, %s,%s)")
	data = (bno,mno,d_o_issue,d_o_ret)
	Cursor.execute(Qry,data)
	cnx.commit()
	Cursor.close()
	cnx.close()
	print("Record Inserted.")
	a=input("Enter any key to continue...")


def returnBook():
	cnx = mysql.connector.connect(host='localhost', user='root',password='mysql',database='library')
	Cursor = cnx.cursor()
	bno=input("Enter Book Code of Book to be returned to the Library : ")
	Mno=input("Enter Member Code of Member who is returning Book : ")
	retDate=date.today()
	Qry =("""Update Issue set d_o_ret= %s WHERE BNO = %s and Mno= %s """)
	rec=(retDate,bno,Mno)
	Cursor.execute(Qry,rec)
	cnx.commit()
	Cursor.close()
	cnx.close()
	print("Book returned Successfully.")
	a=input("Enter any key to continue...")

	



