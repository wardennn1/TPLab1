# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.JsonDataReader import JsonDataReader
import json


class TestJsonDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = {
            "students": {
                "Иванов Константин Дмитриевич": {
                    "математика": 91,
                    "химия": 100
                },
                "Петров Петр Семенович": {
                    "русский язык": 87,
                    "литература": 78
                }
            }
        }

        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.txt")
        p.write_text(json.dumps(file_and_data_content[0]), encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = JsonDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
