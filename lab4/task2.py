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

    json_data = json.dumps(data, indent=4)

    return json_data


print(task(INPUT_FILENAME))
if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
