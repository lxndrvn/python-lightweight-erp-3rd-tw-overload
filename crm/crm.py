# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
    if option == 1:
        show_table("customers.csv")
    elif option == 2:
        add("customers.csv")
    elif option == 3:
        remove("customers.csv", id_)
    elif option == 4:
        update("customers.csv", id_)
    elif option == 5:
        get_longest_name_id("customers.csv")
    elif option == 6:
        get_subscribed_emails("customers.csv")
    elif option == 0:
        return
    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "Name", "Email", "Subscribed"]
    ui.print_table(data_manager.get_table_from_file(table), list_of_titles)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["ID", "Name", "Email", "Subscribed"]
    new_record = [common.generate_random(table)] + ui.get_inputs(title_list, table)
    table.append(new_record)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    for line in table:
        if id_ in line:
            table.remove(line)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    id_list = []
    title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    for line in table:
        if id_ in line:
            line = [id_] + ui.get_inputs(list_titles, table)
    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):
    title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    longest_name = [' ']
    for line in table:
        if len(line[1]) == len(longest_name[0]):
            longest_name.append(line[1])
        elif len(line[1]) > len(longest_name[0]):
            longest_name[0] = line[1]
    for line in table:
        if min(longest_name) in line[1]:
            return(line[0])


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    subscribers = []
    for line in table:
        if '1' in line[3]:
            subscribers.append(line[2] + ';' + line[1])
    return(subscribers)
