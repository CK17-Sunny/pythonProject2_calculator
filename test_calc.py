import sys
import pytest
import yaml

sys.path.append('..')

from pythoncode.Calcuator import Calculator


def get_datas():
    with open("./datas/calc.yml") as f:
        data2 = yaml.safe_load(f)
        return data2['add']['datas'], data2['div']['datas']


class TestCalc:
    middle_data = get_datas()

    def setup_class(self):
        print("开始计算")
        self.cal = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize("a, b, result", middle_data[0])
    def test_add(self, a, b, result):
        for i in [a, b, result]:
            if type(i) == int or float:
                assert result == round(self.cal.add(a, b), 2)
                print(f"a={a}, b={b}, result={result}")
            else:
                raise TypeError("请输入数字")

    @pytest.mark.parametrize("a, b, result", middle_data[1])
    def test_div(self, a, b, result):
        if b != 0:
            assert result == self.cal.div(a, b)
        else:
            raise ZeroDivisionError("b等于0, 这里有个异常")
