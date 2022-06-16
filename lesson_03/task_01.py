# При вызове функции в качестве аргумента должно передаваться путь и имя файла с расширением.
# В функции необходимо реализовать поиск имени файла (с расширением), а затем «выделение» имени файла (без расширения).
# Расширений может быть несколько (например testfile.tar.gz).
import os.path


def get_filename(path, full_filename):
    if full_filename in path:
        filename = full_filename.split('.')[0]
        index = path.find(full_filename)
        return path[0:index] + filename


print(get_filename('F:/folder/filename.ac.bfd', 'filename.ac.bfd'))
