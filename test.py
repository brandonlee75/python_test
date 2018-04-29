
from os import sys, path
import argparse
sys.path.append(path.dirname( path.abspath(__file__)))
from module.lsjutil.module1 import *
from module.lsjutil.module2 import *

def a():
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", help="first argument")
    args = parser.parse_args()
    print(args)

    print("a")
    print("b")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", help="first argument")
    args = parser.parse_args()
    print(parser.parse_args())

    print("c")

    module1func()
    module1.module1func()

    module2func()
    module2.module2func()

