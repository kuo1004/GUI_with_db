import tkinter as tk
import threading
import socket

clientAddr = 0
name = ''
user = ''

def server_recv(sock, addr):
    global name
    textbox.insert(tk.END, "聊天室啟動:")
    sock.sendto(name.encode('utf-8'), addr)
    while True:
        data = sock.recv(1024)
        recvMsg = data.decode('utf-8')
        textbox.insert(tk.END, recvMsg + "\n")
        if recvMsg.lower() == 'EXIT'.lower():
            break

def client_recv(sock, addr):
    textbox.insert(tk.END, "聊天室啟動:\n")
    sock.sendto(name.encode('utf-8'), addr)
    while True:
        data = sock.recv(1024)
        textbox.insert(tk.END, data.decode('utf-8'))

def send(sock, addr):
    string = entry_message.get()
    message = user + ':' + string
    data = message.encode("utf-8")
    sock.sendto(data, addr)
    textbox.insert(tk.END, message )
    textbox.insert(tk.END,"\n")


def start_server():
    global name
    global clientAddr
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = entry_ip.get()
    port = entry_port.get()
    server = (host, int(port))
    s.bind(server)
    msg, clientAddr = s.recvfrom(1024)
    name = msg.decode('utf-8')
    tr = threading.Thread(target=server_recv, args=(s, clientAddr), daemon=True)

    try:
        tr.start()
    except ConnectionResetError:
        print('Error: someone left unexpectedly.')

def start_client():
    global s
    global server
    textbox.insert(tk.INSERT, "-----歡迎來到聊天室-----\n")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = entry_ip.get()
    port = int(entry_port.get())
    server = (host, port)
    tr = threading.Thread(target=client_recv, args=(s, server), daemon=True)
    tr.start()

def start():
    global user
    if mode_var.get() == "server":
        user = 'server'
        tp = threading.Thread(target=start_server)
        tp.start()
    elif mode_var.get() == "client":
        user = 'client'
        start_client()

def send_message():
    if mode_var.get() == "server":
        ts = threading.Thread(target=send, args=(s, clientAddr))
        ts.start()
    elif mode_var.get() == "client":
        ts = threading.Thread(target=send, args=(s, server))
        ts.start()

root = tk.Tk()
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.title("聊天室")

label_ip = tk.Label(root, text="IP:")
label_ip.grid(row=0, column=0, pady=1, padx=2)
entry_ip = tk.Entry(root)
entry_ip.grid(row=0, column=1, pady=1, padx=2)
label_port = tk.Label(root, text="Port:")
label_port.grid(row=0, column=2, pady=1, padx=2)

entry_port = tk.Entry(root)
entry_port.grid(row=0, column=3, pady=1, padx=2)

label_mode = tk.Label(root, text="選擇模式:")
label_mode.grid(row=1, column=0, pady=1, padx=2)

mode_var = tk.StringVar()
radio_server = tk.Radiobutton(root, text="Server", variable=mode_var, value="server")
radio_server.grid(row=1, column=1, pady=1, padx=2)

radio_client = tk.Radiobutton(root, text="Client", variable=mode_var, value="client")
radio_client.grid(row=1, column=2, pady=1, padx=2)

start_button = tk.Button(root, text="開始", command=start)
start_button.grid(row=1, column=3, pady=1, padx=2)

label_message = tk.Label(root, text="輸入文字:")
label_message.grid(row=2, column=0, pady=1, padx=2)
entry_message = tk.Entry(root)
entry_message.grid(row=2, column=1, pady=1, padx=2, columnspan=2)

button_send = tk.Button(root, text="確認", command=send_message)
button_send.grid(row=2, column=3, pady=1, padx=2)

textbox = tk.Text(root)
textbox.grid(row=3, column=0, columnspan=4)

root.mainloop()
