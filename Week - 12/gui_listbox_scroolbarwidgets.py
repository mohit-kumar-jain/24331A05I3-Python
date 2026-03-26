import tkinter as tk

root = tk.Tk()
root.title("Listbox and Scrollbar Demo")
root.geometry("300x250")

frame = tk.Frame(root)
frame.pack(pady=20)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)

for i in range(1, 51):
    listbox.insert(tk.END, f"Item {i}")

listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=listbox.yview)

root.mainloop()