import tkinter as tk

root = tk.Tk()
root.title("Menu and Menubutton Demo")
root.geometry("300x200")

def show(text):
    label.config(text=text)

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=lambda: show("New Selected"))
file_menu.add_command(label="Open", command=lambda: show("Open Selected"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Cut", command=lambda: show("Cut Selected"))
edit_menu.add_command(label="Copy", command=lambda: show("Copy Selected"))
edit_menu.add_command(label="Paste", command=lambda: show("Paste Selected"))

menubar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menubar)

mb = tk.Menubutton(root, text="Options", relief=tk.RAISED)
mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu

mb.menu.add_command(label="Option 1", command=lambda: show("Option 1"))
mb.menu.add_command(label="Option 2", command=lambda: show("Option 2"))
mb.pack(pady=20)

label = tk.Label(root, text="")
label.pack()

root.mainloop()