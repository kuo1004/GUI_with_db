
import tkinter as tk
import socket
import threading

import datetime
class ChatApp:
    def __init__(self):
        self.name = ''
        self.user = ''
        self.s = None
        self.server = None
        self.clientAddr = None
        
        self.root7 = tk.Tk()
        self.root7.rowconfigure(0, weight=1)
        self.root7.rowconfigure(1, weight=1)
        self.root7.rowconfigure(2, weight=1)
        self.root7.rowconfigure(3, weight=1)
        self.root7.columnconfigure(0, weight=1)
        self.root7.columnconfigure(1, weight=1)
        self.root7.columnconfigure(2, weight=1)
        self.root7.columnconfigure(3, weight=1)
        self.root7.title("聊天室")
        
        self.label_ip = tk.Label(self.root7, text="IP:")
        self.label_ip.grid(row=0, column=0, pady=1, padx=2)
        self.entry_ip = tk.Entry(self.root7)
        self.entry_ip.grid(row=0, column=1, pady=1, padx=2)
        
        self.label_port = tk.Label(self.root7, text="Port:")
        self.label_port.grid(row=0, column=2, pady=1, padx=2)
        
        self.entry_port = tk.Entry(self.root7)
        self.entry_port.grid(row=0, column=3, pady=1, padx=2)
        
        self.label_mode = tk.Label(self.root7, text="選擇模式:")
        self.label_mode.grid(row=1, column=0, pady=1, padx=2)
        
        self.mode_var = tk.StringVar()
        self.radio_server = tk.Radiobutton(self.root7, text="Server", variable=self.mode_var, value="server")
        self.radio_server.grid(row=1, column=1, pady=1, padx=2)
        
        self.radio_client = tk.Radiobutton(self.root7, text="Client", variable=self.mode_var, value="client")
        self.radio_client.grid(row=1, column=2, pady=1, padx=2)
        
        self.start_button = tk.Button(self.root7, text="開始", command=self.start)
        self.start_button.grid(row=1, column=3, pady=1, padx=2)
        
        self.label_message = tk.Label(self.root7, text="輸入文字:")
        self.label_message.grid(row=2, column=0, pady=1, padx=2)
        self.entry_message = tk.Entry(self.root7)
        self.entry_message.grid(row=2, column=1, pady=1, padx=2, columnspan=2)
        
        self.button_send = tk.Button(self.root7, text="確認", command=self.send_message)
        self.button_send.grid(row=2, column=3, pady=1, padx=2)
        
        self.textbox = tk.Text(self.root7)
        self.textbox.grid(row=3, column=0, columnspan=4)
        
        self.root7.mainloop()

    def sever_recv(self, sock, addr):
        self.textbox.insert(tk.END, "聊天室啟動:")
        
        sock.sendto(self.name.encode('utf-8'), addr)
        while True:
            data = sock.recv(1024)
            recvMsg = data.decode('utf-8')
            self.textbox.insert(tk.END, recvMsg)
            self.textbox.insert(tk.END, "\n")
            if recvMsg.lower() == 'EXIT'.lower():
                break
    
    def client_recv(self, sock, addr):
        self.textbox.insert(tk.END, "聊天室啟動:")
        self.textbox.insert(tk.END, "\n")
        sock.sendto(self.name.encode('utf-8'), addr)
        while True:
            data = sock.recv(1024)
            recvMsg = data.decode('utf-8')
            self.textbox.insert(tk.END, recvMsg)
            self.textbox.insert(tk.END, "\n")
            if recvMsg.lower() == 'EXIT'.lower():
                break

    def send(self, sock, addr):
        
        string = self.entry_message.get()
        message = self.user + ':' + string
        data = message.encode("utf-8")
        sock.sendto(data, addr)
        self.textbox.insert(tk.END, message)
        self.textbox.insert(tk.END, "\n")
    
    def start_server(self):
        time_now=datetime.datetime.now()
        self.name = ''
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.textbox.insert(tk.INSERT, time_now)
        self.textbox.insert(tk.INSERT, "\n")
        self.textbox.insert(tk.INSERT, "-----連線中-----")
        self.textbox.insert(tk.INSERT, "\n")
        host = self.entry_ip.get()
        port = self.entry_port.get()
        self.server = (host, int(port))
        self.s.bind(self.server)
        msg, self.clientAddr = self.s.recvfrom(1024)
        self.name = msg.decode('utf-8')
        tr = threading.Thread(target=self.sever_recv, args=(self.s, self.server), daemon=True)
        
        try:
            tr.start()
        except ConnectionResetError:
            print('Error: someone left unexpect.')

    def start_client(self):
        time_now=datetime.datetime.now()
        self.name = ''
        self.textbox.insert(tk.INSERT, time_now)
        self.textbox.insert(tk.INSERT, "\n")
        self.textbox.insert(tk.INSERT, "-----歡迎來到聊天室-----")
        self.textbox.insert(tk.INSERT, "\n")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        host = self.entry_ip.get()
        port = int(self.entry_port.get())
        self.server = (host, port)
        tr = threading.Thread(target=self.client_recv, args=(self.s, self.server), daemon=True)
        tr.start()

    def start(self):
        self.user = ''
        if self.mode_var.get() == "server":
            self.user = 'server'
            tr = threading.Thread(target=self.start_server)
            tr.start()
        elif self.mode_var.get() == "client":
            #print("test")
            self.user = 'client'
            self.start_client()

    def send_message(self):
        if self.mode_var.get() == "server":
            ts = threading.Thread(target=self.send, args=(self.s, self.clientAddr))
            ts.start()
        elif self.mode_var.get() == "client":
            ts = threading.Thread(target=self.send, args=(self.s, self.server))
            ts.start()
ChatApp()