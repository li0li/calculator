import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.resizable(False, False) 
        self.expression = ""
        self.text_input = tk.StringVar()
        self.create_widgets()
        self.create_menu()

        
    def create_widgets(self):
        # Поле для ввода
        entry = tk.Entry(self.root, textvariable=self.text_input, font=('arial', 24, 'bold'), bd=20, insertwidth=4,
                         width=14, borderwidth=4, bg="#ffffff", justify='right')
        entry.grid(row=0, column=0, columnspan=4)

        # Кнопки
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+',
            'DEL', '='
        ]

        colors = {
            'numbers': '#b3d1ff',
            'operations': '#80bfff',
            'clear': '#3399ff',
            'delete': '#1a75ff',
            'equal': '#1a75ff',
            'dot': '#80bfff'
        }

        row = 1
        col = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            if button == "=":
                tk.Button(self.root, text=button, padx=20, pady=20, font=('arial', 20, 'bold'),
                          bg=colors['equal'], fg="white", command=action).grid(row=row, column=col, columnspan=2, sticky="nsew")
                col += 1
            elif button == "DEL":
                tk.Button(self.root, text=button, padx=20, pady=20, font=('arial', 20, 'bold'),
                          bg=colors['delete'], fg="white", command=action).grid(row=row, column=col, columnspan=2, sticky="nsew")
                col += 1
            elif button in "0123456789":
                tk.Button(self.root, text=button, padx=20, pady=20, font=('arial', 20, 'bold'),
                          bg=colors['numbers'], command=action).grid(row=row, column=col, sticky="nsew")
            elif button in "/*-+":
                tk.Button(self.root, text=button, padx=20, pady=20, font=('arial', 20, 'bold'),
                          bg=colors['operations'], command=action).grid(row=row, column=col, sticky="nsew")
            elif button == "C":
                tk.Button(self.root, text=button, padx=20, pady=20, font=('arial', 20, 'bold'),
                          bg=colors['clear'], fg="white", command=action).grid(row=row, column=col, sticky="nsew")
            else:  
                tk.Button(self.root, text=button, padx=20, pady=20, font=('arial', 20, 'bold'),
                          bg=colors['dot'], command=action).grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Настройка одинакового размера кнопок
        for i in range(6):  
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def create_menu(self):
        # Создание меню
        menubar = tk.Menu(self.root)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="О калькуляторе", command=self.show_help)
        menubar.add_cascade(label="Справка", menu=helpmenu)
        self.root.config(menu=menubar)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == 'DEL':
            self.expression = self.expression[:-1]
        elif char == '=':
            try:
                result = eval(self.expression)
                self.expression = str(round(result, 10))  
            except Exception as e:
                messagebox.showerror("Ошибка", "Неверное выражение")
                self.expression = ""
        else:
            self.expression += str(char)
        self.text_input.set(self.expression)

    def show_help(self):
        help_text = (
            "Калькулятор поддерживает следующие операции:\n"
            "- Сложение (+)\n"
            "- Вычитание (-)\n"
            "- Умножение (*)\n"
            "- Деление (/)\n"
            "Для ввода дробных чисел используйте точку (.).\n"
            "Результаты округляются до 10 знаков после запятой."
        )
        messagebox.showinfo("О калькуляторе", help_text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
