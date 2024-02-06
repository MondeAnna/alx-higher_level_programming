#!/usr/bin/python3


"""
Append CLI Args to JSON
"""


import json
import sys
import os


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main(args):
    """
    Append CLI Args to JSON
    """

    filename = "add_item.json"
    obj = load_from_json_file(filename) if os.path.isfile(filename) else []
    obj.extend(args)
    save_to_json_file(obj, filename)


if __name__ == "__main__":
    args = [] if len(sys.argv) == 1 else sys.argv[1:]
    main(args)
