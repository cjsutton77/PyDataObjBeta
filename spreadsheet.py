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

def read_input(inp_path,header_exists = True ):
    '''
    Read csv file and output 2-D list of output.
    Assumes 1st element in list is always header.
    
    header_exists is set to True indicating first row is a header
    '''
    housing = []


    with open(input_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ')
        for number,row in enumerate(csvreader):
            if header_exists and number == 0:
                continue
            else:
                housing.append(row)
    
    return housing

housing_csv = read_input(input_path)
        
    