import csv
import re


if __name__ == "__main__":
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    # Корректировка телефонов
    phone_pattern = r"(8|\+7)(\D+|)(\d..)(\D+|)(\d..)(\D+|)(\d.)(\D+|)(\d.)"
    add_pattern = r"(\(|)(доб.)\s(\d+)(\)|)"
    result = []
    for i in contacts_list:
        j = []
        for k in i:
            k = re.sub(phone_pattern, r"+7(\3)\5-\7-\9", k)
            k = re.sub(add_pattern, r"\2\3", k)
            j.append(k)
        result.append(j)

    # Раскидываем ФИО по разделам
    for i in result:
        a = i[0].find(" ")
        if a > 0:
            i[1] = i[0][a + 1:]
            i[0] = i[0][:a]
        a = i[1].find(" ")
        if a > 0:
            i[2] = i[1][a + 1:]
            i[1] = i[1][:a]

    # Объединяем инфу и удаляем лишнее
    for i in range(len(result)):
        for j in range(len(result)):
            if j <= i:
                continue
            if result[i][0] == result[j][0] and result[i][1] == result[j][1]:
                for k in range(len(result[0])):
                    if result[j][k]:
                        result[i][k] = result[j][k]
                    result[j][k] = ""
    for i in result:
        if not i[0]:
            result.remove(i)

    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(result)
