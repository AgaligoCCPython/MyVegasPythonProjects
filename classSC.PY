print('Welcome to Vegas Restaurant')
menu = ['Milkshake', 'Ice cream', 'Cup cake', 'juice', 'bread' , 'tea']
price = [99.99 ,120.99 ,80.79, 55.99 ,90.12 ,80]

print('ITEM', 'PRICE,excl TAX', sep = '\t\t')

for kk in range(len(menu)):
    print(str(kk+1)+'.'+menu[kk], price[kk], sep = '\t\t')
print()

shopping_cart = []
shopping_quant = []

shopping_complete = False

while not shopping_complete:
    order = int(input("Enter 1 to 6 to select a food item, 7 to checkout\n"))

    if order == 7:
        shopping_complete = True
        print("Proceed to checkout...")
        break

    if 1 <= order <= len(menu):
        print('Purchasing', menu[order - 1])
        quant = int(input('How many unit do you wish to purchase?(negative number to remove from the cart.)\n'))
        if quant > 0:
            if menu[order - 1] in shopping_cart:
                print('repeat purchase')
                idx = shopping_cart.index(menu[order - 1])
                shopping_quant[idx] = shopping_quant[idx] + quant
            else:
                print('new purchase')
                shopping_cart.append(menu[order - 1])
                shopping_quant.append(quant)
        elif quant < 0:
            if menu[order - 1] in shopping_cart:
                idx = shopping_cart.index(menu[order - 1])
                remove_qty = min(abs(quant), shopping_quant[idx])
                shopping_quant[idx] = shopping_quant[idx] - remove_qty
                print('Removed from the shopping cart:',remove_qty,'units of', menu[order - 1])
                if shopping_quant[idx] == 0:
                    del shopping_cart[idx]
                    del shopping_quant[idx]
            else: 
                print('This menu is not exist in the shopping cart')
    else:
        print('Invalid input')

print()
print('shopping is complete, displaying shopping cart')

grand_tot = 0.0

print('ITEM','QUANT','UNIT PRICE','TOTAL', sep = '\t\t\t')

for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    unit_price = float(price[idx])
    total_price = unit_price*shopping_quant[kk]
    grand_tot = grand_tot + total_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, total_price, sep='\t\t\t')

print()
print('The grand total is' ,round(grand_tot,2) )

