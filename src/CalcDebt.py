# -*- coding: utf-8 -*-
from Types import DataType


class CalcDebt:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.debt: int = 0

    def marks_tolist(self, marks):
        for mark in marks:
            yield mark[1]

    def calc(self) -> int:
        for _, marks in self.data.items():
            if any(mark < 61 for mark in self.marks_tolist(marks)):
                self.debt += 1
        return self.debt
