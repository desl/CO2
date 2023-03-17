## Takes a csv from an aranet4 and turns it into something useful by 
## formatting the dates.

import sys
import re

test_string = '09/03/2023 7:52:35,"1118","15.5","61","1001"'

def correct_date(input):
    # input = '09/03/2023 7:52:35,"1118","15.5","61","1001"'
    if input[0] == "T":  # Header String
        return input.strip()
    

    regex = re.search(r"(\d\d)\/(\d\d)\/(\d\d\d\d)\s(\d+)\:(\d\d):(\d\d)(\,[\d\w\",\.]*)", input)

    my_obj = {
        'year': regex[3],
        'month': regex[2],
        'day': regex[1],
        'hour': regex[4],
        'min': regex[5],
        'sec': regex[6],
        'the rest': regex[7]
    }

    if len(my_obj['hour']) == 1:
        my_obj['hour'] = "0" + my_obj['hour']

    if len(my_obj['min']) == 1:
        my_obj['min'] = "0" + my_obj['min']

    if len(my_obj['sec']) == 1:
        my_obj['sec'] = "0" + my_obj['sec']

    output_string = (
        "" +
        my_obj['year'] + "-" +  # year
        my_obj['month'] + "-" +  # month
        my_obj['day'] + " " +  # day
        my_obj['hour'] + ":" +  # hour
        my_obj['min'] + ":" +  # min
        my_obj['sec'] +  # second
        my_obj['the rest']  # The rest of the string
    )

    return output_string

output_string = correct_date(test_string)
if output_string != '2023-03-09 07:52:35,"1118","15.5","61","1001"':
    print("string manipulation failing")
    exit()
# print(output_string)

input_csv = sys.argv[1]
# input_csv = 'csv_input/Lennon_2023-03-09T07_54_09-0800.txt'
# print(input_csv, "input")

with open(input_csv) as f:
    content_list = f.readlines()

# print the list
# print(content_list)

# remove new line characters
# content_list = [x.strip() for x in content_list]
print(content_list)

output = ""

for i in content_list:
    # '09/03/2023 7:52:35,"1118","15.5","61","1001"'
    # date
    output = output + correct_date(i)
    output = output + "\n"

# print(output)

output_filename = input_csv
output_filename = output_filename.replace("txt", "csv")
output_filename = output_filename.replace("input", "output")
print("output file", output_filename)


# transform the date strings to be the right thing.
# write the new file to csv_output
f = open(output_filename, "w")
f.write(output)
f.close()