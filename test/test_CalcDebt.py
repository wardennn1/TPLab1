# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcDebt import CalcDebt
import pytest
import json


class TestCalcDebt:
    @pytest.fixture()
    def input_data(self) -> tuple[list[DataType], list]:
        data: list[DataType] = [
            {
                "Абрамов Петр Сергеевич":
                    [
                        ("математика", 80),
                        ("русский язык", 76),
                        ("программирование", 100)
                    ],
                "Петров Игорь Владимирович":
                    [
                        ("математика", 61),
                        ("русский язык", 80),
                        ("программирование", 78),
                        ("литература", 97)
                    ]
            },
            {
                "Абрамов Петр Сергеевич":
                    [
                        ("математика", 50),
                        ("русский язык", 76),
                        ("программирование", 43)
                    ],
                "Петров Игорь Владимирович":
                    [
                        ("математика", 61),
                        ("русский язык", 80),
                        ("программирование", 78),
                        ("литература", 97)
                    ]
            },
            {
                "Абрамов Петр Сергеевич":
                    [
                        ("математика", 57),
                        ("русский язык", 34),
                        ("программирование", 21)
                    ],
                "Петров Игорь Владимирович":
                    [
                        ("математика", 60),
                        ("русский язык", 80),
                        ("программирование", 78),
                        ("литература", 45)
                    ]
            }
        ]

        debts_count = [0, 1, 2]

        return data, debts_count

    def test_init_calc_debt(self, input_data: tuple[list[DataType], list]) \
            -> None:
        for data in input_data[0]:
            assert data == CalcDebt(data).data

    def test_calc(self, input_data: tuple[list[DataType], list]) \
            -> None:
        debts = []
        for i, data in enumerate(input_data[0]):
            assert CalcDebt(data).calc() == input_data[1][i]
