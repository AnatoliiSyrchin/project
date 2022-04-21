import tkinter as tk
from tkinter import messagebox


class Window:
    def __init__(self, main, office):
        self.root = tk.Tk()
        self.root.title = 'Storage'
        self.main = main
        self.office = office
        self.root.columnconfigure([0, 1], minsize=150)

        self.frame_main = tk.Frame(self.root, relief=tk.RAISED, borderwidth=2)
        self.main_storage = tk.Label(self.frame_main, text="Main storage")
        self.main_storage_count = tk.Label(self.frame_main, text=self.main.count())
        self.main_printer_button = tk.Button(self.frame_main, text='Add printer', command=self.main_printer_button)
        self.main_scanner_button = tk.Button(self.frame_main, text='Add scanner', command=self.main_scanner_button)
        self.main_copier_button = tk.Button(self.frame_main, text='Add copier', command=self.main_copier_button)
        self.main_storage_all = tk.Label(self.frame_main, text='')

        self.frame_main_move = tk.Frame(self.root, relief=tk.RAISED, borderwidth=2)
        self.main_move = tk.Label(self.frame_main_move, text='Move to office')
        self.main_printers_entry = tk.Entry(self.frame_main_move, width=5)
        self.main_printers_entry.insert(0, '0')
        self.main_move_printer = tk.Label(self.frame_main_move, text='printers')
        self.main_scanners_entry = tk.Entry(self.frame_main_move, width=5)
        self.main_scanners_entry.insert(0, '0')
        self.main_move_scanners = tk.Label(self.frame_main_move, text='scanners')
        self.main_copiers_entry = tk.Entry(self.frame_main_move, width=5)
        self.main_copiers_entry.insert(0, '0')
        self.main_move_copiers = tk.Label(self.frame_main_move, text='copiers')
        self.main_move_button = tk.Button(self.frame_main_move, text ='move to office', command=self.move_button)

        self.frame_office = tk.Frame(self.root, relief=tk.RAISED, borderwidth=2)
        self.office_storage = tk.Label(self.frame_office, text="Office storage")
        self.office_storage_count = tk.Label(self.frame_office, text=self.office.count())
        self.office_storage_all = tk.Label(self.frame_office, text='')

        self.frame_office_move = tk.Frame(self.root, relief=tk.RAISED, borderwidth=2)
        self.office_move = tk.Label(self.frame_office_move, text='Return to main')
        self.office_printers_entry = tk.Entry(self.frame_office_move, width=5)
        self.office_printers_entry.insert(0, '0')
        self.office_move_printer = tk.Label(self.frame_office_move, text='printers')
        self.office_scanners_entry = tk.Entry(self.frame_office_move, width=5)
        self.office_scanners_entry.insert(0, '0')
        self.office_move_scanners = tk.Label(self.frame_office_move, text='scanners')
        self.office_copiers_entry = tk.Entry(self.frame_office_move, width=5)
        self.office_copiers_entry.insert(0, '0')
        self.office_move_copiers = tk.Label(self.frame_office_move, text='copiers')
        self.office_move_button = tk.Button(self.frame_office_move, text ='return to main', command=self.return_button)

    # прорисовка всего
    def draw_widgets(self):
        self.frame_main.grid(row=0, column=0, padx=20, pady=5, sticky="nwse")
        self.main_storage.grid(row=0, column=0)
        self.main_storage_count.grid(row=1, column=0)
        self.main_printer_button.grid(row=2, column=0)
        self.main_scanner_button.grid(row=3, column=0)
        self.main_copier_button.grid(row=4, column=0)
        self.main_storage_all.grid(row=5, column=0)
       
        self.frame_main_move.grid(row=1, column=0, padx=20, pady=5, sticky="nwse")
        self.main_move.grid(row=0, column=0)
        self.main_printers_entry.grid(row=1, column=0)
        self.main_move_printer.grid(row=1, column=1)
        self.main_scanners_entry.grid(row=2, column=0)
        self.main_move_scanners.grid(row=2, column=1)
        self.main_copiers_entry.grid(row=3, column=0)
        self.main_move_copiers.grid(row=3, column=1)
        self.main_move_button.grid(row=4, column=0)

        self.frame_office.grid(row=0, column=1, padx=20, pady=5, sticky="nwse")
        self.office_storage.grid(row=0, column=1)
        self.office_storage_count.grid(row=1, column=1)
        self.office_storage_all.grid(row=5, column=1)

        self.frame_office_move.grid(row=1, column=1, padx=20, pady=5, sticky="nwse")
        self.office_move.grid(row=0, column=0)
        self.office_printers_entry.grid(row=1, column=0)
        self.office_move_printer.grid(row=1, column=1)
        self.office_scanners_entry.grid(row=2, column=0)
        self.office_move_scanners.grid(row=2, column=1)
        self.office_copiers_entry.grid(row=3, column=0)
        self.office_move_copiers.grid(row=3, column=1)
        self.office_move_button.grid(row=4, column=0)

    # главный запуск
    def run(self):
        self.draw_widgets()
        self.root.mainloop()
        
    # функции для кнопок
    def main_printer_button(self):
        self.main.random_accept('Printer')
        self.main_update_storage()

    def main_scanner_button(self):
        self.main.random_accept('Scanner')
        self.main_update_storage()

    def main_copier_button(self):
        self.main.random_accept('Copier')
        self.main_update_storage()

    def office_printer_button(self):
        self.office.random_accept('Printer')
        self.office_update_storage()

    def office_scanner_button(self):
        self.office.random_accept('Scanner')
        self.office_update_storage()

    def office_copier_button(self):
        self.office.random_accept('Copier')
        self.office_update_storage()

    def move_button(self):
        quantity_printers = self.main_printers_entry.get()
        quantity_scanners = self.main_scanners_entry.get()
        quantity_copiers = self.main_copiers_entry.get()
        result = self.main.move_to(self.office, quantity_printers, quantity_scanners, quantity_copiers)
        self.main_update_storage()
        self.office_update_storage()
        messagebox.showinfo(title='Moved', message=result)
            
    def return_button(self):
        quantity_printers = self.office_printers_entry.get()
        quantity_scanners = self.office_scanners_entry.get()
        quantity_copiers = self.office_copiers_entry.get()
        result = self.office.move_to(self.main, quantity_printers, quantity_scanners, quantity_copiers)
        self.main_update_storage()
        self.office_update_storage()
        messagebox.showinfo(title='Moved', message=result)

            
    # обновление после нажатия кнопок
    def main_update_storage(self):
        self.main_storage_count.config(text=self.main.count())
        self.main_storage_all.config(text=f'Full list:\n {self.main}')

    def office_update_storage(self):
        self.office_storage_count.config(text=self.office.count())
        self.office_storage_all.config(text=f'Full list:\n {self.office}')
