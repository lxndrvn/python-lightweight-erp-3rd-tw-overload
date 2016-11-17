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

def start_module():
    list_options = ["Show tool table",
                    "Add tool",
                    "Remove tool",
                    "Update tool",
                    "Get available tools",
                    "Get average durability by manufacturers"]
    while True:
        ui.print_menu("Tool Manager", list_options, "Back to Main menu")
        inputs = ui.get_inputs(["Please select an option: "], "")
        path = os.path.dirname(os.path.abspath(__file__)) + "/tools.csv"
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

            get_available_tools(path)

        elif option == 6:

            get_average_durability_by_manufacturers(path)

        elif option == 0:
            return
        else:
            raise KeyError("There is no such option.")


# print the default table of records from the file
# @table: list of lists
def show_table(table):
    title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    ui.print_table(data_manager.get_table_from_file(table), title_list)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["ID: ", "Name: ", "Manufacturer: ", "Purchase date: ", "Durability: "]
    new_element = ui.get_inputs(title_list, " ")
    table.append(new_element)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
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
    title_list = ["ID: ", "Name: ", "Manufacturer: ", "Purchase date: ", "Durability: "]
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
    current_year = 2016
    result = []
    for line in table:
        year = line[3]
        durability = line[4]
        if int(year) + int(durability) > current_year:
            line[3] = int(year)
            line[4] = int(durability)
            result.append(line)
    return result

# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists


def get_average_durability_by_manufacturers(table):
    result = {}
    for line in table:
        _, _, manufacturer, _, durability = line
        if manufacturer in result:
            d_sum, count = result[manufacturer]
            result[manufacturer] = [d_sum + int(durability), count + 1]
        else:
            result[manufacturer] = [int(durability), 1]
    for manufacturer, numbers in result.items():
        d_sum, count = result[manufacturer]
        result[manufacturer] = d_sum / count
    return result
