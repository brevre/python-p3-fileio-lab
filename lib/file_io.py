def write_file(file_name, file_content):
    pass

def append_file(file_name, append_content):
    pass

def read_file(file_name):
    pass
def write_file(file_name, file_content):
    pass

def append_file(file_name, append_content):
    pass

def read_file(file_name):
    pass


import os

def write_file(file_name, file_content):
    """Creates a new .txt file and writes the content to it."""
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content )

def append_file(file_name, append_content):
    """Appends content to an existing .txt file."""
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content )

def read_file(file_name):
    """Reads the content of a .txt file and returns it."""
    with open(f"{file_name}.txt", "r") as file:
        return file.read().strip()


