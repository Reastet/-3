# TODO  Напишите функцию count_letters
def count_letters(inp_string):
    dict_of_letters = {}
    list_of_letters = list(inp_string.lower())
    for i in list_of_letters:
        if i.isalpha():
            if i in dict_of_letters.keys():
                dict_of_letters[i] += 1
            else:
                dict_of_letters[i] = 1
    return dict_of_letters


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_of_count_letters):
    total_letters = sum(list(dict_of_count_letters.values()))
    dict_freq = {}
    for i, j in dict_of_count_letters.items():
        dict_freq[i] = round(j / total_letters, 2)
    return dict_freq

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
out_dict = count_letters(main_str)
out_dict = calculate_frequency(out_dict)
for i, j in out_dict.items():
    print(f"{i}: {j:.2f}")