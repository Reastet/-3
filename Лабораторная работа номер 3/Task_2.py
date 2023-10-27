# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, split_type =','):
    first_group_list = first_group.split(split_type)
    second_group_list = second_group.split(split_type)
    first_group_list = set(first_group_list)
    out_data =  list(first_group_list.intersection(second_group_list))
    out_data.sort()
    return out_data

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
