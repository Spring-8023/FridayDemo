# -*- coding:utf-8 -*-
"""
Python 3.7
Author：Spring
Time：  2022/3/8 4:08 PM

"""

import pytest
import datetime

from Friday.App.Test.excel_load import read_excel
from Friday.App.Test.request_client import send

test_data = read_excel('Friday_data.xlsx','Sheet1')
host = "http://192.168.0.8"

@pytest.mark.parametrize('casename,url,method,headers,params,expect_status,expect_busi_code,expect_msg',test_data)
def test_case(casename,url,method,headers,params,expect_status,expect_busi_code,expect_msg):
    params = eval(params)
    resp = send(url=host+url,method=method,headers=headers,**params)
    actual_status = resp.status_code
    actual_busi_code = resp.json()['status']
    if actual_busi_code == -1:

        actual_msg = resp.json()['message']
        pytest.assume(actual_msg == expect_msg)
    # else:

        # pytest.assume(actual_status == expect_status)
        # pytest.assume(actual_busi_code == expect_busi_code)
    assert(actual_status == expect_status)
    assert(actual_busi_code == expect_busi_code)





