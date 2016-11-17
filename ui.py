def print_table(table, title_list):
    print(('|') + (" | ".join(title_list)) + ('|'))
    for row in table:
        print(('|') + ('-') * 100 + ('|'))
        print(('|') + (" | ".join(row)) + ('|'))
    print(('|') + ('-') * 20 + ('|'))


def print_result(result, label):
    if type(result) == str:
        print(result)
    elif type(result) == list:
        for item in result:
            print(item)
    elif type(result) == dict:
        for k, v in result.items():
            print(k, str(v))


def print_menu(title, list_options, exit_message):
    print(title)
    for n in range(0, len(list_options)):
        print('(' + str(n + 1) + ') ' + list_options[n])
    print('(0) ' + exit_message)


def get_inputs(list_labels, title):
    list = []
    for item in list_labels:
        add = input('%s' % (item))
        list.append(add)
    return list


def print_error_message(message):
    print(message)
