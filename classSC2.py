print('Welcome to Vegas Restaurant')
menu = ['Milkshake', 'Ice cream', 'Cup cake', 'Apple juice', 'Cheese Cake' , 'Apple Pie']
price = [99.99 ,120.99 ,80.79, 20.99 ,90.12 ,80]

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
print()

dct_rate = 10.0
kk = 1

searching = True

while searching:
    next_500 = (grand_tot // 500 + kk) * 500  # ใช้ kk ช่วยคำนวณขั้นถัดไป
    gap_500 = next_500 - grand_tot
    dct = next_500 * dct_rate / 100
    print(next_500, gap_500, dct)
    
    if gap_500 > dct:
        searching = False
    else:
        kk = kk + 1

print('You will get discount if you spend' , next_500)

dw = input('Do you want this offer? (Y/N)')

add_quant = []

if dw.upper() == 'Y':
    print('Discount wanted')
    Extra_discount = input('Do you are a Normal Customer, student, employ or owner friend .(S/E/O/C)\n')
    if Extra_discount == 'S':
        dct_rate = 15.0;
        print('You get 15% dicount')
    if Extra_discount == 'E':
        dct_rate = 20.0;
        print('You get 20% dicount')
    if Extra_discount == 'O':
        dct_rate = 25.0;
        print('You get 25% dicount')
    if Extra_discount == 'C':
        dct_rate = 10.0;
        print('You get 10% dicount')

    print('You have the following option:')
    for kk in range(len(menu)):
        add_quant.append(int(gap_500//price[kk] + 1))
        print(str(kk + 1), '. Add', menu[kk], add_quant[kk],'units')
    add_on = int(input('Indicate your preference'))
    if menu[add_on - 1] in shopping_cart:
        idx = shopping_cart.index(menu[add_on - 1])
        shopping_quant[idx] +=add_quant[add_on - 1]
    else:
        print('new purchase')
        shopping_cart.append(menu[add_on - 1])
        shopping_quant.append(add_quant[add_on - 1])
else:
    print('Proceed to checkout')

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

tax_rate = 7.0;

if dw == 'Y':
    dct= dct_rate/100*grand_tot
else:
    dct = 0.0

tax = tax_rate/100*(grand_tot-dct)

print('Total order (INR)', round(grand_tot , 2))
print('Discount (INR)', round(dct , 2))
print('Post discount (INR)', round(grand_tot - dct , 2))
print('Tax (INR)', round(tax , 2))

print('Total to pay', round(grand_tot-dct+tax , 2))
print('Thanks you')
print('Bye!!!!!')