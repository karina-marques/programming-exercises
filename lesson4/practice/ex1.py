# Write a function that converts an input list containing
# the numbers inside the list to Fahrneit. If the input_list
# is null, convert the numbers from 0 to 100.

def convert_celsius_temperatures_to_fahrneit(input_list = None):
    if(input_list == None):
        input_list = range(0, 100)
    # Code goes here