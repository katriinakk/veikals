class Produkti: #-------------->>Izveido galveno klasi
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(price, quantity, name):
        #print("Prece: {}; Cena: {}; Daudzums: {}").format(name, price, quantity)
        return round(price*quantity, 2) #-------------->>Atgriež preces galējo cenu (preces cena * daudzums) (un noapaļota)
    
    
    
class ShoppingCart(Produkti):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.cart_list = [] #-------------->>Izveido grozu
        
    def add_product_to_cart(self, izvele):
        self.cart_list.append(izvele) #-------------->>Pievieno produktu grozam
        print("Jūs pievienojāt preci: "+ izvele.name)

    def remove_product_from_cart(self, izvele):
        self.cart_list.remove(izvele) #-------------->>Noņem produktu no groza
        print("Jūs noņēmāt preci: "+ izvele.name)

    def get_product_list(self):
        return self.cart_list #-------------->>Izdrukā/dabūj visu groza sarakstu

    def get_total_price(self, izvele):
        #print(self.cart_list[0].name)
        total = 0
        i = 0
        
        while i < len(izvele): #-------->>Ievieš ciklu (strādā, līdz tas ir izgājis cauri visiem groza elementiem)
            total = total + self.cart_list[i].price*self.cart_list[i].quantity #------->>izrēķina visu groza summu
            i = i+1
        print(round(total, 2)) #-------------->>Atgriež saraksta summu, kas jāmaksā (noapaļota līdz 2 cipariem aiz komata)


# ↓↓↓↓↓  izveido preču sarakstu
siers = ShoppingCart("Zilais siers", 4.99, 43)
maize = ShoppingCart("Bagete", 1.99, 67)
deserts = ShoppingCart("Makarūni", 9.10, 4)

print(Produkti.get_total_price(siers.price, siers.quantity, siers.name))
print(Produkti.get_total_price(maize.price, maize.quantity, maize.name))
print(Produkti.get_total_price(deserts.price, deserts.quantity, deserts.name))

# ↓↓↓↓↓ ievieto preces grozā
siers.add_product_to_cart(siers)
siers.add_product_to_cart(maize)
siers.add_product_to_cart(deserts)

# ↓↓↓↓↓ noņem preci no groza
siers.remove_product_from_cart(deserts)


# ↓↓↓↓↓ dabūjam groza sarakstu
products =siers.get_product_list()

#print(len(products))
#print(products[0].name)

# ↓↓↓↓↓ izrēķinam visa groza sarakstu cenu
siers.get_total_price(products)