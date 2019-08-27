# coidng=utf-8
import unittest, os, time
import HTMLTestRunner
from app.common.sendMail import sendmail
case_path = os.path.join(os.getcwd(), 'case')
report_path = os.path.join(os.getcwd(), 'report')
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py', top_level_dir=None)
    return discover

if __name__=='__main__':
    # runer = unittest.TextTestRunner()
    # runer.run(all_case())
    report_time = time.strftime("%Y-%m-%d %H_%M_%S")
    report_abspath = os.path.join(report_path, report_time + 'result.html')
    with open(report_abspath,'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'自动化测试执行情况')
        runner.run(all_case())
    sendmail(report_abspath)