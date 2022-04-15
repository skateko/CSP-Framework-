def get_rows_file(path : str, title: str, size: str, opt: str):
    complete_path: str = path + title + '_' + size + 'x' + size + opt
    file: str = ""
    f = open(complete_path, "r")
    for x in f:
        file += x
    return file.split('\n')