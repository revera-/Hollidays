import os
import argparse


CMD = 'python -m unittest -k test_'

parser = argparse.ArgumentParser()
parser.add_argument("--browser", help="Browser to run tests against")
args = parser.parse_args()

os.environ.setdefault('SCREENSHOT_DIR', './screenshots')
os.environ['SELENIUM_BROWSER'] = args.browser or 'chrome'

os.system(CMD)
