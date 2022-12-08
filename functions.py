FILEPATH = "input.txt"


def get_data(filepath=FILEPATH, strip=False):
    """ Get data from input file """
    with open(filepath, 'r') as file_local:
        local_data = file_local.readlines()
    if not strip:
        return local_data
    else:
        local_data_stripped = [s.strip() for s in local_data]
        return local_data_stripped
