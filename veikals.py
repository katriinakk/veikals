class Produkti:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price*self.quantity

siers = Produkti("Franču siers", 4.99, 45)
maize = Produkti("Bagete", 2.33, 67)


class ShoppingCart(Produkti):
    def __init__(self, grozs):
        self.grozs =grozs
        grozs = [0, 0, 0, 0]

    def add_product_to_cart(grozs):

        viens = input("Vai Jūs vēlaties ieveitot"+ siers.name +" grozā?")
        divi = input("Vai Jūs vēlaties ieveitot"+ maize.name +" grozā?")
        grozs = [0, 0, 0, 0]
        if viens == "jā":
            grozs[0] = siers.price
            grozs[1] = siers.quantity
        if divi == "jā":
            grozs[2] = maize.price
            grozs[3] = maize.quantity
        return grozs

        
    def remove_product_from_cart(grozs):

        jaut = input("Vai Jūs vēlaties veikt labojumus (noņemt preci no groza)?")

        if jaut == "jā":
            ok = input("Kuru produktu Jūs vēlaties noņemt? (1 - pirmo, 3 - otro, 5 - abus)")
            if ok == 1 or ok == 3:
                grozs.pop(ok-1)
                grozs.pop(ok)
            elif ok == 5:
                grozs = []
            else:
                return("Nepareizi ievadīti dati")

        else:
            pass

    def get_total_price(grozs):
        return grozs[0]*grozs[1] + grozs[2]*grozs[3]

ShoppingCart.add_product_to_cart(0)
ShoppingCart.remove_product_from_cart(0)
ShoppingCart.get_total_price(0)

