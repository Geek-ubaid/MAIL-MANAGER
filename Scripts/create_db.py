import sqlite3

def create_DB():

	DB = sqlite3.connect('Mailing.db')
	conn = DB.cursor()
	print ("Opened DataBase successfully")

	conn.execute('''CREATE TABLE if not exists MAIL
		(MID TEXT PRIMARY KEY,
		SUBJ TEXT NOT NULL,
		BODY TEXT,
		DATE TEXT);''')

	conn.execute('''CREATE TABLE if not exists USERS
		(name TEXT NOT NULL,
		 email_id TEXT NOT NULL,
		 mail_id TEXT,
		 FOREIGN KEY(mail_id) REFERENCES MAIL(MID));''')


	conn.execute('''CREATE TABLE if not exists Reciever
		(From_add TEXT,
		date TEXT,
		mail_id TEXT,
		foreign key(mail_id) references mail(mid));''')




	conn.execute('''CREATE TABLE if not exists ATTACHMENT
		(Name TEXT NOT NULl,
		type TEXT,
		mail_id TEXT,
		size INTEGER,
		id TXT,
		FOREIGN KEY (mail_id) REFERENCES mail(mid));''')

	conn.execute('''CREATE TABLE if not exists Folder
		(folder_name TEXT,
		folder_size INTEGER,
		total INTEGER);''')


	print ("TableS created successfully")


	DB.commit()
	DB.close()
