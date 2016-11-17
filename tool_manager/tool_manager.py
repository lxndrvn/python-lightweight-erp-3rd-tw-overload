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
        title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
        try:
            option = int(inputs[0])
        except ValueError:
            continue
        path = os.path.dirname(os.path.abspath(__file__)) + "/tools.csv"
        table = data_manager.get_table_from_file(path)
    
        if option == 1:
            show_table(path)
        elif option == 2:
            add(path)
        elif option == 3:
            remove(path, id_)
        elif option == 4:
            update(path, id_)
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
    ID = ()
    new_element = [ID] + ui.get_inputs(title_list, " ")
    table.append(new_element)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    title_list = ["ID: ", "Name: ", "Manufacturer: ", "Purchase date: ", "Durability: "]
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
    date = 2016
    title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    available_tools = [element for element in table if (int(element[3]) + int(element[4])) >= date]
    for a in range(len(available_tools)):
        available_tools[a][0] = int(available_tools[a][0])
        available_tools[a][1] = int(available_tools[a][1])
    return available_tools
    pass

# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):
    title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    average_durability = {}
    average_durability = {manufacturer[2]: 0 for manufacturer in table if average_durability.get(manufacturer[
                                                                                                 2]) == None}
    keys = average_durability.keys()
    counter_dict = {key: 0 for key in keys}
    for tool in table:
        average_durability[str(tool[2])] = average_durability[str(tool[2])] + int(tool[4])
        counter_dict[str(tool[2])] += 1
    for key in average_durability.keys():
        average_durability[key] /= counter_dict[key]
    return(average_durability)