import socket
import cv2
import numpy as np
import io
import threading
from tkinter import *
from PIL import Image, ImageTk


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address ="10.20.204.233"
server_address = (ip_address, 5000)  
client_socket.connect(server_address)


root = Tk()
screenshot_label = Label(root)
screenshot_label.pack()


def receive_screenshot():
    while True:
        
        size_bytes = client_socket.recv(8)

        
        buffer_size = int.from_bytes(size_bytes, byteorder='big')

       
        screenshot_bytes = b''
        while len(screenshot_bytes) < buffer_size:
            remaining = buffer_size - len(screenshot_bytes)
            screenshot_bytes += client_socket.recv(1024 if remaining > 1024 else remaining)

        
        screenshot = cv2.imdecode(np.frombuffer(screenshot_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)

        
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
        screenshot = Image.fromarray(screenshot)
        screenshot = ImageTk.PhotoImage(screenshot)

        
        screenshot_label.configure(image=screenshot)
        screenshot_label.image = screenshot

   
    client_socket.close()


receive_thread = threading.Thread(target=receive_screenshot)
receive_thread.start()


root.mainloop()
