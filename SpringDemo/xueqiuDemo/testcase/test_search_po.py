from SpringDemo.xueqiuDemo.page.main_page import MainPage


class TestSearchPo:
    def test_search(self):
        assert MainPage().to_search().search("alibaba").get_price() > 200