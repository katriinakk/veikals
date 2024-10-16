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
        self.master.geometry("800x700")
        self.master.configure(bg='lightblue')
        self.cart_list = []
        self.cart = ShoppingCart("Makarūni", 9.10, 4)
        self.prod = Produkti("Makarūni", 9.10, 4)


    def input_info_in(self):
        self.entry = Entry()
        self.entry.grid(row = 1, column = 2, columnspan=1, padx =10, pady=10 )
        self.entry2 = Entry()
        self.entry2.grid(row = 2, column = 2, columnspan=1, padx =10, pady=10 )
        self.entry3 = Entry()
        self.entry3.grid(row = 3, column = 2, columnspan=1, padx =10, pady=10 )
        self.removestuff = Entry()
        self.removestuff.grid(row = 4, column = 2, columnspan=1, padx =10, pady=10)


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
        self.teksts = Text(self.master, height = 20, width = 20)
        self.teksts.grid(row=1, column = 4, padx = 10, pady = 10, rowspan = 4)



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
        self.labelout.config(text = "       "+teksts+"       ")
        self.labelout.grid(row=6, column=2, padx =10, pady=10)

        #return teksts

    def products_in_my_cart(self):
        i = 0
        lengthh = len(self.cart_list)
        self.texts = ""
        while i < lengthh:         
            self.texts = self.texts+"\n"+str(i+1)+". produkts: "+self.cart_list[i].name+"\n"
            i=i+1
        self.teksts.insert(tk.END, "----------\n"+self.texts)



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
        
    def destroy_text(self):
        self.teksts.delete("1.0","end") 
        self.teksts = Text(self.master, height = 20, width = 20)
        self.teksts.grid(row=1, column = 4, padx = 10, pady = 10, rowspan = 4)  

    def input_stuff(self):
        self.button = Button(text="Ievadīt")
        self.button.grid(row=5, column= 2, padx =10, pady=10 )
        self.button.configure(command=lambda: [App.remove_process(self), App.the_maths(self), App.products_in_my_cart(self) ])
        self.button2 = Button(text = "notīrīt lauciņus")
        self.button2.grid(row=5, column= 1, padx =10, pady=10 )
        self.button2.configure(command=lambda: [self.entry.delete(0, tk.END), self.entry2.delete(0, tk.END), self.entry3.delete(0, tk.END)])
        self.button3 = Button(text = "Notīrīt izvadi")
        self.button3.grid(row=5, column= 4, padx =10, pady=10 )
        self.button3.configure(command=lambda: App.destroy_text(self))



    def image(self,master):
        self.image = Image.open("french.jpg")
        self.image = self.image.resize((350, 250))
        self.image2 = ImageTk.PhotoImage(self.image)
 
        self.labeli = tk.Label(master, image=self.image2)
        self.labeli.grid(row=7, column= 2, padx =10, pady=10 )
        self.chat = Label(text = "oui oui")
        self.chat.grid(row=7, column= 3, padx =10, pady=10)

    
logs = Tk()
a = App(master=logs)
a.input_info_in()
a.input_label()
#outputs = a.entry_input()
#a.the_maths(outputs)
a.input_stuff()
a.image(logs)


logs.mainloop()