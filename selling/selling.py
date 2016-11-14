# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


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
        show_table('selling.csv')
    elif options == 2:
        add(selling.csv)
    elif options == 3:
        remove('sellings.csv', id_)
    elif options == 4:
        update('selings.csv', id_)
    elif options == 5:
        get_lowest_price_item_id(table)
    elif options == 6:
        get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
    pass

# print the default table of records from the file
#
# @table: list of lists


def show_table(table):
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    ui.print_table(data_manager.get_table_from_file(table), list_of_titles)
    start_module()

    pass

# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists


def add(table):
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    add_item = [common.generate_random(table)] + ui.get_inputs(list_labels, table)
    table.append(add_item)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string

def remove(table, id_):
    for l in table:
        if id_ in l:
            table.remove(l)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string

def update(table, id_):
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    for i in table:
        if id_ in i:
            i = [id_] + ui.get_inputs(list_labels, table)
    return table

# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order


def get_lowest_price_item_id(table):
    lowest_prices = table[i][2]
    names = []
    for i in table:
        if int(i[2]) <= sm_prices:
            sm_prices = int(i[2])
    for i in table:
        if i[1] == max(names):
            return i[0]
    return lowest_price


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)

def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    from_date = int(str(year_from) + str(month_from) + str(day_from))
    to_date = int(str(year_from) + str(month_from) + str(day_from))
    get_list = []
    for i in table:
        date_today = int(str(i[5]) + str(i[3]) + str(i[4]))
        if (date_today > from_date) and (date_today < to_date):
            get_list.append(i)
    return get_list

    pass
