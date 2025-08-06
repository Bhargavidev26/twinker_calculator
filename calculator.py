import tkinter as tk

def click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(event.widget["text"]))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    btn = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18))
    btn.grid(row=row_val, column=col_val)
    
    if button == "=":
        btn.bind("<Button-1>", lambda e: calculate())
    else:
        btn.bind("<Button-1>", click)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

clear_btn = tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 18), command=clear)
clear_btn.grid(row=row_val, column=0, columnspan=4, sticky="we")

root.mainloop()
