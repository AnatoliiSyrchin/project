import tkinter as tk


class Window:

    def __init__(self, main):
        self.root = tk.Tk()
        self.root.title = 'Storage'
        self.main = main

        self.main_storage = tk.Label(self.root, text="Главный склад")
        self.main_storage_count = tk.Label(self.root, text=self.main.count())
        self.printer_button = tk.Button(self.root, text='добавить принтер', command=self.printer_button)
        self.scaner_button = tk.Button(self.root, text='добавить сканер', command=self.scaner_button)
        self.copier_button = tk.Button(self.root, text='добавить ксерокс', command=self.copier_button)

    def draw_widgets(self):
        self.main_storage.grid(row=0, column=0)
        self.main_storage_count.grid(row=1, column=0)
        self.printer_button.grid(row=2, column=0)
        self.scaner_button.grid(row=3, column=0)
        self.copier_button.grid(row=4, column=0)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def printer_button(self):
        self.main.accept('Printer')
        self.main_storage_count.config(text=self.main.count())
        self.root.update()

    def scaner_button(self):
        self.main.accept('Scaner')
        self.main_storage_count.config(text=self.main.count())
        self.root.update()

    def copier_button(self):
        self.main.accept('Copier')
        self.main_storage_count.config(text=self.main.count())
        self.root.update()

# if __name__ == '__main__':
#     window = Window()
#     window.run()
