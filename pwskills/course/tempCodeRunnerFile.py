import os, sys
from os.path import abspath, dirname, join

## its application
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from payment import payment_details as py
def cfun():
    print("This is my first courese function")

py.pay()