
from os import sys, path
import argparse
sys.path.append(path.dirname( path.abspath(__file__)))
from module.lsjutil.module1 import module1func
from module.lsjutil.module2 import module2func

def a():
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", help="first argument")
    args = parser.parse_args()
    print(parser.parse_args())

    print("a")
    print("b")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", help="first argument")
    args = parser.parse_args()
    print(parser.parse_args())

    print("c")

    module1func()

    module2func()

