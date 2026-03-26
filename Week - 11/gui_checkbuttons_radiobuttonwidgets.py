import tkinter as tk

root = tk.Tk()
root.title("Checkbutton and Radiobutton Demo")
root.geometry("300x300")

def show_selection():
    selected = []
    if var1.get():
        selected.append("Python")
    if var2.get():
        selected.append("Java")
    if var3.get():
        selected.append("C++")
    
    lang = language.get()
    result.config(text=f"Selected: {', '.join(selected)} | Preferred: {lang}")

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

tk.Label(root, text="Select Languages:").pack()

tk.Checkbutton(root, text="Python", variable=var1).pack()
tk.Checkbutton(root, text="Java", variable=var2).pack()
tk.Checkbutton(root, text="C++", variable=var3).pack()

language = tk.StringVar(value="Python")

tk.Label(root, text="Choose Preferred Language:").pack()

tk.Radiobutton(root, text="Python", variable=language, value="Python").pack()
tk.Radiobutton(root, text="Java", variable=language, value="Java").pack()
tk.Radiobutton(root, text="C++", variable=language, value="C++").pack()

tk.Button(root, text="Submit", command=show_selection).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()