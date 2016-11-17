# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    table = data_manager.get_table_from_file(current_file_path + "/games.csv")

    list_options = ["Show Table"
                    "Add"
                    "Remove"
                    "Update"
                    "Counts by Manufacturers"
                    "Average by Manucfacturer"]

    ui.print_menu("Store", list_of_options, "Exit")

    while True:
        if option == 1:
            show_table(table)
        elif option == 2:
            add(table)
        elif option == 3:
            remove(table, id_)
        elif option == 4:
            update(table, id_)
        elif option == 5:
            get_counts_by_manufacturers(table)
        elif option == 6:
            get_average_by_manufacturer(table, manufacturer)
        elif option == 0:
            return
        else:
            raise KeyError("This is not an option")
# else?

# print the default table of records from the file
#
# @table: list of lists


def show_table(table):
    list_of_titles = ["ID", "Title", "Manufacturers", "Price", "in stock"]

    ui.print_table(data_manager.get_table_from_file(table), list_of_titles)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists


def add(table):
    list_of_titles = ["ID", "Title", "Manufacturers", "Price", "in stock"]
    table_to_extend = data_manager.get_table_from_file(table)
    table_to_extend.append(common.ask_for_data_to_add(table_to_extend, list_of_titles[1:]))
    data_manager.write_table_to_file('games.csv', table_to_extend)

    return table

# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string


def remove(table, id_):
    table_to_shorten = data_manager.get_table_from_file(table)
    try:
        table_to_shorten.remove(common.ask_for_data_to_remove(table_to_shorten, id_))
        data_manager.write_table_to_file('games.csv', table_to_shorten)
    except:
        ui.print_error_message("No game found with this ID!\n")
    start_module()

# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string


def update(table, id_):
    list_of_titles = ["ID", "Title", "Manufacturers", "Price", "In stock"]
    table_to_update = data_manager.get_table_from_file(table)
    updated_table = common.ask_for_data_and_update(table_to_update, id_, list_of_titles[1:])
    data_manager.write_table_to_file('games.csv', updated_table)
    return table

# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }


def get_counts_by_manufacturers(table):
    data = {}
    for i in range(len(table)):
        stat = table[i][2] in data
        if stat is not True:
            data[table[i][2]] = 1
        else:
            data[table[i][2]] += 1
    return data

# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number


def get_average_by_manufacturer(table, manufacturer):
    all_stock = 0
    count = 0
    for i in range(len(table)):
        if manufacturer == table[i][2]:
            all_stock += int(table[i][4])
            count += 1
    res = all_stock / count
    return res
