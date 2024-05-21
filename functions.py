def get_countries(filepath="countries.txt"):
    """ Read the text file and return
    the list of countries.
    """
    with open(filepath, "r") as file:
        countries_local = file.readlines()
    return countries_local


def write_countries(countries_arg, filepath="countries.txt"):
    with open(filepath, "w") as file:
        file.writelines(countries_arg)


print("Hello from functions")
