# -*- coding:utf-8 -*-
"""
Python 3.7
Author：Spring
Time：  2022/3/17 10:02 AM

"""
import pytest
import os
import allure
from typing import List

_driver = None
# 该文件是pytest测试框架,使用pytest_collection_modifyitems钩子函数去除乱码
def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    # items.reverse()
    for item in items:
        #修改编码
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode_escape')
        # item._nodeid = item._nodeid.encode('utf-8').decode('latin1')

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pass
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

    '''