import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, text_content)

root = tk.Tk()
root.title("Відкриття файлу")
root.geometry("600x350")
root.configure(bg='blue')

open_button = tk.Button(root, text="Відкрити файл", command=open_file)
open_button.place(x=250, y=10)

text_widget = tk.Text(root, wrap='word')
text_widget.place(x=10, y=50, width=580, height=290)

root.mainloop()
