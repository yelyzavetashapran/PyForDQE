import csv
from collections import Counter
import pandas as pd

PATH = r'C:/Users/Yelyzaveta_Shapran/Desktop/New folder (2)/test_module/newsfeed.txt'


def get_words_letters(path_to_file):
    with open(path_to_file, 'r') as f:
        rows_from_file = [str(i) for i in f.readlines()]
        f.close()

    words = []
    letters = []
    for i in rows_from_file:
        every_line = i.replace('!', ',').replace('?', ',').replace(' ', ',').replace('.', ',').replace('\n', ',').replace(':', ',').replace('&', ',')
        new_rows = every_line.split(',')

        for word in new_rows:
            if word.isalpha():
                words.append(word.lower())
                for letter in word:
                    letters.append(letter)

    cnt_letters = dict(Counter(letters))
    cnt_words = dict(Counter(words))

    return words, letters, cnt_letters, cnt_words


words_list, letters_list, count_letters, count_words = get_words_letters(PATH)


def create_csv1():
    with open('task_1.csv', 'w', newline='') as f:
        w = csv.writer(f, delimiter='-')
        w.writerows(count_words.items())
        return 'File "task_1.csv" created successfully.'


def cnt_upper_l(dictionary):
    new_dict = {}
    for letter, count in dictionary.items():
        if letter.isupper():
            new_dict[letter] = count
        else:
            new_dict[letter] = 0

    return new_dict


count_of_upper_case = cnt_upper_l(count_letters)


def percent_of_total_cnt(dictionary):
    new_dict = {}
    total_cnt = sum(dictionary.values())
    for letter, count in dictionary.items():
        percent = count * 100.0 / total_cnt
        new_dict[letter] = percent

    return new_dict


percent = percent_of_total_cnt(count_letters)


# Second file creating with pandas for better performance
def create_csv2():
    letter = [*count_letters.keys()]
    count = [*count_letters.values()]
    cnt_up = [*count_of_upper_case.values()]
    pct = [*percent.values()]

    d = {'letter_name': letter, 'count_all': count, 'count_uppercase': cnt_up, 'percent': pct}

    df = pd.DataFrame(d)

    df.to_csv('task_2.csv', index=False)

    return 'File "task_2.csv" created successfully.'


print(create_csv1())
print(create_csv2())
