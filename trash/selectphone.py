import mysql.connector as myconn
import mysql.connector
import re
from tkinter import *

class Phonenumber:
    def __init__(self):
        self.dbConn=myconn.connect(
        host="localhost",
        user="Kuo",
        password="D1146229",
        database="Kuo"
    )
        self.root = Tk()
        self.root.geometry('500x300')
        self.number_text = Text(self.root, width=60, height=8)
        self.number_text.grid(row=0, column=0)
        self.number_button = Button(self.root, text="執行", command=self.number_find)
        self.number_button.grid(row=0, column=1)
        self.result_text = Text(self.root, width=60, height=8)
        self.result_text.grid(row=1, column=0, columnspan=2)
        self.root.mainloop()

    def number_find(self):
        dbConn=myconn.connect(
        host="localhost",
        user="Kuo",
        password="D1146229",
        database="kuo"
    )
        cursor = dbConn.cursor()
        txt = self.number_text.get("1.0", "end-1c")
        phoneNum = re.findall(r'\d{4}-\d{3}-\d{3}|\(\d{2}\)\d{8}|\+\d{3}-\d{1}-\d{4}-\d{4}|\d{10}|\(\d{2}\)\d{4}-\d{4}', txt)
        if phoneNum:
            self.result_text.delete("1.0", "end")
            for phone in phoneNum:
                self.result_text.insert("end", phone + "\n")
        else:
            self.result_text.delete("1.0", "end")
            self.result_text.insert("end", "No data")
        article = txt
        number = "\n".join(phoneNum) if phoneNum else "No data"
        cursor = dbConn.cursor()
        query = "INSERT INTO `selectphone` (article, number) VALUES (%s, %s)"

        values = (article, number)
        cursor.execute(query, values)
        dbConn.commit()
        cursor.close()



