
class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        print(hasattr(x, 'hello'))
        assert hasattr(x, 'hello')