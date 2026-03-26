import tkinter as tk
from tkinter import messagebox, filedialog

root = tk.Tk()
root.title("Messagebox and File Dialog Demo")
root.geometry("350x200")

def show_message():
    messagebox.showinfo("Info", "Hello! This is a message box")

def open_file():
    file_path = filedialog.askopenfilename()
    label.config(text=file_path)

btn1 = tk.Button(root, text="Show Message", command=show_message)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Open File", command=open_file)
btn2.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()