# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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
        show_table()
    elif options == 2:
        add(items.csv)
    elif options == 3:
        remove(items.csv, _id)
    elif options == 4:
        update(items.csv, _id)
    elif options == 5:
        which_year_max(table)
    elif options == 6:
        avg_amount(table, 2016)

# print the default table of records from the file
#
# @table: list of lists


def show_table(table):
    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    ui.print_table(table, title_list)

# Ask a new record as an input from the user than add it to @table, than return @table
# @table: list of lists


def add(table):
    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    add_item = [common.generate_random(table)] + ui.get_inputs(list_labels, table)
    table.append(add_item)
    return table

# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string


def remove(table, id_):
    for i in table:
        if id in i:
            table.remove(i)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    for line in table:
        if id_ in line:
            line = [id_] + ui.get_inputs(title_list, table)
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    year = {}
    for line in table:
        if line[4] == "in":
            if line[3] not in year.keys():
                year.update({line[3]: int(line[5])})
            else:
                year[line[3]] += int(line[5])
        elif line[4] == "out":
            if line[3] not in year.keys():
                year.update({line[3]: int(line[5])})
            else:
                year[line[3]] += int(line[5])
    maxi = max(year.values())
    for k, v in year.items():
        if v == maxi:
            answer = int(k)
    return answer

    # the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
    # return the answer (number)


def avg_amount(table, year):
    profit = 0
    counter = 0
    for line in table:
        if int(line[3]) == year:
            if str(line[4]) == str("in"):
                profit += int(line[5])
                counter += 1
            elif str(line[4]) == str("out"):
                profit -= int(line[5])
                counter += 1
    avg = profit / counter
    return avg
    pass
