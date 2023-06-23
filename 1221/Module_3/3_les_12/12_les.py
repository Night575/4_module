def factorial(number: int):
    if number == 1:
        return number
    return number * factorial(number - 1)


import os


current_path = os.path.abspath(__file__)
parent_path = os.path.join(current_path, '..')
parent_parent_path = os.path.join(parent_path, '..')
print(parent_path)


def get_all_path(path, filename=None):
    for i_file in os.listdir(path):
        new_path = os.path.join(path,i_file)
        if os.path.isdir(new_path):
            file = open(i_file, 'a', encoding='utf-8')
            file.close()
            print('Директория -- >', new_path)
            get_all_path(new_path)
        else:
            if filename:
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(i_file)
get_all_path(parent_parent_path)
