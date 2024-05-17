import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output_label.config(text="Result: " + str(result))
    except Exception as e:
        output_label.config(text="Error: " + str(e))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget for input
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for numbers and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=7, command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=button, width=7, command=lambda b=button: entry.insert(tk.END, b)).grid(row=row, column=col, padx=5, pady=5)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create a label to display the result
output_label = tk.Label(root, text="")
output_label.grid(row=row, column=0, columnspan=4)

root.mainloop()
