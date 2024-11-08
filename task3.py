# TODO  Напишите функцию count_letters
from decimal import Decimal


def count_letters(text):
    new_main_str = list(text)
    letters = list(char.lower() for char in new_main_str if char.isalpha())
    count_of_every_letter = []
    text_dictionary = {}

    for i, letter in enumerate(letters):
        count = 0
        for k, symbol in enumerate(new_main_str):
            if symbol == letter:
                count += 1
        count_of_every_letter.append(count)

    for i in range(len(letters)):
        text_dictionary[letters[i]] = count_of_every_letter[i]
    return text_dictionary


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dictionary):
    new_dict = {}
    letters = list(dictionary.keys())
    counts = list(dictionary.values())
    sum_letters = sum(counts)
    for i in range(len(letters)):
        new_dict[letters[i]] = Decimal(counts[i] / sum_letters)
        new_dict[letters[i]] = new_dict[letters[i]].quantize(Decimal("1.00"))
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

# TODO Распечатайте в столбик букву и её частоту в тексте


for key, value in calculate_frequency(count_letters(main_str)).items():
    print(f"{key}: {value}", sep='\n')
