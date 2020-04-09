@echo off
d:
cd D:\test_project\appium_pytest_tea7\test_case
pytest --html=../reports/report.html --self-contained-html
pause