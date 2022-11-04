# Assignment 1

# This assignment is related to the attached file: “AT employer enterprise births 2007-2018.csv” (Source: Statistik Austria).
# Write Python functions for finding answers to the following questions:

# - Which industry recorded the highest number of enterprise births?
# - Was there an industry in which no enterprise births were recorded? If, yes, which industry was it (list all such industries)?
# - Was there an industry or industries in which consistently increasing number of enterprise births were recorded? If, yes, list all such industries.
# - Which industry recorded the highest average number of enterprise births year-on-year?


## input vars
input_file = "notebooks/files/AT employer enterprise births 2007-2018.csv"


## Read input data into list of dicts

list_of_dict = []

from csv import DictReader
# open file in read mode
with open(input_file, 'r', encoding='latin-1') as f:
	
	dict_reader = DictReader(f, delimiter=';')
	
	list_of_dict = list(dict_reader)


## Debug

print('')
print(list_of_dict[0])
print('')


## Q1: Which industry recorded the highest number of enterprise births?

# for each industry
for idx, dict_item in enumerate(list_of_dict):
    # create list with enterprise births (select columns with headers 'Enterprise births')
    d = {key: value for (key, value) in dict_item.items() if 'Enterprise births' in key}
    number_of_enterprise_births__list = list(d.values())

    # remove thousands separator ',' comma
    number_of_enterprise_births__list = [x.replace(',','') for x in number_of_enterprise_births__list]

    # convert values to int type
    number_of_enterprise_births__list = [int(x) for x in number_of_enterprise_births__list]

    # create total number of enterprise births by summing up values of all years
    total_number_of_enterprise_births = sum(number_of_enterprise_births__list)

    # print(total_number_of_enterprise_births)

    list_of_dict[idx].update({'total_number_of_enterprise_births': total_number_of_enterprise_births})

# get industry with highest number
industry_with_highest_number_of_enterprise_births = max(list_of_dict, key=lambda x:x['total_number_of_enterprise_births'])

print('The industry which recorded the highest number of enterprise births is: ', industry_with_highest_number_of_enterprise_births['Industry sections and divisions'],
    'with a number of: ', industry_with_highest_number_of_enterprise_births['total_number_of_enterprise_births'])


## Q2: Was there an industry in which no enterprise births were recorded? If, yes, which industry was it (list all such industries)?


## Q3: Was there an industry or industries in which consistently increasing number of enterprise births were recorded? If, yes, list all such industries.


## Q4: Which industry recorded the highest average number of enterprise births year-on-year?


