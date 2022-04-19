from tkinter import *
import collections
import pickle
from functools import partial


class CrudMain:

    def __init__(self, master, cust):
        self.master = master
        self.customer_list = cust

        self.cust_frame = Frame(self.master)
        frame = Frame(self.master)
        frame.master.title("Contact List Editor")

        self.label_1 = Label(frame, text='Contact list').pack(side=LEFT)

        self.update_customers()

        self.add_button = Button(frame, text='Add Contact', command=self.add_contact_window)

        self.add_button.pack(anchor='sw')
        frame.pack(anchor='nw')
        self.cust_frame.pack(anchor='w')

    def update_customers(self):
        for widget in self.cust_frame.winfo_children():
            widget.destroy()

        r = 0
        for key in self.customer_list:
            Button(self.cust_frame, text=key, command=partial(self.cust_info, key)).grid(row=1, column=r)
            r += 1

    def add_contact_window(self):
        AddWindow(self.master, self, self.customer_list)

    def cust_info(self, key):
        CustInfo(self.master, self.customer_list, key)


class CustInfo:

    def __init__(self, master, cust, key):
        self.master = master
        self.cust = cust[key]
        self.info_window = Toplevel()
        self.info_window.title("Contact Information")

        Label(self.info_window, text=self.cust['first_name']).pack()
        Label(self.info_window, text=self.cust['last_name']).pack()
        Label(self.info_window, text=self.cust['email']).pack()
        Label(self.info_window, text=self.cust['address']).pack()
        Label(self.info_window, text=self.cust['phone']).pack()

        Button(self.info_window, text='Close', command=self.info_window.destroy).pack(anchor='s')


class AddWindow:

    def __init__(self, master, main_window, cust):
        self.master = master
        self.cust = cust
        self.main_window = main_window

        self.add_window = Toplevel()
        self.add_window.title("Add Contact")
        Label(self.add_window, text='First Name: ').grid(row=0, column=0)
        Label(self.add_window, text='Last Name: ').grid(row=1, column=0)
        Label(self.add_window, text='Email Address: ').grid(row=2, column=0)
        Label(self.add_window, text='Living Address: ').grid(row=3, column=0)
        Label(self.add_window, text='Phone Number:').grid(row=4, column=0)

        self.first_name = StringVar()
        self.last_name = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.phone = StringVar()

        Button(self.add_window, text="Submit", command=lambda: self.save(self.cust)).grid(row=5, column=0)
        Button(self.add_window, text='Cancel', command=self.add_window.destroy).grid(row=5, column=1)

        Entry(self.add_window, textvariable=self.first_name).grid(row=0, column=1)
        Entry(self.add_window, textvariable=self.last_name).grid(row=1, column=1)
        Entry(self.add_window, textvariable=self.email).grid(row=2, column=1)
        Entry(self.add_window, textvariable=self.address).grid(row=3, column=1)
        Entry(self.add_window, textvariable=self.phone).grid(row=4, column=1)

    def save(self, customers):
        name = str(self.first_name.get())
        last = str(self.last_name.get())
        email = str(self.email.get())
        address = str(self.address.get())
        phone = str(self.phone.get())

        save = {'first_name': name, 'last_name': last, 'email': email, 'address': address, 'phone': phone}
        key = save['first_name']
        customers[key] = save
        pickle.dump(customers, open('customer_file.dat', 'wb'))
        # messagebox.showinfo("Status", "Information saved successfully!")
        self.add_window.destroy()
        self.main_window.update_customers()


def main():
    try:
        input_file = open("customer_file.dat", "rb")
        customers = pickle.load(input_file)
    except (FileNotFoundError, IOError):
        customers = collections.OrderedDict()

    root = Tk()
    CrudMain(root, customers)
    root.mainloop()

main()