class Produkti:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price*self.quantity

class ShoppingCart(Produkti):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    izvele = [Produkti("Zilais siers", 4.99, 45), Produkti("Bagete", 2.33, 67)]

    def add_product_to_cart(izvele):

        viens = input("Vai Jūs vēlaties ieveitot preci '"+ izvele[0].name +"' grozā?")
        divi = input("Vai Jūs vēlaties ieveitot preci '"+ izvele[1].name +"' grozā?")
        izvele = []
        if viens == "jā":
            izvele.extend(izvele[0])
        if divi == "jā":
            izvele.extend(izvele[1])

        
    def remove_product_from_cart(izvele):

        jaut = input("Vai Jūs vēlaties veikt labojumus (noņemt preci no groza)?")

        if jaut == "jā":
            ok = input("Kuru produktu Jūs vēlaties noņemt? (1 - pirmo, 2 - otro, 3 - abus)")
            if ok == 1:
                izvele.remove(izvele[0])
            elif ok == 2:
                izvele.remove(izvele[1])
            elif ok == 3:
                izvele.remove(izvele[1])
                izvele.remove(izvele[0])
            else:
                return("Nepareizi ievadīti dati")
        else:
            pass

    def get_total_price(izvele):
        return izvele[0].price*izvele[0].quantity+izvele[1].price*izvele[1].quantity

izvele = [Produkti("Zilais siers", 4.99, 45), Produkti("Bagete", 2.33, 67)]

ShoppingCart.add_product_to_cart(izvele)
ShoppingCart.remove_product_from_cart(izvele)
ShoppingCart.get_total_price(izvele)

