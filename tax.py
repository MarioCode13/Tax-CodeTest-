import sys

exempt_items = ['book', 'food', 'chocolate', 'medical', 'headache' ]

item_dict = {}

def round_to(n, precision):
    place = 0.5
    return int( n/precision+place ) * precision

def round_to_05(n):
    return round_to(n, 0.05)

def main():
    tax=[]
    add_item = input("Add item? Y/N: ")
    while add_item.capitalize() == 'Y':
        quantity = input("How many? ")
        item_to_add = input("Item: ")
        original_price = float(input("Price: "))
        imported = False
        exempt = False
        if 'import' in item_to_add:
            imported = True
        for i in range(0, len(item_to_add.split())):        # search string see if exempt or not
            item_to_add = item_to_add.rstrip('s')           # remove plurals
            if item_to_add.split()[i] in exempt_items:
                exempt = True
        import_tax = 0
        if imported == True:
            import_tax += original_price*0.05                # add 5% on imported goods   
        print("Imported", imported)      
        sales_tax = 0
        if exempt == False:
            sales_tax += original_price*0.1                  # add 10% if not exempt  add to total sales tax 
        total_tax = sales_tax + import_tax
        rounded_tax = round_to_05(total_tax)
        tax.append(rounded_tax)
        final_price = round((original_price + float(rounded_tax)) * float(quantity), 2) 
        item_to_add = quantity + ' ' + item_to_add
        item = {item_to_add: final_price}
        item_dict.update(item)
        print("Final Price", final_price)
        add_item = input("Add item? Y/N ")

    print('-------------------')
    for key, val in item_dict.items():
        print (key, ':', val)
    print('-------------------')
    print("Sales Taxes:",round(sum(tax), 2))
    print("Total:",round(sum(item_dict.values()) , 2))
    print('-------------------')


if __name__ == '__main__':
    main()