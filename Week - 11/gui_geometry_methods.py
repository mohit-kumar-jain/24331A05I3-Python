import tkinter as tk

root = tk.Tk()
root.title("Geometry Managers Demo")
root.geometry("400x300")

label1 = tk.Label(root, text="Hello Everyone", bg="lightblue")
label1.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

label2 = tk.Label(frame, text="Mohit ", bg="lightgreen")
label3 = tk.Label(frame, text="here", bg="lightgreen")

label2.grid(row=0, column=0, padx=5, pady=5)
label3.grid(row=0, column=1, padx=5, pady=5)

label4 = tk.Label(root, text="Bye!!", bg="red",foreground="white")
label4.place(x=150, y=200)

root.mainloop()