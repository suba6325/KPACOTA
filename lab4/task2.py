# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(filepath, separator=',', line_separator='\n'):
    # TODO считать содержимое csv файла
    with open(filepath, 'r', newline=line_separator) as file:
        reader = csv.DictReader(file, delimiter=separator)
        # TODO Сериализовать в файл с отступами равными 4
        data = []
        for row in reader:
            data.append(row)
    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(data, f, indent=4)
    return data


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
