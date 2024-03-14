import PySimpleGUI as sg
import mysql.connector as myconn

def root2():
    layout2 = [
        [sg.Button('帳號管理'), sg.Button('影像預覽')],
        [sg.Button('影像管理'), sg.Button('電話篩選')],
        [sg.Button('聊天即時通'), sg.Button('離開')]
    ]
    root = sg.Window('功能選單', layout2, font=('BluePurple', 12))
    while True:
        event, values = root.read()

        if event == sg.WINDOW_CLOSED or event == '離開':
            break

        if event == '帳號管理':
            print('選擇了帳號管理')

    # 關閉視窗
    root.close()

# 定義登入介面的佈局
layout = [
    [sg.Text('使用者名稱', size=(15, 1)), sg.InputText()],
    [sg.Text('密碼', size=(15, 1)), sg.InputText(password_char='*')],
    [sg.Button('登入'), sg.Button('取消')]
]

# 創建登入視窗
window = sg.Window('使用者登入', layout, font=('BlueMono', 12))

# 事件迴圈
while True:
    event, values = window.read()
    dbConn = myconn.connect(
        host="localhost",
        user="Kuo",
        password="D1146229",
        database="Kuo"
    )
    try:
        my_cursor = dbConn.cursor()
        sql = "SELECT * FROM `users`"
        my_cursor.execute(sql)
        result = my_cursor.fetchall()
        dict1 = {}
        for row in result:
            dict1[row[0]] = row[1]

        if event == sg.WINDOW_CLOSED or event == '取消':
            break

        if event == '登入':
            username = values[0]
            password = values[1]
            if username in dict1.keys():
                if dict1[username] == int(password):
                    sg.popup(f'使用者名稱: {username}\n密碼: {password}\n登入成功！')
                    root2()
                else:
                    sg.popup('登入失敗;(')
    finally:
        # 關閉資料庫連接
        my_cursor.close()

# 關閉視窗
window.close()
