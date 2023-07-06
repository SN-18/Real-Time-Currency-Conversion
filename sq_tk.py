"""sql lite option"""
import tkinter as tk
from tkinter import ttk
import sqlite3

conn = sqlite3.connect("/database")
c = conn.cursor()

def get_value():
    c.execute("SELECT var FROM state WHERE id = 1")
    return c.fetchone()[0]

def change_value():
    c.execute("UPDATE state SET var = 1 - var WHERE id = 1")
    conn.commit()

def check_value():
    state = 'disabled' if get_value() == 1 else 'normal'
    button_1.config(state=state)
    button_2.config(state=state)
    root.after(100, check_value)

root = tk.Tk()

tab = ttk.Notebook(root)
tab.pack(fill='both', expand=1)

frame1 = ttk.Frame(tab)
frame2 = ttk.Frame(tab)
frame3 = ttk.Frame(tab)

tab.add(frame1, text='Mytab1')
tab.add(frame2, text='Mytab2')
tab.add(frame3, text='Mytab3')

button_1 = ttk.Button(frame1, text='Color change')
button_1.pack()

button_2 = ttk.Button(frame2, text='Generate text')
button_2.pack()

ttk.Button(frame3, text='Change value', command=change_value).pack()

check_value() # check value and update state of buttons periodically
root.mainloop()