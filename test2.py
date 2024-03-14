import tkinter as tk
from tkinter import ttk
import mysql.connector as myconn
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as myconn
import mysql.connector as myconn
from tkinter import *
def image_browser():

    def fetch_image_data():
        selected_type = combol.get()

        dbConn = myconn.connect(
            host="localhost",
            user="Kuo",
            password="D1146229",
            database="Kuo"
        )
        cursor = dbConn.cursor()

        query = "SELECT file_name, name, time FROM `photodt` WHERE type=%s"
        cursor.execute(query, (selected_type,))
        image_data = cursor.fetchall()

        # 關閉資料庫連接
        cursor.close()
        dbConn.close()

        return image_data

    def show_image():
        nonlocal current_index
        if 0 <= current_index < len(image_data):
            image_path, image_name, image_time = image_data[current_index]
            image = Image.open(image_path)
            image = image.resize((300, 300))
            photo = ImageTk.PhotoImage(image)
            image_label.configure(image=photo)
            image_label.image = photo  # 保持對圖像物件的引用

            formation_label.config(text=f"Name: {image_name}\nType: {combol.get()}\nTime: {image_time}")

    def next_image():
        nonlocal current_index
        if current_index < len(image_data) - 1:
            current_index += 1
            show_image()

    def previous_image():
        nonlocal current_index
        if current_index > 0:
            current_index -= 1
            show_image()

    root8 = tk.Toplevel()
    root8.title("Image Browser")

    _label = tk.Label(root8, text='choose photo type:')
    _label.grid(row=0, column=0, sticky="w")

    combol = ttk.Combobox(root8, values=['person', 'family'])
    combol.current(0)
    combol.grid(row=0, column=1, sticky="w")

    image_data = []
    current_index = 0

    def open_images():
        nonlocal image_data, current_index
        image_data = fetch_image_data()
        current_index = 0
        show_image()

    open_button = tk.Button(root8, text="open", command=open_images)
    open_button.grid(row=0, column=2, sticky="e")

    image_label = tk.Label(root8)
    image_label.grid(row=1, column=0, columnspan=3)

    next_button = tk.Button(root8, text="Next", command=next_image)
    next_button.grid(row=2, column=2, sticky="e")

    previous_button = tk.Button(root8, text="Previous", command=previous_image)
    previous_button.grid(row=2, column=0, sticky="w")

    formation_label = tk.Label(root8, text="")
    formation_label.grid(row=2, column=1)

    root8.mainloop()
image_browser()