FILEPATH = "input.txt"


def get_data(filepath=FILEPATH):
    """ Get data from input file """
    with open(filepath, 'r') as file_local:
        local_data = file_local.readlines()
    return local_data
