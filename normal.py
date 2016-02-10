
# Remove vowels from sentence

my_sentence = list("List Comprehensions are the Greatest!")

my_consonants = ''.join([letter for letter in my_sentence if letter not in "aeiou"])
print(my_consonants)

# Open data file


waves = open("waves.csv")
lines = waves.readlines()
waves.close()

# Create list of water temps for each day


def temps(item):
    return [line.strip().split(',')[-2:] for line in item]

temp_date = temps(lines)
print(temp_date)

# Convert water temps from string to float


def water_list(temp_and_date):
    return [float(_[0]) for _ in temp_and_date[1:]]

float_list = water_list(temp_date)
print(float_list)

# Convert Celsius floats


def fahrenheit(celsius_floats):
    return [int(float_c * (9 / 5)) + 32 for float_c in celsius_floats]
fahrenheit_list = fahrenheit(float_list)

# Create a list from each line of waves.csv


def full_list(data_lines):
    return [line.strip().split(',') for line in data_lines]

data_list = full_list(lines)

# Create a dict of date and wave height from list of lines in previous function
waves_dict = {data[-1]: float(data[1]) for data in data_list[1:]}


# Use dict values to calculate the average wave height for each day
waves_avg = {"waves_avg": sum(waves_dict.values()) / len(waves_dict)}
print(waves_avg)

# Create Homework Grades dict
homework_dict = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
                 'Jordan': {'Homework 1': 92, 'Homework 2': 87},
                 'Peyton': {'Homework 1': 84, 'Homework 2': 77},
                 'River': {'Homework 1': 85, 'Homework 2': 91}
                 }

# Create list of hw scores using list comprehension
hw1 = [value["Homework 1"] for key, value in homework_dict.items()]

hw1_avg = sum(hw1) / len(hw1)
print(hw1_avg)
