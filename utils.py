def open_file(path):
    with open(path, 'r') as fin:
        return fin.readlines()


def make_list_from_string(string, separator=False, integer=False):
    result = []
    if separator:
        result = string.split(separator)
    else:
        result = string.split(' ')
    if integer:
        return [int(i) for i in result]
    else:
        return result

def remove_new_line_from_list_items(list_w_items):
    cleaned_list = []
    for i in list_w_items:
        cleaned_list.append(i.strip('\n'))
    return cleaned_list
