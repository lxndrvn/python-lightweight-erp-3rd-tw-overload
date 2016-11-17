# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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
    list_options = ["Show Table",
                    "Add",
                    "Remove",
                    "Update",
                    "Oldest person",
                    "Average age"]

    exit_message = "Go back to main"

    while True:
        ui.print_menu("HR menu", list_options, "Exit to Main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        try:
            option = int(inputs[0])
        except ValueError:
            continue
        path = os.path.dirname(os.path.abspath(__file__)) + "/persons.csv"
        table = data_manager.get_table_from_file(path)

        if option == 1:

            show_table(path)

        elif option == 2:

            data_manager.write_table_to_file(path, add(table))

        elif option == 3:

            id_ = ui.get_inputs(["Enter an ID to remove: "], "")
            data_manager.write_table_to_file(table, remove(path, id_[0]))

        elif option == 4:

            id_ = ui.get_inputs(["Enter the ID to update or modify: "], "")
            data_manager.write_table_to_file(path, update(table, id_[0]))

        elif option == 5:

            get_oldest_person(path)

        elif option == 6:

            get_persons_closest_to_average(path)

        elif option == 0:
            return
        else:
            raise KeyError("This is not an option.")


# print the default table of records from the file
#
# @table: list of lists


def show_table(table):
    list_of_titles = ["ID", "Name", "Birth Date"]
    ui.print_table(data_manager.get_table_from_file(table), list_of_titles)
    return

# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)

# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists


def add(table):
    title_list = ["ID", "Name", "Birth Date"]
    new_element = ui.get_inputs(title_list, " ")
    table.append(new_element)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string


def remove(table, id):
    remove_data = data_manager.get_table_from_file(table)
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


def update(table, id):
    title_list = ["ID", "Name", "Birth Date"]
    for a in range(le(table)):
        if str(id_) == str(table[a][0]):
            updated_element = ui.get_inputs(title_list, " ")
            table[a] = [id_] + updated_element
    return table

# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)


def get_oldest_person(table):
    oldest_year = table[0][2]
    oldest = [table[0][1]]
    for i in range(len(table)):
        if int(table[i][2]) < int(oldest_year):
            oldest_year = table[i][2]
            oldest = [table[i][1]]
        elif int(table[i][2]) == int(oldest_year):
            oldest.append(table[i][1])
    return oldest


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)

def get_persons_closest_to_average(table):
    sum_year = 0
    for i in range(len(table)):
        sum_year = sum_year + int(table[i][2])
    average = int(sum_year / len(table))
    smallest_difference = abs(average - int(table[0][2]))
    closest_person = [table[0][1]]
    for i in range(len(table)):
        if abs(average - int(table[i][2])) < int(smallest_difference):
            closest_person = [table[i][1]]
            smallest_difference = abs(average - int(table[i][2]))
        elif abs(average - int(table[i][2])) == int(smallest_difference):
            closest_person.append(table[i][1])
    return closest_person
