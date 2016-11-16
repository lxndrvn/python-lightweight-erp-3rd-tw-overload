
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

    title = "Accounting"

    list_options = ['Show_table',
                    'Add',
                    'Remove',
                    'Update',
                    'get the highest profit',
                    'get the average profit']

    exit_message = "Go back to main"

    ui.print_menu(title, list_options, exit_message)

    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]

    if option == 1:
        show_table()
    elif option == 2:
        add(items.csv)
    elif option == 3:
        remove(items.csv, _id)
    elif option == 4:
        update(items.csv, _id)
    elif option == 5:
        which_year_max(table)
    elif option == 6:
        avg_amount(table, 2016)
    else:
        raise KeyError("It's not an option.")


def show_table(table):
    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    ui.print_table(table, title_list)


def add(table):
    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    add_item = [common.generate_random(table)] + ui.get_inputs(list_labels, table)
    table.append(add_item)
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
