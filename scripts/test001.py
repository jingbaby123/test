import pytest, allure

class Test_001:
    @allure.step(title='测试步骤001')
    @pytest.mark.parametrize("a",[1,2,3])
    def tests_ab(self,a):
        assert a!=3

    @allure.step(title='测试步骤2')
    @pytest.mark.parametrize("a",[5,6,7])
    def test_dd(self,a):
        allure.attach('描述','ceshibuzhou2demaioshu')
        assert a !=4
