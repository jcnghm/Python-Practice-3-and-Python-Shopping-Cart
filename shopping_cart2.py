
cart = {}
def shoppingcart():
    
    while True:
        command = input('What would you like to do? (Show/Add/Delete or Quit)')
        if command.lower() == 'add': # Do this if command input is 'add'
            itemkey = input('Name of the product to add to cart: ')
            itemprice = input("Price of that item: ")
            cart[itemkey] = itemprice
            command = input('Would you like to continue shopping? (Yes or no)')
            if command.lower() == 'no':
                print('Thanks for Shopping! Your Cart: ')
                return
        elif command.lower() == 'show': # Do this if command input is 'show'
            print('Your shopping cart: ')
            return cart
        elif command.lower() == 'delete': # Do this if command input is 'delete'
            print('Your shopping cart has been emptied')
            return cart.clear()
        elif command.lower() == 'quit': # Do this if command input is 'quit'
            print('Thanks for Shopping! Your Cart: ')
            break
        else:
            continue
           
shoppingcart()

print(cart)