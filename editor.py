#!/usr/bin/python3

import re

from ast import literal_eval

mod = [
    [r"(?<=fieldone: )(.*?)(?=\\n)", "1.3.3.7"]
]

rem = [
    r"\\n  sometest:(.*?)(?=(\\n  [a-zA-Z]+))",
]


def remove_key(content, pattern):
    content = repr(content)
    content = re.sub(pattern, '', content)
    content = literal_eval(content)
    return content


def modify_key(content, pattern, value):
    content = repr(content)
    content = re.sub(pattern, value, content)
    content = literal_eval(content)
    return content


def open_yaml(yaml_file_path):
    with open(yaml_file_path, 'r') as file:
        content = file.read()
    return content


def write_yaml(yaml_file_path, content):
    with open(yaml_file_path, 'w') as file:
        file.write(content)

content = open_yaml('example.yaml')

content = remove_key(content, rem[0])
content = modify_key(content, mod[0][0], mod[0][1])

write_yaml('example.yaml.new', content)

