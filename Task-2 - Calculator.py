import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")

# Set window size
root.geometry("400x400")

# Global variable to store the input and result
expression = ""

# Function to update the input field
def update_expression(number):
    global expression
    expression += str(number)
    input_text.set(expression)

# Function to evaluate the expression
def evaluate_expression():
    try:
        global expression
        result = str(eval(expression))  # Evaluate the expression
        input_text.set(result)
        expression = result  # Reset the expression to the result for further calculations
    except:
        messagebox.showerror("Error", "Invalid Expression")
        expression = ""

# Function to clear the input field
def clear_input():
    global expression
    expression = ""
    input_text.set("")

# Input field setup
input_text = tk.StringVar()
input_field = tk.Entry(root, textvariable=input_text, font=('Arial', 18), bd=10, insertwidth=4, width=14, borderwidth=4)
input_field.grid(row=0, column=0, columnspan=4, ipadx=8)

# Create buttons and link them to the functions
button_1 = tk.Button(root, text="1", padx=20, pady=20, font=('Arial', 18), command=lambda: update_expression(1))
button_1.grid(row=1, column=0)

button_2 = tk.Button(root, text="2", padx=20, pady=20, font=('Arial', 18), command=lambda: update_expression(2))
button_2.grid(row=1, column=1)

button_3 = tk.Button(root, text="3", padx=20, pady=20, font=('Arial', 18), command=lambda: update_expression(3))
button_3.grid(row=1, column=2)

button_4 = tk.Button(root, text="4", padx=20, pady=20, font=('Arial', 18), command=lambda: update_expression(4))
button_4.grid(row=2, column=0)

button_5 = tk.Button(root, text="5", padx=20, pady=20, font=('Arial', 18), command=lambda: update_expression(5))
button_5.grid(row=2, column=1)

button_6 = tk.Button(root, text="6", padx=20, pady=20, font=('Arial', 18), command=lambda: update_expression(6))
button_6.grid(row=2, column=2)

button_7 = tk.Button(root, text="7", padx=20, pady=20, font=('Arial', 18), command=lambda: update_expression(7))
button_7.grid(row=3, column=0)

button_8 = tk.Button(root, text="8", padx=20, pady=20, font=('Arial', 18), command=lambda: update_expression(8))
button_8.grid(row=3, column=1)

button_9 = tk.Button(root, text="9", padx=20, pady=20, font=('Arial', 18), command=lambda: update_expression(9))
button_9.grid(row=3, column=2)

button_0 = tk.Button(root, text="0", padx=20, pady=20, font=('Arial', 18), command=lambda: update_expression(0))
button_0.grid(row=4, column=0)

button_add = tk.Button(root, text="+", padx=20, pady=20, font=('Arial', 18), command=lambda: update_expression('+'))
button_add.grid(row=1, column=3)

button_subtract = tk.Button(root, text="-", padx=20, pady=20, font=('Arial', 18), command=lambda: update_expression('-'))
button_subtract.grid(row=2, column=3)

button_multiply = tk.Button(root, text="*", padx=20, pady=20, font=('Arial', 18), command=lambda: update_expression('*'))
button_multiply.grid(row=3, column=3)

button_divide = tk.Button(root, text="/", padx=20, pady=20, font=('Arial', 18), command=lambda: update_expression('/'))
button_divide.grid(row=4, column=3)

button_clear = tk.Button(root, text="C", padx=20, pady=20, font=('Arial', 18), command=clear_input)
button_clear.grid(row=4, column=1)

button_equals = tk.Button(root, text="=", padx=20, pady=20, font=('Arial', 18), command=evaluate_expression)
button_equals.grid(row=4, column=2)

# Start the Tkinter event loop
root.mainloop()
