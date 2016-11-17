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
    title = "Game Store"
    exit = "Back to Main menu"
    list_options = ["Show Table",
                    "Add",
                    "Remove",
                    "Update",
                    "Counts by Manufacturers",
                    "Average by Manucfacturer"]

    while True:
        ui.print_menu(title, list_options, exit)
        inputs = ui.get_inputs(["Please enter a number: "], "")
        path = os.path.dirname(os.path.abspath(__file__)) + "/games.csv"
        table = data_manager.get_table_from_file(path)
        try:
            option = int(inputs[0])
        except:
            continue

        if option == 1:
            show_table(path)
        elif option == 2:
            data_manager.write_table_to_file(path, add(table))
        elif option == 3:
            id_ = ui.get_inputs(["Enter the ID to remove: "], "")
            data_manager.write_table_to_file(path, remove(table, id_[0]))
        elif option == 4:
            id_ = ui.get_inputs(["Enter the ID to update or modify: "], "")
            data_manager.write_table_to_file(path, update(table, id_[0]))
        elif option == 5:
            get_counts_by_manufacturers(path)
        elif option == 6:
            get_average_by_manufacturer(path)
        elif option == 0:
            return
        else:
            raise KeyError("There is no such option.")

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
    list_of_titles = ["ID: ", "Title: ", "Manufacturers: ", "Price: ", "in stock: "]
    new_element = ui.get_inputs(list_of_titles, " ")
    table.append(new_element)
    return table

# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string


def remove(table, id_):
    for i in table:
        if id_ in i:
            table.remove(i)
    return table

# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string


def update(table, id_):
    list_of_titles = ["ID", "Title", "Manufacturers", "Price", "In stock"]
    for line in table:
        if id_ in line:
            line = [id_] + ui.get_inputs(list_labels, table)
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
