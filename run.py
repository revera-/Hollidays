import os
import argparse


os.system('rm -rf reports')
os.system('mkdir -p reports')

parser = argparse.ArgumentParser()
parser.add_argument("--browser", help="Browser to run tests against")
parser.add_argument("--test", help="Test to run")
args = parser.parse_args()

#CMD = f'python -m unittest -k test_ {args.test if args.test else ""}'
CMD = f'python -m unittest -v test_login.py {args.test if args.test else ""}'

os.environ.setdefault('SCREENSHOT_DIR', './reports/screenshots')
os.environ.setdefault('SELENIUM_DRIVER_LOG_DIR', './reports')
os.environ['SELENIUM_BROWSER'] = args.browser or 'chrome'
os.environ['SAVED_SOURCE_DIR'] = './reports/src'
os.environ['TESTS_BASE_URL'] = 'https://tms-lite-test1.artlogics.ru/'

os.system(CMD)
