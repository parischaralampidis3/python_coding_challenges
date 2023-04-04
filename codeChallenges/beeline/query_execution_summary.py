from sys import argv
script, filename  = argv

import itertools
#set a variable for your input file 
filename = "beeline_consent_query_stderr.txt"
my_dict = {}


def read_dictionary():
    with open(filename, 'r', ) as file:
        for line in itertools.islice(file,83,89): 
            key, *value = line.strip().split(',')
            my_dict[key] = value
    print(my_dict)
    #add code here
read_dictionary()
