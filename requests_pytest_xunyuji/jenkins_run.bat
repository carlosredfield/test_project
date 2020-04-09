@echo off
d:
cd D:\test_project\requests_pytest_xunyuji\test_case
pytest --alluredir ../reports/allure_raw
allure serve ../reports/allure_raw
pause