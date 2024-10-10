import tkinter as tk
from tkinter import messagebox
from veikals2 import ShoppingCart
from veikals2 import Produkti
from tkinter import*
from PIL import Image, ImageTk


class App():
    def __init__(self, master):
        #Toplevel.__init__(self, master)
        self.master = master
        self.master.title("Iepirkumu grozs")
        self.master.geometry("800x550")
        self.cart_list = []
        self.cart = ShoppingCart("Makarūni", 9.10, 4)
        self.prod = Produkti("Makarūni", 9.10, 4)


    def input_info_in(self):
        self.entry = Entry()
        self.entry.grid(row = 1, column = 2, columnspan=6, padx =10, pady=10 )
        self.entry2 = Entry()
        self.entry2.grid(row = 2, column = 2, columnspan=6, padx =10, pady=10 )
        self.entry3 = Entry()
        self.entry3.grid(row = 3, column = 2, columnspan=6, padx =10, pady=10 )
        self.removestuff = Entry()
        self.removestuff.grid(row = 4, column = 2, columnspan=6, padx =10, pady=10)


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
        self.labelremove = Label(text = "Ievadiet produkta numuru,\nko vēlaties noņemt:")
        self.labelremove.grid(row = 4, column =1, padx =10, pady=10)



#    def remove_stuff(self):
#        self.buttonremove = Button(text="Noņemt")
#        self.buttonremove.grid(row = 6, column = 2, columnspan=4, padx =10, pady=10)
#        self.buttonremove.configure(command=lambda: App.remove_process(self))



    def the_maths(self):
        try:
            teksts = ""
            self.product = Produkti(self.entry.get(), float(self.entry2.get()), int(self.entry3.get()))
            self.cart_list.append(self.product)

            lengthof = len(self.cart_list)
            total = 0
            i = 0
        
            while i < lengthof:
                total = total + self.cart_list[i].price*self.cart_list[i].quantity
                i = i+1

            teksts = "Produktu skaits: "+str(lengthof)+"; Kopējā (groza) summa: "+str(total)

            
        except: 
            teksts = ""
            lengthof = len(self.cart_list)
            total = 0
            i = 0
        
            while i < lengthof:
                total = total + self.cart_list[i].price*self.cart_list[i].quantity
                i = i+1

            teksts = "Produktu skaits: "+str(lengthof)+"; Kopējā (groza) summa: "+str(int(total))

    
        self.labelout = Label(text = "       "+teksts+"       ", bg = 'light gray')
        self.labelout.grid(row=6, column=2, padx =10, pady=10)

        #return teksts

    def products_in_my_cart(self):
        i = 0
        lengthh = len(self.cart_list)
        texts = " "
        while i < lengthh:         
            texts = str(i+1)+". produkts: "+self.cart_list[i].name
            i=i+1

        self.labelis = Label(text = texts, bg = 'light gray')
        self.labelis.grid(row=i, column= 3, padx =10, pady=10)

    def remove_process(self):

        self.num = self.removestuff.get()
        print(self.num)
        #self.num = int(self.num)
        try:
            x = self.cart_list.pop(int(self.num) -1)
            self.cart_list.remove(x)
            print(self.num)
        except:
            pass   

    def input_stuff(self):
        self.button = Button(text="Ievadīt")
        self.button.grid(row=5, column= 2, padx =10, pady=10 )
        self.button.configure(command=lambda: [App.remove_process(self), App.the_maths(self), App.products_in_my_cart(self) ])

    def image(self,master):
        self.image = Image.open("french.jpg")
        self.image = self.image.resize((350, 250))
        self.image2 = ImageTk.PhotoImage(self.image)
 
        self.labeli = tk.Label(master, image=self.image2)
        self.labeli.grid(row=7, column= 2, padx =10, pady=10 )

    
logs = Tk()
a = App(master=logs)
a.input_info_in()
a.input_label()
#outputs = a.entry_input()
#a.the_maths(outputs)
a.input_stuff()
a.image(logs)


logs.mainloop()