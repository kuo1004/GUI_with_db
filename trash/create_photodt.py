import os
from datetime import datetime
import tkinter as tk
from PIL import Image
from tkinter import filedialog
import mysql.connector as myconn
from tkinter import messagebox


class ImagePreview:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Image Preview App")

        self.selected_image = None

        # 創建按鈕、標籤和清單框
        self.select_button = tk.Button(self.root, text="選取圖片", command=self.select_image)
        self.select_button.pack()

        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        self.image_listbox = tk.Listbox(self.root, width=50)
        self.image_listbox.pack()

        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side="right", fill="y")

        self.image_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.image_listbox.yview)
        self.update = tk.Frame(self.root)
        self.update.pack()
        self.LM = tk.Label(self.update, text="檔名:")
        self.LM.pack(side="left")
        self.name = tk.Entry(self.update)
        self.name.pack(side="right")
        self.submit = tk.Button(self.root, text="submit", command=self.update_database)
        self.submit.pack()
        self.root.mainloop()

    def select_image(self):
        # 開啟檔案對話方塊，讓使用者選取圖片
        filepath = filedialog.askopenfilename(initialdir="/", title="選取圖片",
                                              filetypes=(("JPEG files", "*.jpg;*.jpeg"), ("PNG files", "*.png"),
                                                         ("All files", "*.*")))
        if filepath:
            self.selected_image = filepath

            # 轉換圖片到PNG格式
            self.convert_to_png()

            # 顯示圖片預覽
            self.show_image_preview()

            # 儲存圖片資訊到清單框
            self.save_image_info(filepath)

    def convert_to_png(self):
        # 獲取檔案名稱（不包含副檔名）
        filename, _ = os.path.splitext(self.selected_image)

        # 設定輸出檔案的路徑和檔名
        output_filepath = f"{filename}.png"

        # 轉換圖片格式到PNG，並調整大小為400x400像素
        img = Image.open(self.selected_image)
        img = img.resize((300, 300))
        img.save(output_filepath, "PNG")

        # 更新選取的圖片為轉換後的PNG圖片
        self.selected_image = output_filepath

    def show_image_preview(self):
        # 顯示選取的圖片預覽
        image = tk.PhotoImage(file=self.selected_image)

        self.image_label.configure(image=image)
        self.image_label.image = image

    def save_image_info(self, filepath):
        # 獲取檔案名稱和建立時間
        filename = os.path.basename(filepath)
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 將檔案名稱顯示在清單框中
        self.image_listbox.insert("end", f"File: {filename}, Created At: {created_at}")

    def update_database(self):
        dbConn = myconn.connect(
            host="localhost",
            user="Kuo",
            password="D1146229",
            database="Kuo"
        )
        try:
            filename, _ = os.path.splitext(self.selected_image)
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            output_filepath = f"{filename}.png"
            name = self.name.get()
            cursor = dbConn.cursor()
            query = "INSERT INTO `photodt` (type, file_name, name, time) VALUES (%s, %s, %s, %s)"

            values = ('person', output_filepath, name, created_at)
            cursor.execute(query, values)
            dbConn.commit()
            cursor.close()
            messagebox.showinfo("done", '新增成功')
        except:
            messagebox.showerror('Error!', '新增失敗')


ImagePreview()
