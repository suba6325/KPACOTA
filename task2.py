# TODO Напишите функцию find_common_participants

def find_common_participants(participants_first_group, participants_second_group, separator=','):
    list_similar = []
    for surname_1 in participants_first_group.split(separator):
        for surname_2 in participants_second_group.split(separator):
            if surname_1 == surname_2:
                list_similar.append(surname_1)
    return list_similar


participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"
print(find_common_participants(participants_first_group, participants_second_group))

# TODO Провеьте работу функции с разделителем отличным от запятой

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
