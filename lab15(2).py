import tkinter as tk
from tkinter import messagebox
import numpy as np

def solve_system():
    try:
        a1 = float(entry_a1.get() or 0)
        b1 = float(entry_b1.get() or 0)
        c1 = float(entry_c1.get() or 0)
        d1 = float(entry_d1.get() or 0)
        
        a2 = float(entry_a2.get() or 0)
        b2 = float(entry_b2.get() or 0)
        c2 = float(entry_c2.get() or 0)
        d2 = float(entry_d2.get() or 0)
        
        a3 = float(entry_a3.get() or 0)
        b3 = float(entry_b3.get() or 0)
        c3 = float(entry_c3.get() or 0)
        d3 = float(entry_d3.get() or 0)

        A = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
        B = np.array([d1, d2, d3])

        solution = np.linalg.solve(A, B)
        
        result_text.set(f"x = {solution[0]:.2f}, y = {solution[1]:.2f}, z = {solution[2]:.2f}")
    except ValueError:
        messagebox.showerror("Помилка", "Переконайтеся, що всі поля містять числа.")
    except np.linalg.LinAlgError:
        messagebox.showerror("Помилка", "Система рівнянь не має розв'язків або має нескінченну кількість розв'язків.")

root = tk.Tk()
root.title("Система лінійних рівнянь")
root.geometry("400x300")

labels = ['a1', 'b1', 'c1', 'd1', 'a2', 'b2', 'c2', 'd2', 'a3', 'b3', 'c3', 'd3']
entries = {}
for i, label in enumerate(labels):
    row = i // 4
    col = i % 4
    tk.Label(root, text=label).grid(row=row, column=col*2, padx=5, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=row, column=col*2+1, padx=5, pady=5)
    entries[label] = entry

entry_a1, entry_b1, entry_c1, entry_d1 = entries['a1'], entries['b1'], entries['c1'], entries['d1']
entry_a2, entry_b2, entry_c2, entry_d2 = entries['a2'], entries['b2'], entries['c2'], entries['d2']
entry_a3, entry_b3, entry_c3, entry_d3 = entries['a3'], entries['b3'], entries['c3'], entries['d3']

solve_button = tk.Button(root, text="Розв'язати", command=solve_system)
solve_button.grid(row=4, column=1, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.grid(row=5, column=0, columnspan=4)

root.mainloop()

