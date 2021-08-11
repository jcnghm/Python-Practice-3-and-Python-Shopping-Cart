
cart = {}
def shoppingcart():
    
    while True:
        command = input('What would you like to do? (Show/Add/Delete or Quit)')
        if command.lower() == 'add': # Do this if command input is 'add'
            itemkey = input('Name of the product to add to cart: ')
            itemprice = input("Price of that item: ")
            cart[itemkey] = itemprice
        elif command.lower() == 'show': # Do this if command input is 'show'
            return cart
        elif command.lower() == 'delete': # Do this if command input is 'delete'
            return cart.clear()
        elif command.lower() == 'quit': # Do this if command input is 'quit'
            break
        else:
            continue
            
shoppingcart()

print(cart)