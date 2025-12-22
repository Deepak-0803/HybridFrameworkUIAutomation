from utilities import EXCELUtils


class test_only:
    def test_excel_data(self):
        value = EXCELUtils.get_data_from_excel("Sheet1", 1, )
        print(value)