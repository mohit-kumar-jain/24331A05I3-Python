import tkinter as tk

def show_message():
    name = entry.get()
    result_label.config(text=f"Hello {name}")

root = tk.Tk()
root.title("Hello Username")
root.geometry("300x200")

label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=show_message)
button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
