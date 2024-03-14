
import tkinter as tk
from tkinter import ttk
from tkinter import *
from mysql.connector import connect
from PIL import ImageTk, Image
import mysql.connector as myconn

class ImageBrowser:
    def __init__(self):
        self.dbConn = myconn.connect(
            host="localhost",
            user="Kuo",
            password="D1146229",
            database="Kuo"
        )
        self.cursor = self.dbConn.cursor()
        self.image_paths = []
        self.image_info = {}

        self.root = tk.Tk()
        self.root.title("Image Browser")

        self._label = tk.Label(self.root, text='choose photo type:')
        self._label.grid(row=0, column=0, sticky="w")

        self.combol = ttk.Combobox(self.root, values=['person', 'family'])
        self.combol.current(0)
        self.combol.grid(row=0, column=1, sticky="w")

        self.open_button = tk.Button(self.root, text="open", command=self.fetch_image_paths)
        self.open_button.grid(row=0, column=2, sticky="e")

        self.image_label = tk.Label(self.root)
        self.image_label.grid(row=1, column=0, columnspan=3)

        self.current_index = 0

        self.next_button = tk.Button(self.root, text="Next", command=self.next_image)
        self.next_button.grid(row=2, column=2, sticky="e")

        self.previous_button = tk.Button(self.root, text="Previous", command=self.previous_image)
        self.previous_button.grid(row=2, column=0, sticky="w")

        self.info_label = tk.Label(self.root)
        self.info_label.grid(row=2, column=1, sticky="w")

        self.fetch_image_paths()
        self.show_image()

        self.root.mainloop()

    def fetch_image_paths(self):
        self.current_index = 0  # Reset the current index when switching photo type
        selected_type = self.combol.get()

        query = "SELECT file_name, name, time, type FROM `photodt` WHERE type=%s"
        self.cursor.execute(query, (selected_type,))
        self.image_paths = self.cursor.fetchall()

    def show_image(self):
        if 0 <= self.current_index < len(self.image_paths):
            image_path = self.image_paths[self.current_index][0]
            image = Image.open(image_path)
            image = image.resize((300, 300))
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo

            file_name = self.image_paths[self.current_index][0]
            name = self.image_paths[self.current_index][1]
            time = self.image_paths[self.current_index][2]
            image_type = self.image_paths[self.current_index][3]

            info_text = f"File Name: {file_name}\nName: {name}\nTime: {time}\nType: {image_type}"
            self.info_label.configure(text=info_text)

    def next_image(self):
        if self.current_index < len(self.image_paths) - 1:
            self.current_index += 1
            self.show_image()

    def previous_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_image()

ImageBrowser()
