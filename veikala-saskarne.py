import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from veikals2 import ShoppingCart
from veikals2 import Produkti
from tkinter import*

class App():
    def __init__(self, master):
        #Toplevel.__init__(self, master)
        self.master = master
        self.master.title("Iepirkumu grozs")
        self.master.geometry("400x550")
        self.cart_list = []
        self.cart = ShoppingCart("Makarūni", 9.10, 4)
        self.prod = Produkti("Makarūni", 9.10, 4)
        self.product = 0


    def input_info_in(self):
        self.entry = Entry()
        self.entry.grid(row = 1, column = 2, columnspan=4, padx =10, pady=10 )
        self.entry2 = Entry()
        self.entry2.grid(row = 2, column = 2, columnspan=4, padx =10, pady=10 )
        self.entry3 = Entry()
        self.entry3.grid(row = 3, column = 2, columnspan=4, padx =10, pady=10 )

    def input_label(self):
        self.label = Label(text= "Produkts:")
        self.label.grid(row=1, column=1, padx =10, pady=10)
        #self.label.configure(command=self.cart.add_product_to_cart(self.entry.get()))
        self.label2 = Label(text= "Cena:")
        self.label2.grid(row=2, column=1, padx =10, pady=10)
        #self.label.configure(command=self.cart.add_product_to_cart(self.entry2.get()))
        self.label3 = Label(text= "Daudzums:")
        self.label3.grid(row=3, column=1, padx =10, pady=10)
        #self.label.configure(command=self.cart.add_product_to_cart(self.entry3.get()))

    def entry_input(self):
        self.product = ShoppingCart(self.entry.get(), self.entry2.get(), self.entry3.get())
        return self.product

    def the_maths(self, aa):
        self.cart.add_product_to_cart(aa)
        lengthof = len(self.cart_list)
        result = self.cart.get_total_price1(aa)
        teksts = "Produktu tipu skaits: "+str(lengthof)+"; Kopējā (groza) summa: "+str(result)

        self.labelout = Label()

    def input_stuff(self):
        self.button = Button(text="Ievadīt")
        self.button.grid(row=4, column= 2, padx =10, pady=10 )
        self.button.configure(command=)

    


    




logs = Tk()
a = App(master=logs)
a.input_info_in()
a.input_label()
outputs = a.entry_input
a.the_maths(outputs)
a.input_stuff()



logs.mainloop()