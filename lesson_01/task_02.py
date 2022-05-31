import os


def print_directory_contents(path):
    for file in os.listdir(path):
        new_path = os.path.join(path, file)
        if os.path.isdir(new_path):
            print("\033[33m {}".format(file))
            print_directory_contents(new_path)
        else:
            print("---", "\033[37m {}".format(file))


to_print = []
# path = input('Введите путь')
path = r'F:\Sonya\GeekBrains\02_linux_basics'
print_directory_contents(path)
