# TODO решите задачу
import json


def task(file) -> float:
    with open(file, 'r') as file:
        data = json.load(file)
        total_sum = 0
        for item in data:
            score = item['score']
            weight = item['weight']
            total_sum += score * weight
    return round(total_sum, 3)


print(task("input.json"))
