from helper_module import *

# calculate the total cost function
def customers_cost(shopping_list):
    s = 0
    for i in range(len(shopping_list)):
        s += shopping_list[i][3]
    return s


# write the data to file
def write_to_file(data):
    try:
        write_file = open(filename, "a")
        for i in range(len(data)):
            write_file.write('%-10s %30s %18d %18.2f\n'
                             % (data[i][0], data[i][1], data[i][2], data[i][3]))
    except IOError:
        print("not found")
    finally:
        write_file.close()


# call our functions in 1 method
def main_method():
    shop_list = customers_entry()
    cost = customers_cost(shop_list)
    print('The Cost of customers entered:', cost)
    write_to_file(shop_list)


# run the program in one call
main_method()
