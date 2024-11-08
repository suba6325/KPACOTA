# TODO Напишите функцию find_common_participants

def find_common_participants(participants_first_group, participants_second_group, seporator=','):
    list_similar = []
    for i, surname_1 in enumerate(participants_first_group.split(seporator)):
        for k, surname_2 in enumerate(participants_second_group.split(seporator)):
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
