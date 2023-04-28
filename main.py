from tkinter import *
import subprocess

root = Tk()
root.title("Projects")

def start_server():
    subprocess.Popen(["python", "resource_share_client.py"])

def start_client():
    subprocess.Popen(["python", "screen_share_server.py"])

button1 = Button(root, text="First Project", command=start_server)
button1.pack(pady=10)

button2 = Button(root, text="Second Project", command=start_client)
button2.pack(pady=10)

root.mainloop()
