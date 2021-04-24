filename = "shopping.txt"


def customers_entry():
    customers_count = int(input('Enter the Number of Customers you want to add ? '))
    customers_count += 1
    customers = []
    c = []
    for i in range(1, customers_count, 1):
        name = input('input customer name: ')
        address = input('input customer address: ')
        items = int(input('input items bought: '))
        total = float(input('input total_price: '))
        c.append(name)
        c.append(address)
        c.append(items)
        c.append(total)
        customers.append(c)
        # reset list object
        c = []
        print('\n')

    return customers
