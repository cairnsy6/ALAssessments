# -*- coding: utf-8 -*-
# !/usr/bin/env python
import csv
import pandas as pd
import numpy as np



def rows_to_csv(filepath, rows, columns=[]):
    if len(columns) == 0:
        data = pd.DataFrame.from_dict(rows)
        data.to_excel(filepath)
    else:
        keys = rows[0].keys()
        main_list = [item for item in keys if item not in columns]
        for options in main_list:
            for i in range(len(rows)):
                del rows[i][options]
        data =pd.DataFrame.from_dict(rows)
        data.to_excel(filepath)



def csv_to_rows(filepath):
    with open(filepath, 'r', newline='') as csv_file:
        artwork_reader = csv.DictReader(csv_file)
        list_of_dict = list(artwork_reader)
        return list_of_dict


# csv_to_rows('../data/artworks.csv')

# rows_to_csv('artwork.xlsx', csv_to_rows('data/artworks.csv'))
