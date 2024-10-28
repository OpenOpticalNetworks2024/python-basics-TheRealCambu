import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
import json


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
        json_object += f'"{key}": "{value}"'
        if index != len_dict - 1:
            json_object += ", "
        else:
            json_object += " }"
    return json_object


# Convert Python objects into JSON strings
def exercise3(py_dict):
    if not isinstance(py_dict, dict):
        raise TypeError(f"Expected dict for 'py_dict', got {type(py_dict).__name__}")

    return [f'"{key}": "{value}"' for key, value in py_dict.items()]


# Write a Python program to convert Python dictionary objects (sort by key) to JSON data.
# Print the object members with indent level 4.
def exercise4(py_dict, indent):
    if not isinstance(py_dict, dict):
        raise TypeError(f"Expected dict for 'py_dict', got {type(py_dict).__name__}")

    # Sort by the keys
    ordered_py_dict = dict(sorted(py_dict.items()))
    len_dict = len(ordered_py_dict)
    json_object = "{\n"
    for index, (key, value) in enumerate(ordered_py_dict.items()):
        json_object += f'{indent}"{key}": "{value}"'
        if index != len_dict - 1:
            json_object += ",\n"
        else:
            json_object += "\n"
    json_object += "}"  # Close the JSON object
    return json_object


def exercise5(json_data, key_to_del):
    for state in json_data.get("states", []):
        if key_to_del in state:
            del state[key_to_del]
            print(f"Deleted 'area_codes' from {state['name']}.")

    return json_data


if __name__ == "__main__":
    json_obj = '{ "Name": "David", "Class": "I", "Age": 6 }'
    python_obj = {
        'Name': 'David',
        'Class': 'I',
        'Age': 6
    }

    print("EXERCISE SET 1")
    print("EX1")
    converted_py_obj = exercise1(json_obj)
    print(f"Original JSON:\n", {json_obj})
    print("Converted into Python dictionary:\n", converted_py_obj)

    print("EX2")
    converted_json_obj = exercise2(python_obj)
    print("Original JSON data:\n", json_obj)
    print("Converted into Python dictionary:\n", converted_json_obj)

    print("EX3")
    JSON_strings = exercise3(python_obj)
    print(f"Original Python object:\n", {json_obj})
    print("Printing JSON strings...")
    for idx, string in enumerate(JSON_strings):
        print(f"String {idx + 1}: {string}")

    print("EX4")
    indent_level = 4
    indentation = " " * 4
    converted_json_obj = exercise4(python_obj, indentation)
    print(f"Original Python object:\n{python_obj}")
    print(f"Converted into JSON data with indent level {indent_level}:\n{converted_json_obj}")

    print("EX5")
    with open("states.json") as file:
        data_json = json.load(file)
    key_to_delete = "area_codes"
    new_json_fpath = "states_no_area_code.json"
    new_json_data_area_code = exercise5(data_json, key_to_delete)
    with open(new_json_fpath, "w") as file:
        json.dump(new_json_data_area_code, file, indent=2)
    print("'area_codes' field removed and the new JSON file has been saved!")
