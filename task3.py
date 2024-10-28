# TODO  Напишите функцию count_letters
from typing import Dict, Any


def count_letters(text):
    new_main_str = list(text)
    letters = set(char.lower() for char in new_main_str if char.isalpha())
    sorted_letters = sorted(letters)
    count_of_every_letter = []
    dictionary = {}

    for i in range(len(sorted_letters)):
        count = 0
        for k in range(len(new_main_str)):
            if new_main_str[k] == sorted_letters[i]:
                count += 1
        count_of_every_letter.append(count)

    for i in range(len(sorted_letters)):
        dictionary[sorted_letters[i]] = count_of_every_letter[i]
    return dictionary


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict):
    new_dict = {}
    letters = list(dict.keys())
    counts = list(dict.values())
    sum_letters = sum(counts)
    for i in range(len(letters)):
        new_dict[letters[i]] = round( counts[i]/sum_letters, 4)
    return new_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
print(count_letters(main_str))
print(calculate_frequency(count_letters(main_str)))


# TODO Распечатайте в столбик букву и её частоту в тексте

for i in range(len(calculate_frequency(count_letters(main_str)).keys())):
    print(list(calculate_frequency(count_letters(main_str)).keys())[i],': ', round(list(calculate_frequency(count_letters(main_str)).values())[i], 2), sep='')
