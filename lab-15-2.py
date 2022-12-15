import tkinter as tk

win = tk.Tk()
win.geometry("450x250")


def action():
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZqwertyuiopasdfghjklzxcvbnm'
    ss = entry.get()
    a = -1
    b = 0
    for i in range(54):
        a += 1
        x = ss.count(abc[a])
        b += x
        entry.insert(tk.END, int(b))


entry = tk.Entry(foreground="black", background="white", width=50)
entry.grid(padx=2, pady=2)

button = tk.Button(text="ПУСК",  width=30,  height=10,
                   background="gray", foreground="black", command=action)
button.grid(padx=3, pady=3)

win.mainloop()
