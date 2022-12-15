import tkinter as tk
import json

win = tk.Tk()
win.geometry("450x250")

lab = tk.Label(text=f" Введіть назву фірми ", width=15, height=10)
lab.grid(padx=4, pady=4)


def action():
    build_corp = '{"Build corps": "450", "Pioners": "260", "DM Development":"547","Woodridge Capital Partners":"428"}'

    build = json.loads(build_corp)

    with open('build_company.txt', 'w') as json_file:
        json.dump(build, json_file)

        ss = entry.get()

        if ss == 'Build corps':
            entry.insert(
                tk.END, build["Build corps"] + '' + ' чисельність робітників')

        if ss == 'Pioners':
            entry.insert(tk.END, build["Pioners"] +
                         '' + ' чисельність робітників')

        if ss == 'DM Development':
            entry.insert(
                tk.END, build["DM Development"] + '' + ' чисельність робітників')

        if ss == 'Woodridge Capital Partners':
            entry.insert(
                tk.END, build["Woodridge Capital Partners"] + '' + ' чисельність робітників')


button = tk.Button(text="ПУСК",  width=30,  height=10,
                   background="gray", foreground="black", command=action)
button.grid(padx=3, pady=3)

entry = tk.Entry(foreground="black", background="white", width=50)
entry.grid(padx=2, pady=2)

win.mainloop()
