# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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
    if options == 1:
        show_table("tools.csv")
    elif options == 2:
        add("tools.csv")
    elif options == 3:
        remove("tools.csv", id_)
    elif options == 4:
        update("tools.csv", id_)
    elif options == 5:
        get_available_tools("tools.csv")
    elif options == 6:
        get_average_durability_by_manufacturers("tools.csv")
    elif option == 0:
        return
    pass


# print the default table of records from the file
# @table: list of lists
def show_table(table):
    title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    ui.print_table(data_manager.get_table_from_file(table), list_of_titles)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    ID = (common.generate_random(table))
    new_element = [ID] + ui.get_inputs(title_list, " ")
    table.append(new_element)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    for a in range(len(table)):
        if str(id_) == str(table[a][0]):
            table.pop(a)
            break
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    for a in range(len(table)):
        if str(id_) == str(table[a][0]):
            updated_element = ui.get_inputs(title_list, " ")
            table[a] = [id_] + updated_element
    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):
    date = 2016
    title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    available_tools = [element for element in table if (int(element[3]) + int(element[4])) >= date]
    for a in range(len(available_tools)):
        available_tools[a][3] = int(available_tools[a][3])
        available_tools[a][4] = int(available_tools[a][4])
    return table


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):

    # your code

    pass