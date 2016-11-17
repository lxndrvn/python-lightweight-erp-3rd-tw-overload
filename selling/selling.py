
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
    table = data_manager.get_table_from_file(current_file_path + "/sellings.csv")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    list_options = ["Show Table",
                    "Add to table",
                    "Remove from table",
                    "Update table",
                    "Lowest price ID",
                    "Sold in a period"]
    ui.print_menu("Sellings menu", list_options, "Exit to main menu")

    inputs = ui.get_inputs(["Please enter a number: "], "")
    if option == 1:
        show_table('selling.csv')
    elif option == 2:
        add(selling.csv)
    elif option == 3:
        remove('sellings.csv', id_)
    elif option == 4:
        update('selings.csv', id_)
    elif option == 5:
        get_lowest_price_item_id(table)
    elif option == 6:
        list_labels = ["month from: ", "day from: ", "year from: ", "month to: ", "day to: ", "year to: "]
        ui.print_result(get_items_sold_between(sell_list, int(inputs[0]), int(
            inputs[1]), int(inputs[2]), int(inputs[3]), int(inputs[4]), int(inputs[5])), "")
    elif option == "0":
        data_manager.write_table_to_file("selling/selling.csv", sell_list)
        break
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    ui.print_table(data_manager.get_table_from_file(table), list_of_titles)
    start_module()


def add(table):
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    add_item = [common.generate_random(table)] + ui.get_inputs(list_labels, table)
    table.append(add_item)
    return table


def remove(table, id_):
    for i in table:
        if id_ in i:
            table.remove(i)
    return table


def update(table, id_):
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    for line in table:
        if id_ in line:
            line = [id_] + ui.get_inputs(list_labels, table)
    return table


def get_lowest_price_item_id(table):
    lowest_price = 1000000
    id = 0
    for line in table:
        if int(line[2]) < lowest_price:
            lowest_price = int(line[2])
            id = line[0]
            title = line[1]
        if lowest_price == int(line[2]):
            if line[1] < title:
                lowest_price = int(line[2])
                id = line[0]
                title = line[1]
    return id


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    from_date = int(str(year_from) + str(month_from) + str(day_from))
    to_date = int(str(year_from) + str(month_from) + str(day_from))
    get_list = []
    for line in table:
        date_today = int(str(line[5]) + str(line[3]) + str(line[4]))
        if date_today > from_date and date_today < to_date:
            get_list.append(line)
    return get_list
