import json
import os
import re


def get_current_path():
    current_working_directory = os.getcwd()
    return current_working_directory


def convert_json(str_file):
    write_file_path = get_current_path() + "/json_file.json"
    json_object = str_file.read()
    json_object = json.loads(json_object)
    if isinstance(json_object, dict):
        json_object = json.dumps(json_object, indent=4)

    json_object = re.sub(r'\\n', "", json_object)
    json_object = re.sub(r'\\', "", json_object)
    json_object = re.sub(r'\\n', "", json_object)
    json_object = re.sub(r'"{', "{", json_object)
    json_object = re.sub(r'}"', "}", json_object)
    # Create a new file.
    with open(write_file_path, 'w') as new_json_file:
        new_json_file.write(json_object)
    return json_object


if __name__ == '__main__':
    read_file_path = get_current_path() + "/str_file.txt"
    with open(read_file_path, 'r') as json_file:
        json_obj = convert_json(json_file)
        print(json_obj)
