# TODO Напишите функцию find_common_participants

def find_common_participants(participants_first_group, participants_second_group, seporator=', '):
    list_first = participants_first_group.split(seporator)
    list_second = participants_second_group.split(seporator)
    list_similar = []
    for i in range(len(list_first)):
        for k in range(len(list_second)):
            if list_first[i] == list_second[k]:
                list_similar.append(list_first[i])
    return list_similar


participants_first_group = "Иванов, Петров, Сидоров"
participants_second_group = "Петров, Сидоров, Смирнов"
print(find_common_participants(participants_first_group, participants_second_group))


# TODO Провеьте работу функции с разделителем отличным от запятой

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
