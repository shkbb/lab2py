import tkinter as tk
from tkinter import messagebox

# Функція конвертації
def convert_temperature():
    try:
        celsius = float(entry.get())
        fahrenheit = celsius * 9/5 + 32
        result_label.config(text=f"Температура у Фаренгейтах: {fahrenheit:.2f}°F")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть числове значення.")

# Створення головного вікна
root = tk.Tk()
root.title("Конвертер температури")

# Поле введення
tk.Label(root, text="Введіть температуру в Цельсіях:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

# Кнопка для запуску конвертації
convert_button = tk.Button(root, text="Конвертувати", command=convert_temperature)
convert_button.pack(pady=5)

# Мітка для відображення результату
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Запуск головного циклу Tkinter
root.mainloop()
