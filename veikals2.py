class Produkti: #-------------->>Izveido galveno klasi
    def __init__(self, name, price, quantity):
        self.name = str(name)
        self.price = price
        self.quantity = quantity

    def get_total_price1(self):
        cena= round(self.price*self.quantity, 2) #-------------->>Atgriež preces galējo cenu (preces cena * daudzums) (un noapaļota)
        print(self.name+": ")
        print(cena)    
    
    
class ShoppingCart(Produkti):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.cart_list = [] #-------------->>Izveido grozu
        
    def add_product_to_cart(self, izvele):
        self.cart_list.append(izvele) #-------------->>Pievieno produktu grozam
        #print("Jūs pievienojāt preci: "+ izvele.name)

    def remove_product_from_cart(self, izvele):
        self.cart_list.remove(izvele) #-------------->>Noņem produktu no groza
        print("Jūs noņēmāt preci: "+ izvele.name)

    def get_product_list(self):
        return self.cart_list #-------------->>Izdrukā/dabūj visu groza sarakstu

    def get_total_price(self, izvele):
        #print(self.cart_list[0].name)
        print("Summa: ")
        total = 0
        i = 0
        
        while i < len(izvele): #-------->>Ievieš ciklu (strādā, līdz tas ir izgājis cauri visiem groza elementiem)
            total = total + self.cart_list[i].price*self.cart_list[i].quantity #------->>izrēķina visu groza summu
            i = i+1
        print(round(total, 2)) #-------------->>Atgriež kopējo summu, kas jāmaksā (noapaļota līdz 2 cipariem aiz komata)


class SystemUser:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.user_info = ["MF_DOOM", "D00msD4y", "mf_doom@gmail.com"]  #-------------->>Piešķir lietotājam atribūtus

    def set_user_info(self, info):
        self.user_info[0] = info.username #-------------->>Lietotājs nomaina informāciju
        self.user_info[1] = info.password
        self.user_info[2] = info.email

    def get_user_info(self):
        return "Lietotājvārds: "+self.user_info[0]+" ; Parole: "+self.user_info[1]+" ; E-pasts: "+self.user_info[2]


# ↓↓↓↓↓  izveido preču sarakstu
siers1 = ShoppingCart("Zilais siers", 4.99, 43)

siers = Produkti("Zilais siers", 4.99, 43)
maize = Produkti("Bagete", 1.99, 67)
deserts = Produkti("Makarūni", 9.10, 4)

siers.get_total_price1()
maize.get_total_price1()
deserts.get_total_price1()


# ↓↓↓↓↓ ievieto preces grozā
siers1.add_product_to_cart(siers)
siers1.add_product_to_cart(maize)
siers1.add_product_to_cart(deserts)

# ↓↓↓↓↓ noņem preci no groza
siers1.remove_product_from_cart(deserts)


# ↓↓↓↓↓ dabūjam groza sarakstu
products =siers1.get_product_list()

#print(len(products))
#print(products[0].name)

# ↓↓↓↓↓ izrēķinam visa groza sarakstu cenu
siers1.get_total_price(products)

# ↓↓↓↓↓ izveidojam jaunu lietotāju
liet = SystemUser("MIMI", "w0rmSs", "mimi@gmail.com")

# ↓↓↓↓↓ izvietojam informāciju par lietotāju ar jauno info
liet.set_user_info(liet)

# ↓↓↓↓↓ izprintē datus
print(liet.get_user_info())

