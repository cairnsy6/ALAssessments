#!/usr/bin/env python
import csv
import pandas
from lib.csvfile import csv_to_rows, rows_to_csv

def create_new_stock_numbers(filepath):
    artwork_info = csv_to_rows(filepath)
    alphabetical_artwork_info = sorted(artwork_info, key=lambda d: d['Artist']) 
    count = 0
    for i in range(len(alphabetical_artwork_info)):
        if create_new_initials(alphabetical_artwork_info[i]["Artist"]) == create_new_initials(alphabetical_artwork_info[i-1]["Artist"]):
            count += 1
        else:
            count = 0
        new_stock_number = create_new_initials(alphabetical_artwork_info[i]["Artist"])+" "+str(count).zfill(3)
        alphabetical_artwork_info[i]["Stock number"] = new_stock_number
    rows_to_csv('artwork_test.xlsx', artwork_info)
    

def create_new_initials(name):
    if name == "":
        return('ZZ')
    else:
        names = name.split(" ")
        if len(names) == 1:
            return (names[0][:2].upper())
        else:
            return (names[0][0].upper() + names[-1][0].upper())



    """
    Exercise 2
    Write something here which describes what you want your function to do.
    This will help you when creating it...

    """

create_new_stock_numbers('data/artworks.csv')
# create_new_initials("michael  gordon banks farsworth Jordan")

