# -*- coding: utf-8 -*-
import argparse
import pathlib
import sys
from CalcRating import CalcRating
from CalcDebt import CalcDebt
from JsonDataReader import JsonDataReader
from TextDataReader import TextDataReader
from Types import DataType


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def read_data(path: str) -> DataType:
    file_extension = pathlib.Path(path).suffix
    if file_extension == '.txt':
        return TextDataReader().read(path)
    elif file_extension == '.json':
        return JsonDataReader().read(path)
    else:
        raise NameError('Data type is not supported.')


def main():
    path = get_path_from_arguments(sys.argv[1:])

    students = read_data(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    debts = CalcDebt(students).calc()
    print("Students with debts: ", debts)


if __name__ == "__main__":
    main()
