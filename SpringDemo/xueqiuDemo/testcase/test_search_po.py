import pytest
from SpringDemo.xueqiuDemo.page.main_page import MainPage


class TestSearchPo:
    @pytest.mark.parametrize("name, price", [
        ('alibaba', 200),
        ('jd', 8),
        ('baidu', 50)
    ])
    def test_search(self, name, price):
        assert MainPage().to_search().search(name).get_price() > price