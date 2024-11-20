# TODO решите задачу
import json
def task() -> float:
    filename = 'input.json'
    list_ = []
    with open(filename) as file:
        data = json.load(file)

    for i in data:
        list_.append(i['score'] * i['weight'])

    sum_ = round(sum(list_), 3)
    return sum_


print(task())