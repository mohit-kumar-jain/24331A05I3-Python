import tkinter as tk

root = tk.Tk()
root.title("First GUI code")
root.geometry("300x200")

label = tk.Label(root, text="Hello World", font=("Arial", 16))

label.pack(pady=50)

root.mainloop()