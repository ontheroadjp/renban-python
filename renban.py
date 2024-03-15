#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
from pathlib import Path

def _init():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [options] path extension",
        description="This script renames files with a given extension in the specified directory by prefixing them with a three-digit sequential number.",
        add_help=True,
        epilog="end"
    )
    parser.add_argument("path", type=Path, help="Directory path where files are located")
    parser.add_argument("extension", help="File extension to filter files")
    return parser.parse_args()

def main(args):
    try:
        directory = args.path
        extension = args.extension

        if not directory.exists() or not directory.is_dir():
            raise FileNotFoundError("Directory does not exist: {}".format(directory))

        files = directory.glob("*." + extension)
        if not files:
            print("No files found with the extension '{}' in directory '{}'".format(extension, directory))
        else:
            for index, file in enumerate(files, start=1):
                new_name = "{:03d}_{}".format(index, file.name)
                file.rename(directory.joinpath(new_name))
                print("Renamed '{}' to '{}'".format(file.name, new_name))
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    args = _init()
    main(args)
