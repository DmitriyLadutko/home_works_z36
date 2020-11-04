from argparse import ArgumentParser
import os

'script for creating a repository and a file in it'

if __name__ == '__main__':

    # Суфикс по которому буду сравнивать файл
    suf = '.py'

    # Вводимое сообщение если выполняется условие
    message = "def main():\n\tpass\n\n\nif __name__ == '__main__':\n\tmain()"

    parser = ArgumentParser()
    parser.add_argument('-f', '--folder_name', required=True)
    parser.add_argument('-fn', '--file_name', required=True)
    args = parser.parse_args()

    # Нахождение абсолютного пути до файла
    file_path = os.path.abspath(__file__)

    # Нахождение директории в которой лежит файл
    dir_name = os.path.dirname(file_path)

    # Создание нового пути к директории
    new_direct = f'{dir_name}/{args.folder_name}'

    # Создание нового пути к файлу
    new_file = f'{new_direct}/{args.file_name}'

    # Создание новой директории
    os.mkdir(new_direct)

    # Создание нового файла если последних 3 символа равны суфиксу иначе удалить файл и директорию
    with open(new_file, 'w') as file:
        if new_file[-3:] == suf:
            file.write(message)
        else:
            os.remove(new_file)
            os.rmdir(new_direct)
