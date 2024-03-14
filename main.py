import numpy as np
import csv
from tensorflow.keras.utils import to_categorical


def array_num(path_files, begin_year, end_year):
    array = np.array([])
    with open(path_files, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            if row[0] == "Country Name":
                # print(row)
                start_popul = row.index(str(begin_year))
                end_popul = row.index(str(end_year))
            if row[0] == "Russian Federation":
                # print(row)
                for i in range(start_popul, end_popul + 1):
                    # print(row[i])
                    array = np.append(array, int(row[i]))
    return array


def number_arr(array, num_of_categories):
    maxi = array[np.where(array == max(array))[0][0]]
    mini = array[np.where(array == min(array))[0][0]]
    delta = (maxi-mini) / num_of_categories
    array_num_of_categories = np.array([])
    for i in array:
        n = int((i - mini) / delta)
        array_num_of_categories = np.append(array_num_of_categories, n)
    return array_num_of_categories


arr = array_num("datasets/new.csv", 1960, 2022)
arr_num_of_categories = number_arr(arr, 100)
new = to_categorical(arr_num_of_categories)
print(new)
