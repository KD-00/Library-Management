
def create():
	import mysql.connector
	mydb=mysql.connector.connect(host='localhost',user='root',password='mysql')
	if mydb.is_connected()==True:
		print("Connection established between MySQL and Program")
	mycursor=mydb.cursor()
	mycursor.execute("CREATE DATABASE library")
	print("libraray Database Created")

	mycursor.execute("USE library")
	mycursor.execute('''CREATE TABLE bookrecord
		(bno int primary key auto_increment,
		bname varchar(50),
		author varchar(30),
		price int ,
		publ varchar(30),
		qty int default 1,
		d_o_purchase date)''')
	print("bookrecord Table Created")

	mycursor.execute('''CREATE TABLE member
		(mno int primary key auto_increment,
		mname varchar(50),
		mob varchar(10) ,
		dop date,
		adr varchar(200))''')
	print("memeber Table Created")

	mycursor.execute('''CREATE TABLE issue
		(bno int ,
		mno int,
		d_o_issue date,
		d_o_ret date,
		primary key(bno,mno),
		foreign key(bno) references bookrecord(bno))''')
	print("issue Table Created")
 

