# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import json


class JsonDataReader(DataReader):

    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            data = json.load(file)
            students_list = data['students']
            for name, marks in students_list.items():
                self.students[name] = []
                for subject, mark in marks.items():
                    self.students[name].append((subject, int(mark)))
        return self.students
