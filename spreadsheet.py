"""
Read in a CSV File for Data Objects in Python from Manning
author: christian.sutton@gmail.com
"""

import argparse
import csv


# Create the parser
my_parser = argparse.ArgumentParser(description='read CSV file for analysis')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to csv file')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

print(input_path)

housing = []

with open(input_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=' ')
    for number,row in enumerate(csvreader):
        if number == 0:
            continue
        else:
            housing.append(row)
        
    