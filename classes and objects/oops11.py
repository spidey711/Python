'''
Define a class called Lunch. Its __init__() method should have two arguments:self and menu where menu is a string. Add a method called menu_price. It will involve an if statement:
    if "menu 1" print "Your choice:", menu, "Price 12.00", 
    if "menu 2" print "Your choice:", menu, "Price 13.40", 
    else print "Error in menu".

To check if it works define: Paul=Lunch("menu 1") and call Paul.menu_price().
'''
class Lunch:
    def __init__(self, menu):
        self.menu = menu
    def menuPrice(self):
        if self.menu == "menu 1":
            return f"Your choice: {self.menu}\nPrice: $12.00"
        if self.menu == "menu 2":
            return f"Your choice: {self.menu}\nPrice: $13.40"
        else:
            return "Error in menu..."

paul = Lunch('menu 1')
sam = Lunch('menu 2')
aiden = Lunch('menu 3')

print(paul.menuPrice())
print(sam.menuPrice())
print(aiden.menuPrice())
            