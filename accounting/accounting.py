
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


def start_module():
    list_options = ['Show table',
                    'Add',
                    'Remove',
                    'Update',
                    'get the highest profit',
                    'get the average profit']
    exit_message = "Go back to main"

    while True:
        ui.print_menu("Accounting", list_options, "Exit to main menu")
        inputs = ui.get_inputs(["Please select an option: "], "")
        table = data_manager.get_table_from_file(current_file_path + "/items.csv")
        option = int(inputs[0])

        if option == 1:
            show_table(table)
        elif option == 2:
            data_manager.write_table_to_file(table, add(table))
        elif option == 3:
            id_ = ui.get_inputs(["Enter the ID to remove: "], "")
            data_manager.write_table_to_file(table, remove(table, id_[0]))
        elif option == 4:
            id_ = ui.get_inputs(["Enter the ID to update or modify: "], "")
            data_manager.write_table_to_file(table, update(table, id_[0]))
        elif option == 5:
            ui.print_result(which_year_max(table), "Which year had most amount?")
        elif option == 6:
            year = ui.get_inputs(["Given year"], "")
            ui.print_result(avg_amount(table, year), "Average from the given year is : ")
        elif option == 0:
            return
        else:
            raise KeyError("This is not an option.")


def show_table(table):
    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    ui.print_table(table, title_list)


def add(table):
    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    new_element = ui.get_inputs(title_list, " ")
    table.append(new_element)
    return table


def remove(table, id_):
    for i in table:
        if id in i:
            table.remove(i)
    return table


def update(table, id_):
    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    for line in table:
        if id_ in line:
            line = [id_] + ui.get_inputs(title_list, table)
    return table


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
