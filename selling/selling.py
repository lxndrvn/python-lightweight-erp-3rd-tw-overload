
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

    list_options = ["Show Table",
                    "Add to table",
                    "Remove from table",
                    "Update table",
                    "Lowest price ID",
                    "Sold in a period"]
    exit_message = "Go back to main"

    while True:
        ui.print_menu("Sellings menu", list_options, "Exit to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        try:
            option = int(inputs[0])
        except ValueError:
            continue
        path = os.path.dirname(os.path.abspath(__file__)) + "/sellings.csv"
        table = data_manager.get_table_from_file(path)

        if option == 1:

            show_table(path)

        elif option == 2:

            data_manager.write_table_to_file(path, add(table))

        elif option == 3:

            id_ = ui.get_inputs(["Enter the ID to remove: "], "")
            data_manager.write_table_to_file(table, remove(path, id_[0]))

        elif option == 4:

            id_ = ui.get_inputs(["Enter the ID to update or modify: "], "")
            data_manager.write_table_to_file(path, update(table, id_[0]))

        elif option == 5:

            get_lowest_price_item_id(table)

        elif option == 6:

            list_labels = ["month from: ", "day from: ", "year from: ", "month to: ", "day to: ", "year to: "]
            ui.print_result(get_items_sold_between(sell_list, int(inputs[0]), int(
                inputs[1]), int(inputs[2]), int(inputs[3]), int(inputs[4]), int(inputs[5])), "")

        elif option == "0":
            data_manager.write_table_to_file(table, sell_list)
            return False
        else:
            raise KeyError("This is not an option.")


def show_table(table):
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    ui.print_table(data_manager.get_table_from_file(table), title_list)


def add(table):
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    new_element = ui.get_inputs(title_list, " ")
    table.append(new_element)
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
