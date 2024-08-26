import tkinter as tk
def evaluate(event):
    resultlabel.config(text=str(eval(entry.get())))
    root = tk.Tk()
    root.title("Calculadora Simples")
    entry = tk.Entry(root)
    entry.bind("<Return>",evaluate)
    entry.pack()
    resultlabel = tk.label(root, text="")
    resultlabel.pack()
    root.geometry("250x80")
    root.mainloop()