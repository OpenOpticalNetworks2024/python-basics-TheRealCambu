import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re


# Convert JSON data to Python objects
def exercise1(json_string):
    if not isinstance(py_dict, str):
        raise TypeError(f"Expected str for 'json_string', got {type(json_string).__name__}")
    splitted_cleaned_string = json_string[1:-1].replace(" ", "").split(",")
    python_object = {}
    for dictionary in splitted_cleaned_string:
        if ":" in dictionary:
            key, value = dictionary.replace('"', '').split(":", 1)
            python_object[key] = value
    return python_object


# Convert Python object into JSON data
def exercise2(py_dict):
    if not isinstance(py_dict, dict):
        raise TypeError(f"Expected dict for 'py_dict', got {type(py_dict).__name__}")
    len_dict = len(py_dict)
    json_object = "{ "
    for index, (key, value) in enumerate(py_dict.items()):
        json_object += "\"" + key + "\":" + "\"" + str(value) + "\""
        if index != len_dict - 1:
            json_object += ", "
        else:
            json_object += " }"
    return json_object


# Convert Python objects into JSON strings
def exercise3(py_dict):
    if not isinstance(py_dict, dict):
        raise TypeError(f"Expected dict for 'py_dict', got {type(py_dict).__name__}")

    return ["\"" + key + "\": \"" + str(value) + "\"" for key, value in py_dict.items()]


def exercise4():
    pass


def exercise5():
    pass


if __name__ == "__main__":
    json_obj = '{ "Name": "David", "Class": "I", "Age": 6 }'
    python_obj = {
        'Name': 'David',
        'Class': 'I',
        'Age': 6
    }

    # print("EXERCISE SET 1")
    # print("EX1")
    # converted_py_obj = exercise1(json_obj)
    # print(f"Original JSON:\n", {json_obj})
    # print("Converted into Python dictionary:\n", converted_py_obj)

    # print("EX2")
    # converted_json_obj = exercise2(python_obj)
    # print("Original JSON data:\n", json_obj)
    # print("Converted into Python dictionary:\n", converted_json_obj)
    #
    # print("EX3")
    # JSON_strings = exercise3(python_obj)
    # print(f"Original Python object:\n", {json_obj})
    # print("Printing JSON strings...")
    # for idx, string in enumerate(JSON_strings):
    #     print(f"String {idx + 1}: {string}")

    print("EX4")
    exercise4()

    print("EX5")
    exercise5()
